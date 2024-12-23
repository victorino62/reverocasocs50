import os
import time
import sqlite3

from forms import ContactForm
from flask_mail import Mail, Message
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_socketio import SocketIO
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from helpers import apology, login_required

# Configure application
app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = 'revercs50'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seu_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'sua_senha'
mail = Mail(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
#@login_required
def index():
    """home"""
    return render_template("index.html")


@app.route("/music")
#@login_required
def music():
    """music"""
    return render_template("music.html")

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContactForm()
    if form.validate_on_submit():
        # Processar o formulário aqui (ex: enviar e-mail ou salvar no banco)
        flash('Mensagem enviada com sucesso!', 'success')
        return redirect('/contato')
    return render_template('contato.html', form=form)


@app.route('/newsletter', methods=['POST'])
def newsletter():
    email = request.form.get('email')
    with sqlite3.connect('newsletter.db') as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS subscribers (id INTEGER PRIMARY KEY, email TEXT)")
        cursor.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
        conn.commit()

    flash('Obrigado por se inscrever na nossa newsletter!', 'success')
    return redirect(url_for('index'))


@app.route('/admin/newsletter')
def admin_newsletter():
    with sqlite3.connect('newsletter.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM subscribers")
        emails = cursor.fetchall()
    return render_template('admin_newsletter.html', emails=emails)



class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.css') or event.src_path.endswith('.html') or event.src_path.endswith('.js'):
            socketio.emit('file_changed')




if __name__ == "__main__":
    observer = Observer()
    observer.schedule(ChangeHandler(), path='static', recursive=True)
    observer.start()
    try:
        socketio.run(app, debug=True)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()