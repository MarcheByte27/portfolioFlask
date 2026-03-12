from flask import Flask, render_template, request, flash, redirect, url_for
import resend
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

resend.api_key = os.environ.get('RESEND_API_KEY')
TO_EMAIL = os.environ.get('TO_EMAIL')

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

        try:
            resend.Emails.send({
                "from": "Portafolio <onboarding@resend.dev>",
                "to": [TO_EMAIL],
                "reply_to": email,
                "subject": f"Nuevo mensaje de {name} (Portafolio Flask)",
                "html": f"""
                    <h2>Nuevo mensaje de contacto</h2>
                    <p><strong>Nombre:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Mensaje:</strong></p>
                    <p>{message}</p>
                """,
            })
            flash('¡Mensaje enviado con éxito! Te responderé lo antes posible.', 'success')
        except Exception as e:
            flash(f'Error al enviar el mensaje: {str(e)}', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', threaded=True)
