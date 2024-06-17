from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(30), nullable=False)
    localidad = db.Column(db.String(30), nullable=False)
    direccion = db.Column(db.String(60), nullable=False)
    paquetes = db.relationship('Paquete', backref='sucursal', lazy=True)
    transportes_destino = db.relationship('Transporte', backref='sucursal_destino_ref', lazy=True)

class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(60), nullable=False)
    dni = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    paquetes = db.relationship('Paquete', backref='repartidor', lazy=True)

class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.Integer, nullable=False)
    fechahorasalida = db.Column(db.DateTime, nullable=False)
    fechahorallegada = db.Column(db.DateTime)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='transporte', lazy=True)

class Paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.Integer, nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    dirdestinatario = db.Column(db.String(60), nullable=False)
    nomdestinatario = db.Column(db.String(60), nullable=False)
    entregado = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.String(100))
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))
