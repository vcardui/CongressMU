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
# | Last update..: May 10th, 2025
# | WhatIs.......: NewMU - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Jinja Expressions: https://jinja.palletsprojects.com/en/stable/templates/#jinja-filters.length
# SweetAlert Js with Flask: https://github.com/elijahondiek/SweetAlert-Js-with-Flask

# ------------------------- Libraries -------------------------
from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap5

from form import LogInForm, SignUpForm, NewArticleForm, EvaluationForm
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

# Category Options
evaluationOptions = {
    "Grade": [(1, ' ★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')],
    "Conclusion": [(0, 'Aceptado sin modificaciones'), (1, 'Aceptado con modificaciones básicas'), (2, 'Aceptado con modificaciones básicas y algunas de estructura'), (3, 'Evaluar, reescribir contenidos y presentar a una próxima convocatoria para nueva evaluación'), (4, 'No Aceptado')]
}
# ----------------------- Flask routes ------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "aabb$12345678":
            # flash(f"Bienvenido", "success")
            return redirect(url_for("dashboard", userid=f"{form.email.data}"))
        else:
            print("denied")
            flash(f"Credenciales incorrectas", "error")
    else:
        pass
        # flash(f"Validación NO exitosa", "error")

    return render_template("index.html", form=form)

@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm(titleOptions)
    if form.validate_on_submit():
        flash(f"Registro exitoso", "success")
        print(form.data)
        return redirect(url_for('home'))
    return render_template('sign_up.html', form=form)

@app.route('/<userid>')
def dashboard(userid):
    userDashboard = Dashboard(id)
    return render_template("dashboard.html", dashboard=userDashboard)

@app.route("/new_article", methods=["GET", "POST"])
def new_article():
    form = NewArticleForm(categoryOptions)
    if form.validate_on_submit():
        flash(f"Registro exitoso", "success")
        print(form.data)
        return redirect(url_for('dashboard'))
    return render_template('new_article.html', form=form)

@app.route("/evaluation", methods=["GET", "POST"])
def evaluation():
    form = EvaluationForm(evaluationOptions)
    if form.validate_on_submit():
        flash(f"Evaluación exitosa", "success")
        print(form.data)
        # return redirect(url_for('dashboard'))
    return render_template('evaluation.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
