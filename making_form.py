from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length


class CreterionForm(FlaskForm):
    min_carbs = TextAreaField('Минимальные углеводы', validators=[DataRequired()])
    max_carbs = TextAreaField('Максимальные углеводы', validators=[DataRequired()])
    min_protein = TextAreaField('Минимальные белки', validators=[DataRequired()])
    max_protein = TextAreaField('Максимальные белки', validators=[DataRequired()])
    min_calories = TextAreaField("Минимальные калории", validators=[DataRequired()])
    max_calories = TextAreaField('Максимальные калории', validators=[DataRequired()])
    min_fat = TextAreaField("Минимальные жиры", validators=[DataRequired()])
    max_fat = TextAreaField("Максимальные жиры", validators=[DataRequired()])
    submit = SubmitField('Готово')
