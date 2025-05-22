# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: May 2nd, 2025
# | Last update..: May 21th, 2025
# | WhatIs.......: CongressMU - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Jinja Expressions: https://jinja.palletsprojects.com/en/stable/templates/#jinja-filters.length
# SweetAlert Js with Flask: https://github.com/elijahondiek/SweetAlert-Js-with-Flask
# How to connect Python programs to MariaDB: https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
# Flask with MariaDB: A Comprehensive Guide: https://readmedium.com/flask-with-mariadb-a-comprehensive-guide-0be504b0970f

# ------------------------- Libraries -------------------------
# Flask imports
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap5

# Integrate MariaDB to app
import MySQLdb
import mariadb

# Hashing
import bcrypt

# Cardui classes
from form import LogInForm, SignUpForm, NewArticleForm, EvaluationForm, FinalEvaluationForm
from dashboard import Dashboard


# ------------------------- Variables -------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Title Options
titleOptions = {
    "Title": [(0, 'Ninguno'), (1, 'Ing.'), (2, 'Lic.'), (3, 'Mtr.'), (4, 'Phd.')]
}

# Category Options
categoryOptions = {
    "Category": [(0, 'Inclusión'), (1, 'Tecnología educativa'), (2, 'Cloud en en la escuela')]
}

