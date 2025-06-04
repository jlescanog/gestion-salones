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
        return redirect(url_for('ver_miembros'))

    # Si el método es GET, simplemente muestra el formulario
    return render_template('registrar_miembro.html')

# NUEVA RUTA PARA VER TODOS LOS MIEMBROS
@app.route('/miembros')
def ver_miembros():
    # Consultar todos los miembros de la base de datos
    # El método .all() devuelve una lista de todos los objetos Miembro
    todos_los_miembros = Miembro.query.all()
    
    # Renderizar una nueva plantilla HTML y pasarle la lista de miembros
    return render_template('ver_miembros.html', miembros=todos_los_miembros)

# NUEVA RUTA PARA EDITAR UN MIEMBRO
@app.route('/miembro/editar/<int:miembro_id>', methods=['GET', 'POST'])
def ruta_editar_miembro(miembro_id):
    # Obtener el miembro de la base de datos por su ID
    # .first_or_404() es útil: obtiene el primero o devuelve un error 404 si no se encuentra
    miembro_para_editar = Miembro.query.get_or_404(miembro_id)

    if request.method == 'POST':
        # Actualizar los campos del miembro con los datos del formulario
        miembro_para_editar.nombres = request.form['nombres']
        miembro_para_editar.apellidos = request.form['apellidos']
        miembro_para_editar.dni = request.form['dni']
        miembro_para_editar.correo_electronico = request.form['correo_electronico']
        miembro_para_editar.numero_celular = request.form['numero_celular']
        
        fecha_nac_str = request.form['fecha_nacimiento']
        if fecha_nac_str:
            try:
                miembro_para_editar.fecha_nacimiento = datetime.datetime.strptime(fecha_nac_str, '%Y-%m-%d').date()
            except ValueError:
                miembro_para_editar.fecha_nacimiento = None # o manejar error
        else:
            miembro_para_editar.fecha_nacimiento = None
            
        miembro_para_editar.direccion = request.form['direccion']

        # Confirmar los cambios en la base de datos
        try:
            db.session.commit()
            # Podríamos añadir un mensaje flash de éxito aquí
            return redirect(url_for('ver_miembros'))
        except Exception as e:
            db.session.rollback() # Revertir cambios si hay un error
            # Podríamos añadir un mensaje flash de error aquí y mostrar el formulario de nuevo
            # print(f"Error al actualizar: {e}") # Para depuración
            # Por ahora, solo redirigimos o mostramos el form de nuevo
            return render_template('editar_miembro.html', miembro_a_editar=miembro_para_editar, error="Error al guardar cambios.")


    # Si el método es GET, simplemente muestra el formulario con los datos actuales del miembro
    return render_template('editar_miembro.html', miembro_a_editar=miembro_para_editar)

# NUEVA RUTA PARA ELIMINAR UN MIEMBRO
@app.route('/miembro/eliminar/<int:miembro_id>', methods=['POST']) # Solo aceptar POST
def ruta_eliminar_miembro(miembro_id):
    # Obtener el miembro de la base de datos por su ID
    miembro_para_eliminar = Miembro.query.get_or_404(miembro_id)

    try:
        db.session.delete(miembro_para_eliminar)
        db.session.commit()
        # Podríamos añadir un mensaje flash de éxito aquí: "Miembro eliminado correctamente."
    except Exception as e:
        db.session.rollback()
        # Podríamos añadir un mensaje flash de error aquí: "Error al eliminar el miembro."
        # print(f"Error al eliminar: {e}") # Para depuración
    
    # Redirigir siempre a la lista de miembros
    return redirect(url_for('ver_miembros'))

if __name__ == '__main__':
    app.run(debug=True)