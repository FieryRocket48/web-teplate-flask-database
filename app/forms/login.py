from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length, EqualTo, ValidationError
from ..models.users import Users

class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить')
    submit = SubmitField('Войти')
    def validate_login(self, login):
        user = Users.query.filter_by(login=login.data).first()
        if user.status is False:
            raise ValidationError('Пользователь заблокирован')

class CreateUser(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=4,)])
    login = StringField('Login', validators=[DataRequired(),Length(min=4,)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,)])
    confirm_password = PasswordField('Confirm ', validators=[DataRequired(), EqualTo('password')])
    group = SelectField('Groups', validators=[DataRequired()],
                        choices=[ ('user', 'Пользователь'),('admin', 'Администратор')])
    submit = SubmitField('Create')


    def validate_login(self, login):
        user = Users.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Имя пользователя уже занято')


class UpdateUser(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=4,)])
    login = StringField('Login', validators=[DataRequired(),Length(min=4,)])
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm ', validators=[ EqualTo('password')])
    group = SelectField('Groups', validators=[DataRequired()],
                        choices=[ ('user', 'Пользователь'),('admin', 'Администратор')])
    status = BooleanField('Active user')
    update = SubmitField('Save')
