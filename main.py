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
# | Last update..: May 22th, 2025
# | WhatIs.......: CongressMU - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Jinja Expressions: https://jinja.palletsprojects.com/en/stable/templates/#jinja-filters.length
# SweetAlert Js with Flask: https://github.com/elijahondiek/SweetAlert-Js-with-Flask

# How to use Flask-Session in Python Flask: https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/

# ------------------------- Libraries -------------------------
# Flask imports
from flask import Flask, render_template, flash, redirect, url_for, request, session, jsonify
from flask_bootstrap import Bootstrap5
from flask_session import Session

# Hashing
import bcrypt

# Cardui classes
from form import LogInForm, SignUpForm, NewArticleForm, EvaluationForm, FinalEvaluationForm
from dashboard import Dashboard

# Database
import database

# ------------------------- App configuration -------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# ----------------------- db ------------------------
db = database.MariaDB()

# ----------------------- Flask sessions ------------------------

app.config["SESSION_PERMANENT"] = False       # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files

# Start Flask-Session
Session(app)

# ------------------------- Variables -------------------------
# Title Options
titleOptions = {
    "Title": [(0, ''), (1, 'Lic.'), (2, 'Ing.'), (3, 'Mtr.'), (4, 'Phd.')]
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


# ----------------------- Flask routes ------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        result = db.select(f"SELECT * FROM mucuser WHERE userlogin = '{form.data['email']}'")
        
        # print(f"This is the result: {result}")

        if result == ():
            flash(f"Este usuario no existe. Favor de registrarse", "error")
        else:
            user_key = db.select(f"SELECT userhash FROM mucuser WHERE userlogin = '{form.data['email']}'")
            user_hash = user_key[0][0].encode(encoding="utf-8")

            if verify_password_bcrypt(form.data['password'], user_hash):
                flash(f"Bienvenido", "success")

                user_session = request.cookies.get('session')

                if not db.insert(f"""
                INSERT INTO
                    musession (idmucuser, sessionnumber)
                SELECT
                    idmucuser,
                    '{user_session}'
                FROM
                    mucuser
                WHERE
                    userlogin = '{form.data['email']}'
                    AND NOT EXISTS (
                        SELECT
                            *
                        FROM
                            musession
                        WHERE
                            sessionnumber = '{user_session}'
                    )
                """):
                    flash(f"Error al crear sesión", "error")

                return redirect(url_for("dashboard"))
            else:
                flash(f"Credenciales incorrectas", "error")
    else:
        pass
        # flash(f"Validación NO exitosa", "error")

    return render_template("login.html", form=form)

@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm(titleOptions)
    if form.validate_on_submit():
        result = db.select(f"SELECT * FROM mucuser WHERE userlogin = '{form.data['email']}'")

        print(f"titleOptions['Title'][int(form.data['title'])]: {titleOptions['Title'][int(form.data['title'])]}")

        if result == ():
            user_salt = bcrypt.gensalt()
            user_hash = hash_password_bcrypt(form.data['password'], user_salt)
            user_hash_str = user_hash.decode('utf-8')

            if db.insert(f"""
                        INSERT INTO
                            mucuser (userkind, userlogin, userhash, firstname, lastName, email, title, specialty)
                        SELECT
                            'Author',
                            '{form.data['email']}',
                            '{user_hash_str}',
                            '{form.data['name']}',
                            '{form.data['fathersName']} {form.data['mothersName']}',
                            '{form.data['email']}',
                            '{titleOptions['Title'][int(form.data['title'])][1]}',
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
                    return redirect(url_for('login'))
            else:
                flash(f"Problema para insertar en la base de datos", "error")
        else:
            flash(f"El usuario ingresado ya existe", "error")

        # return redirect(url_for('home'))
        # return redirect(url_for('sign_up'))
    return render_template('sign_up.html', form=form)

@app.route('/dashboard')
def dashboard():
    user_dashboard = Dashboard(request.cookies.get('session'))
    return render_template("dashboard.html", dashboard=user_dashboard)

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
