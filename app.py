from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import datetime

# Obtener la ruta absoluta del directorio donde está app.py
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'gestion_congregacion.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

# --- Definición de Modelos de Base de Datos ---
class Miembro(db.Model):
    __tablename__ = 'miembros' # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True) # id_miembro
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=True) # DNI puede ser opcional o no, y único
    correo_electronico = db.Column(db.String(120), unique=True, nullable=True)
    numero_celular = db.Column(db.String(20), nullable=True)
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    direccion = db.Column(db.String(200), nullable=True)
    # id_grupo_limpieza y roles_especiales los podemos añadir/refinar luego.
    # Para fecha_registro, podemos usar un valor por defecto:
    fecha_registro = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Miembro {self.nombres} {self.apellidos}>'

@app.route('/')
def hola_mundo():
    return render_template('index.html')

# NUEVA RUTA PARA REGISTRAR MIEMBROS
@app.route('/registrar', methods=['GET', 'POST']) # Permite métodos GET y POST
def ruta_registrar_miembro():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        dni = request.form['dni']
        correo = request.form['correo_electronico']
        celular = request.form['numero_celular']
        # Para la fecha, hay que convertirla de string a objeto date
        fecha_nac_str = request.form['fecha_nacimiento']
        fecha_nac = None
        if fecha_nac_str:
            try:
                fecha_nac = datetime.datetime.strptime(fecha_nac_str, '%Y-%m-%d').date()
            except ValueError:
                pass 
        
        direccion = request.form['direccion']

        # Crear una nueva instancia del modelo Miembro
        nuevo_miembro = Miembro(
            nombres=nombres,
            apellidos=apellidos,
            dni=dni,
            correo_electronico=correo,
            numero_celular=celular,
            fecha_nacimiento=fecha_nac,
            direccion=direccion
        )

        # Añadir el nuevo miembro a la sesión de la base de datos
        db.session.add(nuevo_miembro)
        # Confirmar los cambios en la base de datos
        db.session.commit()

        # Redirigir a alguna página (ej. la página de inicio o una de confirmación)
        return redirect(url_for('hola_mundo'))

    # Si el método es GET, simplemente muestra el formulario
    return render_template('registrar_miembro.html')

if __name__ == '__main__':
    app.run(debug=True)