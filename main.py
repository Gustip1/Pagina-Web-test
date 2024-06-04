from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'Clave Secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form.get("name")
        password = request.form.get("password")
        
        
        hashed_password = generate_password_hash(password)
        
       
        new_user = User(name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        session["name"] = name
        return redirect("/")
    
    return render_template("register.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form.get("name")
        password = request.form.get("password")
        user = User.query.filter_by(name=name).first()
        
        if user and check_password_hash(user.password, password):
            session["name"] = user.name
            return redirect("/")
        else:
            return "Nombre o contraseña incorrectos"
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)