# Evaluation Options
evaluationOptions = {
    "Criteria": [
        (1, '¿Hay claridad en el propósito u objetivo de la investigación o del texto?'),
        (2, '¿Se presentan datos de forma clara y ordenada, se informa su origen y se evidencia su relación con el texto?'),
        (3, 'En caso de que el texto incluya hipótesis, ¿éstas se encuentran explicitadas de manera clara y articuladas con la introducción y la teoría? ¿Los resultados aportan conceptualización o contribuyen a resolver un problema?'),
        (4, '¿Hay precisión de las definiciones conceptuales? ¿Se evidencia rigor en la recolección de los datos? (sistematización)'),
        (5, '¿El articulo sigue el formato APA?')
    ],
    "Grade": [(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')],
    "Conclusion": [(0, 'Aceptado sin modificaciones'), (1, 'Aceptado con modificaciones básicas'), (2, 'Aceptado con modificaciones básicas y algunas de estructura'), (3, 'Evaluar, reescribir contenidos y presentar a una próxima convocatoria para nueva evaluación'), (4, 'No Aceptado')]
}

# Articles Assignment Options
articlesAssignmentCategories = {
    "EvaluatorCategories": [(0, 'Inclusión'), (1, 'Tecnología educativa'), (2, 'Cloud en en la escuela')],
    "ArticleCategories": [(0, 'Inclusión'), (1, 'Tecnología educativa'), (2, 'Cloud en en la escuela')]
}

articlesAssignmentDummy = {
    "Evaluators": [
        {
            "name": "Juan Paco Pedro de la Mar",
            "id": "FFAA21",
            "assignedArticles": ["000001", "000002", "000003"]
        },
        {
            "name": "Albert Einstein Energy",
            "id": "FFAA22",
            "assignedArticles": ["000001", "000002", "000003"]
        },
        {
            "name": "Marie Curie Poland",
            "id": "FFAA23",
            "assignedArticles": ["000001", "000002", "000003"]
        }
    ],
    "Articles": [
        {
            "title": "Effects of sleep deprivation on cognitive performance in college students",
            "id": "FFAA21",
            "assignedEvaluators": ["000001", "000002", "000003"]
        },
        {
            "title": "Effects of increased carbon dioxide on coral reef ecosystems in the Great Barrier Reef",
            "id": "FFAA22",
            "assignedEvaluators": ["000001", "000002", "000003"]
        },
        {
            "title": "Essential Guide to Manuscript Writing for Academic Dummies",
            "id": "FFAA23",
            "assignedEvaluators": ["000001", "000002", "000003"]
        }
    ]
}

# Articles catalog dummy data
articlesAssignmentDummy = [
    {
        "id": "FFAA21",
        "author": "Juan Paco Pedtro de la mar",
        "title": "Effects of sleep deprivation on cognitive performance in college students",
        "category": "Pikachu",
        "evaluationsGrades": ["4", "3", "5"],
        "averageGrade": 4,
        "evaluationStatus": True,
        "emailSent": False,

    },
    {
        "id": "FFAA22",
        "author": "Paul",
        "title": "Effects of increased carbon dioxide on coral reef ecosystems in the Great Barrier Reef",
        "category": "Charmander",
        "evaluationsGrades": ["4", "3", "5"],
        "averageGrade": 4,
        "evaluationStatus": True,
        "emailSent": True,
    },
    {
        "id": "FFAA23",
        "author": "Pedro de la mar",
        "title": "Essential Guide to Manuscript Writing for Academic Dummies",
        "category": "Squartle",
        "evaluationsGrades": ["4", "3", "5"],
        "averageGrade": 4,
        "evaluationStatus": False,
        "emailSent": False,
    }
]

FinalEvaluationDummy = [
    [4, 4, 5, 1, 1],
    [5, 2, 1, 2, 2],
    [3, 1, 5, 4, 5]
]

# ----------------------- Hashing -------------------------
def hash_password_bcrypt(password, salt):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password_bcrypt(entered_password, stored_hash):
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hash)

# ----------------------- Database ------------------------
# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '97cb42K3a8yef!ds)/6#)VQV'
app.config['MYSQL_DB'] = 'flask_db'

# Initialize MySQL
mysql = MySQLdb.connect(host=app.config['MYSQL_HOST'],
                        user=app.config['MYSQL_USER'],
                        passwd=app.config['MYSQL_PASSWORD'],
                        db=app.config['MYSQL_DB'])

cursor = mysql.cursor()

# cursor.execute("SHOW TABLES")
# result = cursor.fetchall()
# print(result)

def db_insert(mysql, insertCmd):
    try:
        cursor.execute(insertCmd)
        mysql.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False

# ----------------------- Flask routes ------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "aabb$12345678":
            cursor.execute(f"SELECT * FROM mucuser WHERE userlogin = '{form.data['email']}'")
            result = cursor.fetchall()

            if result == ():
                pass
            else:
                flash(f"Este usuario no existe. Favor de registrarse", "error")

            print(result)

            # flash(f"Bienvenido", "success")
            print(form.data)
            return redirect(url_for("dashboard", userid=f"{form.email.data}"))
        else:
            print("denied")
            flash(f"Credenciales incorrectas", "error")
    else:
        pass
        # flash(f"Validación NO exitosa", "error")

    return render_template("login.html", form=form)

@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm(titleOptions)
    if form.validate_on_submit():
        cursor.execute(f"SELECT * FROM mucuser WHERE userlogin = '{form.data['email']}'")
        result = cursor.fetchall()

        if result == ():
            userSalt = bcrypt.gensalt()
            userHash = hash_password_bcrypt(form.data['password'], userSalt)

            userSalt_str = userSalt.decode('utf-8')
            userHash_str = userHash.decode('utf-8')

            if db_insert(mysql, f"""
                        INSERT INTO
                            mucuser (userlogin, userhash, usersalt, firstname, lastName, email, title, specialty)
                        SELECT
                            '{form.data['email']}',
                            '{userHash_str}',
                            '{userSalt_str}',
                            '{form.data['name']}',
                            '{form.data['fathersName']} {form.data['mothersName']}',
                            '{form.data['email']}',
                            '{form.data['title']}',
                            '{form.data['specialty']}'
                        FROM
                            DUAL
                        WHERE
                            NOT EXISTS (
                                SELECT
                                    *
                                FROM
                                    mucuser
                                WHERE
                                    userlogin = '{form.data['email']}'
                            )
                    """):
                    flash(f"Registro exitoso", "success")
            else:
                flash(f"Problema para insertar en la base de datos", "error")
        else:
            flash(f"El usuario ingresado ya existe", "error")

        # return redirect(url_for('home'))
        # return redirect(url_for('sign_up'))
    return render_template('sign_up.html', form=form)

'''
@app.route('/<userid>')
def dashboard(userid):
    userDashboard = Dashboard(id)
    return render_template("dashboard.html", dashboard=userDashboard)
    
'''

@app.route('/dashboard')
def dashboard():
    userDashboard = Dashboard(id)
    return render_template("dashboard.html", dashboard=userDashboard)

@app.route("/new_article", methods=["GET", "POST"])
def new_article():
    form = NewArticleForm(categoryOptions)
    if form.validate_on_submit():
        flash(f"Registro exitoso", "success")
        print(form.data)
        # return redirect(url_for('dashboard'))
    return render_template('new_article.html', form=form)

@app.route("/evaluation", methods=["GET", "POST"])
def evaluation():
    form = EvaluationForm(evaluationOptions)
    if form.validate_on_submit():
        flash(f"Evaluación exitosa", "success")
        print(form.data)
        # return redirect(url_for('dashboard'))
    return render_template('evaluation.html', form=form)

@app.route("/articles_assignment", methods=["GET", "POST"])
def articles_assignment():
    if request.method == "POST":
        flash(f"Evaluación exitosa", "success")
        data = request.form
        print(data)
        return render_template('articles_assignment.html', data=articlesAssignmentDummy, categories=articlesAssignmentCategories)
    else:
        return render_template('articles_assignment.html', data=articlesAssignmentDummy, categories=articlesAssignmentCategories)

@app.route("/articles_catalog", methods=["GET", "POST"])
def articles_catalog():
    return render_template('articles_catalog.html', data=articlesAssignmentDummy, categories=articlesAssignmentCategories)

@app.route("/final_evaluation", methods=["GET", "POST"])
def final_evaluation():
    form = FinalEvaluationForm(evaluationOptions)
    if form.validate_on_submit():
        flash(f"Evaluación final exitosa", "success")
        print(form.data)
        # return redirect(url_for('dashboard'))
    return render_template('final_evaluation.html', form=form, criteria=evaluationOptions["Criteria"], partialEvaluation=FinalEvaluationDummy)


if __name__ == '__main__':
    app.run(debug=True)
