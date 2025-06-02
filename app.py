from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta y la función que se ejecutará cuando se acceda a esa ruta
@app.route('/')  # Esta es la ruta raíz o principal de tu sitio (ej. http://localhost:5000/)
def hola_mundo():
    return '¡Hola, Mundo desde Flask!'

# Esto es para asegurar que el servidor de desarrollo solo se ejecute
# cuando el script es ejecutado directamente (no cuando es importado)
if __name__ == '__main__':
    app.run(debug=True) # debug=True es útil durante el desarrollo para ver errores 