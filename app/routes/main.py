from click import group
from flask import Blueprint, render_template, send_from_directory, request, redirect, flash, url_for, abort
from flask_login import logout_user, login_user, login_required, current_user

from ..extensions import bcrypt, db
from ..forms.login import LoginForm, CreateUser, UpdateUser
from ..models.users import Users

main = Blueprint('main', __name__)


@main.route('/favicon.ico')
def favicon():
    return send_from_directory('static/img', 'favicon.ico')



@main.route('/', methods=['GET', 'POST'])
@main.route('/index')
@login_required
def index():
    return render_template('main/index.html')


@main.route('/configure', methods=['GET', 'POST'])
def configure():
    form = CreateUser()
    form.group.choices = [('admin', 'administrator')]
    admin = Users.query.filter_by(login='admin').first()

    if admin is None:
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user= Users(
                name=form.name.data,
                login=form.login.data,
                password=hashed_password,
                group=form.group.data,
            )
            try:
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                print(str(e))
            logout_user()
            flash(f'Пользователь {form.name.data} успешно создан', "success")
            return redirect(url_for('main.index'))
        else:
            for item, error in form.errors.items():
                if item == 'confirm_password':
                    flash(f'Введённые пароли не совпадают!', "danger")
                elif item == 'login':
                    pass
                else:
                    flash(f'Возникла ошибка{item, error}!', "danger")
            print(form.errors)
            return render_template('main/configure.html', form=form)
    else:
        flash(f'The configuration has been completed', "success")
        return redirect(url_for('main.index'))
    return render_template('main/configure.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(login=form.login.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.index'))
            else:
                flash(f'неверный логин или пароль.', 'danger')
        else:
            flash(f'При входе возникла ошибка, {form.errors}!', "danger")
    return render_template('users/login.html', form=form)


@main.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    if current_user.group =="admin":
        users = Users.query.all()
        form = CreateUser()
        if request.method == 'POST':
            if form.validate_on_submit():
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = Users(
                    name=form.name.data,
                    login=form.login.data,
                    password=hashed_password,
                    group=form.group.data,
                )
                db.session.add(user)
                db.session.commit()
                flash(f'Пользователь {form.name.data} успешно создан', "success")
                return redirect(url_for('main.users'))
            else:
                for item, error in form.errors.items():
                    if item == 'confirm_password':
                        flash(f'Введённые пароли не совпадают!', "danger")
                    else:
                        flash(f'Возникла ошибка{item, error}!', "danger")

        return render_template('users/users.html', users=users, form=form)
    else:
        abort(403)
@main.route('/users/edit/<guid>', methods=['GET', 'POST'])
@login_required
def edit_user(guid):
    if current_user.group == "admin":
        user = Users.query.filter_by(guid=guid).first()
        form = UpdateUser()
        form.name.data = user.name
        form.login.data = user.login
        form.group.data = user.group
        form.status.data = user.status
        print(type(user.status), user.status)
        if request.method == 'POST':

            if form.validate_on_submit():
                password = request.form.get('password')
                if password is not '':
                    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                    user.password = hashed_password

                    if len(password) < 8:
                        flash(f'Пароль менее 8 символов!', "danger")
                        return render_template('users/edit.html',  form=form, login=user.login)

                user.name = request.form.get('name')
                user.group = request.form.get('group')
                user.status = True if request.form.get('status') else False
                try:
                    db.session.commit()
                except Exception as e:
                    print(str(e))
                flash(f'Данные пользователя {form.name.data} успешно обновлены', "success")
                return redirect(url_for('main.users'))
            else:
                for item, error in form.errors.items():
                    if item == 'confirm_password':
                        flash(f'Введённые пароли не совпадают!', "danger")
                    else:
                        flash(f'Возникла ошибка{item, error}!', "danger")
        return render_template('users/edit.html',  form=form, login=user.login, group=user.group)
    else:
        abort(403)