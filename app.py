from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Simulated database (in a real app, you'd use a proper database)
class Database:
    def __init__(self):
        self.volunteers = []
        self.organizations = []
        self.opportunities = []

db = Database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would implement actual login logic
        flash('Inicio de sesión exitoso!')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes-somos.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Here you would implement actual registration logic
        flash('¡Registro exitoso! Nos pondremos en contacto contigo pronto.')
        return redirect(url_for('index'))
    return render_template('registro.html')

@app.route('/cupos')
def cupos():
    # In a real application, you would fetch this from a database
    opportunities = [
        {
            'title': 'Desarrollador Web',
            'organization': 'Fundación Educativa',
            'location': 'Ciudad de México',
            'duration': '3 meses',
            'age_range': '18-35 años',
            'spots': 3
        },
        # Add more opportunities as needed
    ]
    return render_template('cupos.html', opportunities=opportunities)

@app.route('/postular/<int:opportunity_id>', methods=['POST'])
def postular(opportunity_id):
    # Here you would implement the application logic
    flash('¡Gracias por tu interés! Nos pondremos en contacto contigo pronto.')
    return redirect(url_for('cupos'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)