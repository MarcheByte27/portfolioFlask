from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

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

        msg = Message(subject=f"Nuevo mensaje de {name} (Portafolio Flask)",
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"
        
        try:
            mail.send(msg)
            flash("¡Mensaje enviado con éxito! Te responderé lo antes posible.", "success")
        except Exception as e:
            flash(f"Hubo un error al enviar el mensaje. Verifica tu configuración. Detalle: {str(e)}", "danger")
            
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', threaded=True)
