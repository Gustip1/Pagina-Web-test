from flask import Flask, render_template, request, session, redirect, url_for
from models import db, Sucursal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config.from_object('config')
db.init_app(app)

@app.route('/')
def index():
    if "sucursal_id" not in session:
        return redirect(url_for('sucursal'))
    sucursales = Sucursal.query.order_by(Sucursal.id).all()  # Ordenar por ID
    return render_template('index.html', sucursales=sucursales)

@app.route("/sucursal/<int:sucursal_id>/ingresar")
def ingresar_sucursal(sucursal_id):
    sucursal = Sucursal.query.get_or_404(sucursal_id)
    # Aquí puedes realizar cualquier acción relacionada con ingresar a la sucursal
    return render_template('sucursal_detail.html', sucursal=sucursal)


@app.route("/logout")
def logout():
    session.pop("sucursal_id", None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
