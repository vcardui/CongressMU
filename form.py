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
# | Last update..: May 27th, 2025
# | WhatIs.......: form - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Flask-WTF Basic fields: https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields
# Flask-WTF Validators: https://wtforms.readthedocs.io/en/3.0.x/validators/#module-wtforms.validators
# Dynamic Forms with Flask: https://blog.miguelgrinberg.com/post/dynamic-forms-with-flask

# Flaskform class pass arguments for constructor:
# Struggling to understand FlaskForm with concurrent use of a constructor with super() function: https://www.reddit.com/r/flask/comments/pag4yl/struggling_to_understand_flaskform_with/
# (It inheritances)
# What Does Super().__Init__(*Args, **Kwargs) Do in Python?: https://www.geeksforgeeks.org/what-does-super-__init__args-kwargs-do-in-python/

# ------------------------- Libraries -------------------------
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, FileField, TextAreaField
from wtforms.validators import Length, InputRequired, Email, Regexp, EqualTo

from flask_wtf.file import FileField, FileAllowed, FileRequired

# ------------------------- Classes -------------------------
# pip install email_validator
class LogInForm(FlaskForm):
    email = StringField("Email", [
        Length(min=6, max=25),
        InputRequired("Ingrese su usuario"),
        Email(
            message="Este campo requiere una dirección de correo electrónico válida",
            granular_message=True,
            check_deliverability=True,
            allow_smtputf8=False
        )
    ])

    password = PasswordField('Password', [
        InputRequired("Ingrese su contraseña")
    ])
    submit = SubmitField(label="Log In")

