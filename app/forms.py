from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, DateTimeField, DecimalField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp


class ScheduleForm(FlaskForm):
    flight_number = DecimalField('Email', validators=[DataRequired(message='Це поле обовязкове')])
    departure_time = StringField('Depart time', validators=[DataRequired(message='Це поле обовязкове')])
    days_week = StringField('Days', validators=[DataRequired(message='Це поле обовязкове')])
    number_seats = DecimalField('Number seats', validators=[DataRequired(message='Це поле обовязкове')])
    route = StringField('Email', validators=[DataRequired(message='Це поле обовязкове')])
    submit = SubmitField('Add')
