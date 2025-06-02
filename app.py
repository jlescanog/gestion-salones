from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # Importa SQLAlchemy
import os # Necesario para construir la ruta al archivo de la BD
import datetime # Necesario para manejar fechas

# Obtener la ruta absoluta del directorio donde está app.py
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'gestion_congregacion.db')
# La línea anterior crea un archivo llamado 'gestion_congregacion.db' en el mismo directorio de app.py
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactiva notificaciones innecesarias

# Inicializar la extensión SQLAlchemy con nuestra aplicación Flask
db = SQLAlchemy(app)

# --- Aquí definiremos nuestros modelos de base de datos (tablas) ---

# --- Definición de Modelos de Base de Datos ---
class Miembro(db.Model):
    __tablename__ = 'miembros' # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True) # id_miembro
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=True) # DNI puede ser opcional o no, y único
    correo_electronico = db.Column(db.String(120), unique=True, nullable=True)
    numero_celular = db.Column(db.String(20), nullable=True)
    # Para fecha_nacimiento y fecha_registro, usaremos DateTime
    # Importa datetime al principio del archivo: import datetime
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    direccion = db.Column(db.String(200), nullable=True)
    # id_grupo_limpieza y roles_especiales los podemos añadir/refinar luego.
    # Por ahora, nos enfocamos en los campos básicos.
    # Para fecha_registro, podemos usar un valor por defecto:
    fecha_registro = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # Representación del objeto (útil para debugging)
    def __repr__(self):
        return f'<Miembro {self.nombres} {self.apellidos}>'

@app.route('/')
def hola_mundo():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)