class SignUpForm(FlaskForm):
    name = StringField('Nombre', [
        Length(min=2, max=64, message="Su nombre debe contener entre 2 y 64 caracteres"),
        InputRequired("Ingrese su(s) nombre(s)"),
        Regexp(
            regex="^[A-Za-z áéíóúüñÁÉÍÓÚÜÑàâäæçèéêëîïôœùûüÿÀÂÆÇÈÉÊËÎÏÔŒÙÛÜŸß .&'@#-]+$",
            message="Eliminar cualquier caracter que no sea alfabético o emoji"
        )
    ])

    fathersName = StringField("Apellido paterno", [
        Length(min=2, max=64, message="Su apellido debe contener entre 2 y 64 caracteres"),
        InputRequired("Ingrese su apellido paterno"),
        Regexp(
            regex="^[A-Za-z áéíóúüñÁÉÍÓÚÜÑàâäæçèéêëîïôœùûüÿÀÂÆÇÈÉÊËÎÏÔŒÙÛÜŸß .&'@#-]+$",
            message="Eliminar cualquier caracter que no sea alfabético o emoji"
        )
    ])

    mothersName = StringField("Apellido materno", [
        Length(min=2, max=64, message="Su apellido debe contener entre 2 y 64 caracteres"),
        InputRequired("Ingrese su apellido materno"),
        Regexp(
            regex="^[A-Za-z áéíóúüñÁÉÍÓÚÜÑàâäæçèéêëîïôœùûüÿÀÂÆÇÈÉÊËÎÏÔŒÙÛÜŸß .&'@#-]+$",
            message="Eliminar cualquier caracter que no sea alfabético o emoji"
        )
    ])

    email = StringField("Correo electónico", [
        Length(min=6, max=128, message="Su correo debe contener entre 6 y 128 caracteres"),
        InputRequired("Ingrese su correo electrónico"),
        Email(
            message="Este campo requiere una dirección de correo electrónico válida",
            granular_message=True,
            check_deliverability=True,
            allow_smtputf8=False
        )
    ])

    password = StringField('Contraseña', [
        InputRequired("Please enter your password"),
        Regexp(
            regex="^(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$",
            message="La contraseña debe contener: caracteres alfanuméricos, al menos un caracter especial y tener entre 8 y 16 caracteres de longitud."
        ),
        EqualTo('passwordConfirmation', message='Las contraseñas no coinciden')
    ])

    passwordConfirmation = StringField('Confirmación de contraseña')

    title = SelectField('Título', coerce=str)

    specialty = StringField('Especialidad', [
        Length(min=6, max=64, message="Su especialidad debe contener entre 6 y 64 caracteres"),
        InputRequired("Ingrese su campo de estudio principal"),
        Regexp(
            regex="^[A-Za-z0-9 áéíóúüñÁÉÍÓÚÜÑàâäæçèéêëîïôœùûüÿÀÂÆÇÈÉÊËÎÏÔŒÙÛÜŸß .&'@#-]+$",
            message="Eliminar cualquier caracter que no sea alfabético o emoji"
        )
    ])

    submit = SubmitField(label="Registrarse")

    def __init__(self, options: dict = None, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.title.choices = options["Title"]


class NewArticleForm(FlaskForm):
    title = StringField('Título del artículo', [
        Length(min=6, max=128, message="El título debe contener entre 12 y 128 caracteres"),
        InputRequired("Ingrese el título del artículo"),
        Regexp(
            regex="^[A-Za-z0-9 áéíóúüñÁÉÍÓÚÜÑàâäæçèéêëîïôœùûüÿÀÂÆÇÈÉÊËÎÏÔŒÙÛÜŸß .&'@#-]+$",
            message="Eliminar cualquier caracter que no sea alfabético o emoji"
        )
    ])

    category = SelectField('Categoría', coerce=str)

    # https://wtforms.readthedocs.io/en/3.0.x/fields/#wtforms.fields.FileField
    pdf_file = FileField('Artículo en formato pdf', validators=[
        FileRequired(),
        # FileAllowed('pdf', 'Cargue únicamente archivos PDF')
    ])

    comments = TextAreaField("Comentarios", [
        Length(min=0, max=128, message="El comentario debe contener máximo 128 caracteres"),
    ])

    submit = SubmitField(label="Mandar solicitud")

    def __init__(self, options: dict = None, *args, **kwargs):
        super(NewArticleForm, self).__init__(*args, **kwargs)
        self.category.choices = options["Category"]


class EvaluationForm(FlaskForm):
    criterion1 = SelectField('', coerce=str)
    criterion2 = SelectField('', coerce=str)
    criterion3 = SelectField('', coerce=str)
    criterion4 = SelectField('', coerce=str)
    criterion5 = SelectField('', coerce=str)

    evaluation = SelectField('Categoría', coerce=str)

    comments = TextAreaField("Comentarios", [
        Length(min=0, max=128, message="El comentario debe contener máximo 128 caracteres"),
    ])

    submit = SubmitField(label="Guardar evaluación")

    def __init__(self, options: dict = None, *args, **kwargs):
        super(EvaluationForm, self).__init__(*args, **kwargs)

        self.criterion1.choices = options["Grade"]
        self.criterion1.label.text = options["Criteria"][0][1]

        self.criterion2.choices = options["Grade"]
        self.criterion3.label.text = options["Criteria"][0][1]

        self.criterion3.choices = options["Grade"]
        self.criterion3.label.text = options["Criteria"][0][1]

        self.criterion4.choices = options["Grade"]
        self.criterion4.label.text = options["Criteria"][0][1]

        self.criterion5.choices = options["Grade"]
        self.criterion5.label.text = options["Criteria"][0][1]

        self.evaluation.choices = options["Conclusion"]

class FinalEvaluationForm(FlaskForm):
    finalEvaluation = SelectField('Estatus de evaluación', coerce=str)

    comments = TextAreaField("Comentarios", [
        Length(min=0, max=128, message="El comentario debe contener máximo 128 caracteres"),
    ])

    submit = SubmitField(label="Guardar evaluación")

    def __init__(self, options: dict = None, *args, **kwargs):
        super(FinalEvaluationForm, self).__init__(*args, **kwargs)
        self.finalEvaluation.choices = options["Conclusion"]