# Portfolio - iaFlaskProject

Este es un proyecto de portafolio personal desarrollado utilizando **Python** y el framework web **Flask**.

## Arquitectura del Proyecto

El proyecto está diseñado de forma modular utilizando las características de Flask y los motores de plantillas (Jinja2) para separar correctamente la lógica de backend y la presentación:

- **Backend en Flask (`app.py`)**: Define las rutas principales del sitio y se encarga de renderizar la vista correspondiente. Las rutas disponibles son:
  - `/` -> Inicio (`index.html`)
  - `/habilidades` -> Habilidades (`skills.html`)
  - `/proyectos` -> Proyectos (`projects.html`)
  - `/contacto` -> Contacto (`contact.html`)
  
- **Sistema de Templates Separados**: Las diferentes páginas en HTML constan de archivos propios ubicados en el directorio `templates/`. Esta separación facilita la organización y mantenibilidad del código del frontend.

- **Uso de Partials**: Para evitar la repetición de código y mantener una estructura limpia, se hace uso de plantillas parciales (por ejemplo, `partials/header.html`), de tal forma que los elementos comunes a todas las páginas puedan incluirse fácilmente usando la sintaxis de Jinja.

## Cómo ejecutar el proyecto en modo desarrollo

1. Asegúrate de tener Python instalado en tu sistema.
2. Se recomienda crear y activar un entorno virtual.
3. Instala las dependencias necesarias (principalmente Flask):
   ```bash
   pip install Flask
   ```
4. Ejecuta el archivo principal de la aplicación:
   ```bash
   python app.py
   ```
5. Abre tu navegador web de preferencia y accede a la dirección que indica la consola, típicamente: `http://127.0.0.1:5000`.
