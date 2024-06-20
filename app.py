from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Sucursal, Paquete, Transporte
import random
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config.from_object('config')
db.init_app(app)

@app.route('/')
def index():
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    return render_template('index.html', sucursales=sucursales)

@app.route("/crear_paquete", methods=['GET', 'POST'])
def crear_paquete():
    if request.method == 'POST':
        try:
            idsucursal = request.form.get('sucursal_id')
            peso = request.form.get('peso')
            direccion = request.form.get('direccion')
            nomdestinatario = request.form.get('nomdestinatario')
            if not nomdestinatario:
                flash('Nombre del destinatario es obligatorio', 'error')
                return redirect(url_for('crear_paquete'))

            entregado = 'entregado' in request.form
            observaciones = request.form.get('observaciones')
            numerodeenvio = random.randint(1000, 1500)
            id_transporte = request.form.get('idtransporte')
            id_repartidor = request.form.get('idrepartidor')

            paquete = Paquete(
                numeroenvio=numerodeenvio,
                idsucursal=idsucursal,
                peso=peso,
                dirdestinatario=direccion,
                nomdestinatario=nomdestinatario,
                entregado=entregado,
                observaciones=observaciones,
                idtransporte=id_transporte,
                idrepartidor=id_repartidor
            )

            db.session.add(paquete)
            db.session.commit()
            flash('Paquete creado exitosamente', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Hubo un error al crear el paquete: {}'.format(str(e)), 'error')

        return redirect(url_for('index'))
    else:
        sucursales = Sucursal.query.order_by(Sucursal.numero).all()
        return render_template('crear_paquete.html', sucursales=sucursales)

@app.route("/salida_transporte", methods=['GET', 'POST'])
def salida_transporte():
    if request.method == 'POST':
        try:
            sucursal_destino_id = request.form.get('sucursal_destino')
            paquete_ids = request.form.getlist('paquete_ids')

            if sucursal_destino_id and paquete_ids:
                transporte = Transporte(
                    numerotransporte=random.randint(1000, 9999),
                    fechahorasalida=datetime.datetime.now(),
                    idsucursal=sucursal_destino_id
                )
                db.session.add(transporte)
                db.session.commit()

                for paquete_id in paquete_ids:
                    paquete = Paquete.query.get(paquete_id)
                    if paquete:
                        paquete.idtransporte = transporte.id
                        paquete.idsucursal = sucursal_destino_id  # Esta es la línea modificada
                        db.session.commit()

                flash('Transporte registrado exitosamente', 'success')
            else:
                flash('Seleccione una sucursal destino y al menos un paquete', 'error')
        except Exception as e:
            db.session.rollback()
            flash('Hubo un error al registrar el transporte: {}'.format(str(e)), 'error')

        return redirect(url_for('index'))
    else:
        sucursales = Sucursal.query.order_by(Sucursal.numero).all()
        return render_template('seleccionar_sucursal.html', sucursales=sucursales)

@app.route("/seleccionar_paquetes", methods=['GET'])
def seleccionar_paquetes():
    sucursal_id = request.args.get('sucursal_destino')
    if not sucursal_id:
        flash('Seleccione una sucursal destino', 'error')
        return redirect(url_for('salida_transporte'))

    # Filtramos paquetes que no están entregados y no tienen repartidor asignado
    paquetes = Paquete.query.filter_by(entregado=0, idrepartidor=0).all()
    if not paquetes:
        flash('No hay paquetes disponibles para transporte', 'info')
    
    return render_template('seleccionar_paquetes.html', sucursal_id=sucursal_id, paquetes=paquetes)

@app.route("/llegada_transporte", methods=['GET', 'POST'])
def llegada_transporte():
    if request.method == 'POST':
        try:
            transporte_id = request.form.get('transporte_id')

            if transporte_id:
                transporte = Transporte.query.get(transporte_id)
                if transporte:
                    transporte.fechahorallegada = datetime.datetime.now()
                    db.session.commit()
                    flash('Llegada del transporte registrada exitosamente', 'success')
                else:
                    flash('Transporte no encontrado', 'error')
            else:
                flash('Seleccione un transporte', 'error')
        except Exception as e:
            db.session.rollback()
            flash('Hubo un error al registrar la llegada del transporte: {}'.format(str(e)), 'error')

        return redirect(url_for('index'))
    else:
        sucursales = Sucursal.query.order_by(Sucursal.numero).all()
        return render_template('seleccionar_sucursal_llegada.html', sucursales=sucursales)

@app.route("/transportes_pendientes")
def transportes_pendientes():
    sucursal_id = request.args.get('sucursal_id')
    if not sucursal_id:
        flash('Seleccione una sucursal', 'error')
        return redirect(url_for('llegada_transporte'))

    transportes = Transporte.query.filter_by(idsucursal=sucursal_id, fechahorallegada=None).all()
    return render_template('transportes_pendientes.html', transportes=transportes)

if __name__ == '__main__':
    app.run(debug=True)
