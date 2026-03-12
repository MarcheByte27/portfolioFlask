from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

WEB3FORMS_KEY = os.environ.get('WEB3FORMS_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/habilidades')
def skills():
    return render_template('skills.html')

@app.route('/proyectos')
def projects():
    return render_template('projects.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        payload = {
            'access_key': WEB3FORMS_KEY,
            'name': name,
            'email': email,
            'message': message,
            'subject': f'Nuevo mensaje de {name} (Portafolio Flask)',
        }

        try:
            response = requests.post('https://api.web3forms.com/submit', json=payload, timeout=10)
            if response.status_code == 200 and response.json().get('success'):
                flash('¡Mensaje enviado con éxito! Te responderé lo antes posible.', 'success')
            else:
                flash('Hubo un error al enviar el mensaje. Inténtalo de nuevo.', 'danger')
        except Exception as e:
            flash(f'Error de conexión al enviar el mensaje: {str(e)}', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', threaded=True)
