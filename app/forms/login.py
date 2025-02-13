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
    name = StringField('Имя', validators=[DataRequired(),Length(min=4,)])
    login = StringField('Логин', validators=[DataRequired(),Length(min=4,)])
    password = PasswordField('Пароль', validators=[DataRequired(),Length(min=8,)])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
    group = SelectField('Группа доступа', validators=[DataRequired()],
                        choices=[ ('user', 'Пользователь'),('admin', 'Администратор')])
    submit = SubmitField('Создать')


    def validate_login(self, login):
        user = Users.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Имя пользователя уже занято')


class UpdateUser(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(),Length(min=4,)])
    login = StringField('Логин', validators=[DataRequired(),Length(min=4,)])
    password = PasswordField('Пароль')
    confirm_password = PasswordField('Подтверждение пароля ', validators=[ EqualTo('password')])
    group = SelectField('Группа доступа', validators=[DataRequired()],
                        choices=[ ('user', 'Пользователь'),('admin', 'Администратор')])
    status = BooleanField('Активный')
    update = SubmitField('Сохранить')
