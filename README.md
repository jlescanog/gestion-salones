# Sistema de Gestión de Asignaciones para Congregaciones

## 🎯 Propósito del Proyecto

Este proyecto es una aplicación web de código abierto diseñada para ayudar a las congregaciones JW a gestionar los horarios y asignaciones de sus reuniones. El objetivo principal es reemplazar los métodos manuales (como PDFs compartidos) por un sistema centralizado, accesible y fácil de usar, especialmente desde dispositivos móviles.

La aplicación permitirá registrar miembros, definir roles, programar diferentes tipos de reuniones y asignar participantes a diversas responsabilidades dentro de estas reuniones. Cada congregación podrá alojar su propia instancia de la aplicación (auto-alojamiento).

## ✨ Características Actuales (Fase 1 - MVP en desarrollo)

* Gestión completa de Miembros de la congregación (CRUD):
    * Registrar nuevos miembros.
    * Ver la lista de todos los miembros registrados.
    * Editar la información de miembros existentes.
    * Eliminar miembros.
* Estructura básica de la aplicación web con Flask.
* Uso de base de datos SQLite para el almacenamiento de datos.
* Interfaz de usuario básica renderizada a través de plantillas HTML.

## 🛠️ Tecnologías Utilizadas

* **Backend**: Python 3 con Flask
* **Base de Datos**: SQLite3
* **Frontend**: HTML, CSS, JavaScript (actualmente mínimo)
* **Gestión de Base de Datos (ORM)**: Flask-SQLAlchemy
* **Entorno Virtual**: `venv`

## 📋 Prerrequisitos

Antes de empezar, asegúrate de tener instalado en tu sistema:

* [Python 3](https://www.python.org/downloads/) (versión 3.7 o superior recomendada)
* [Git](https://git-scm.com/downloads/)

## 🚀 Configuración e Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1.  **Clonar el Repositorio:**
    Abre tu terminal y clona el repositorio del proyecto desde GitHub:
    ```bash
    git clone (https://github.com/jlescanog/gestion-salones.git)
    ```
2.  **Navegar al Directorio del Proyecto:**
    ```bash
    cd gestion-salones
    ```
    (Ej. `cd gestion-salones`)

3.  **Crear un Entorno Virtual:**
    Es altamente recomendado usar un entorno virtual para aislar las dependencias del proyecto.
    ```bash
    python3 -m venv venv
    ```
    (En Windows, puedes usar `python -m venv venv`)

4.  **Activar el Entorno Virtual:**
    * En Linux/macOS:
        ```bash
        source venv/bin/activate
        ```
    * En Windows (PowerShell o CMD):
        ```bash
        .\venv\Scripts\activate
        ```
    Verás `(venv)` al inicio del prompt de tu terminal si se activó correctamente.

5.  **Instalar Dependencias:**
    Con el entorno virtual activo, instala los paquetes necesarios usando el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

6.  **Crear la Base de Datos y las Tablas:**
    Ejecuta el script proporcionado para inicializar la base de datos SQLite y crear las tablas necesarias:
    ```bash
    python create_tables.py
    ```
    Deberías ver un mensaje "¡Tablas creadas exitosamente!" y se creará un archivo `gestion_congregacion.db` en el directorio raíz del proyecto.

## ▶️ Ejecutar la Aplicación

1.  Asegúrate de que tu entorno virtual esté activo.
2.  Navega al directorio raíz del proyecto en tu terminal.
3.  Ejecuta la aplicación Flask:
    ```bash
    python app.py
    ```
    (O `python3 app.py` dependiendo de tu configuración de Python)
4.  Abre tu navegador web y ve a la siguiente dirección:
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

    Deberías ver la página de inicio de la aplicación. Desde allí podrás navegar a `/registrar` para añadir miembros o a `/miembros` para ver la lista.

## 🤝 Cómo Contribuir

¡Las contribuciones son bienvenidas! Si deseas colaborar con el proyecto, por favor sigue estos pasos:

1.  **Haz un Fork** del repositorio en GitHub.
2.  **Crea una Nueva Rama** para tus cambios: `git checkout -b caracteristica/nueva-funcionalidad` o `git checkout -b correccion/error-especifico`.
3.  **Realiza tus Cambios**: Implementa nuevas funcionalidades, corrige errores, mejora la documentación, etc.
    * Intenta seguir el estilo de código existente. Para Python, nos adherimos a las convenciones de [PEP 8](https://www.python.org/dev/peps/pep-0008/).
4.  **Prueba tus Cambios**: Asegúrate de que tus cambios no rompan la funcionalidad existente.
5.  **Haz Commit** de tus cambios: `git commit -m "Agrega nueva funcionalidad X"`
6.  **Haz Push** a tu rama: `git push origin caracteristica/nueva-funcionalidad`
7.  **Abre un Pull Request** en el repositorio original. Describe claramente los cambios que has realizado.

También puedes contribuir abriendo "Issues" en GitHub si encuentras errores o tienes sugerencias para nuevas funcionalidades.

## 📝 Plan de Desarrollo Futuro (Resumen)

* Gestión de Roles Asignables.
* Gestión de Grupos de Limpieza/Congregación.
* Programación de Reuniones (Entre Semana y Fin de Semana) con asignación de partes.
* Portal de autogestión para oradores invitados (Fase 2).
* Mejoras en la interfaz de usuario y experiencia del usuario (mensajes flash, etc.).
* Internacionalización (traducción a otros idiomas).

---
