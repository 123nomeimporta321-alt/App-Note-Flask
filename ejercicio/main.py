# Importar
from flask import Flask, render_template,request, redirect
# Importando la biblioteca de bases de datos
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Conectando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creación de una base de datos
db = SQLAlchemy(app )

#Asignación #1. Crear una tabla de base de datos











# Ejecutar la página con contenido
@app.route('/')
def index():
    # Visualización de los objetos de la DB
    # Asignación #2. Mostrar los objetos de la DB en index.html
    

    return render_template('index.html',
                           #tarjetas = tarjetas

                           )

# Ejecutar la página con la tarjeta
@app.route('/card/<int:id>')
def card(id):
    # Asignación #2. Mostrar la tarjeta correcta por su id
    

    return render_template('card.html', card=card)

# Ejecutar la página y crear la tarjeta
@app.route('/create')
def create():
    return render_template('create_card.html')

# El formulario de la tarjeta
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Asignación #2. Crear una forma de almacenar datos en la DB
        




        return redirect('/')
    else:
        return render_template('create_card.html')
    
# función CLI para inicializar la base de datos
@app.cli.command("init-db")
def init_db_command():
    db.create_all()
    print("Base de datos inicializada.")
    #
    # Comandos para ejecutar la inicialización de BD en distintos terminales:
    #
    # Git Bash:
    #   export FLASK_APP=main.py
    #   flask init-db && flask run
    #
    # PowerShell:
    #   $env:FLASK_APP = "main.py"
    #   flask init-db; flask run
    #
    # CMD (Símbolo del sistema):
    #   set FLASK_APP=main.py
    #   flask init-db && flask run
    #
    # Alternativa sin variables de entorno (independiente del shell):
    #   ./venv/Scripts/flask.exe --app main init-db
    #   ./venv/Scripts/flask.exe --app main run

if __name__ == "__main__":
    app.run(debug=True)
