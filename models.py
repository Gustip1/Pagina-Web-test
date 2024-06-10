from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    provincia = db.Column(db.String(30))
    localidad = db.Column(db.String(30))
    direccion = db.Column(db.String(60))

class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    nombre = db.Column(db.String(60))
    dni = db.Column(db.String(8))
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class Paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.Integer)
    peso = db.Column(db.Integer)
    nomdestinatario = db.Column(db.String(60))
    dirdestinatario = db.Column(db.String(100))
    entregado = db.Column(db.Boolean)
    observaciones = db.Column(db.Text)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))

class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.Integer)
    fechahorasalida = db.Column(db.DateTime)
    fechahorallegada = db.Column(db.DateTime)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
