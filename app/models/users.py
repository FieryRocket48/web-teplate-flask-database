import uuid
from flask_login import UserMixin
from ..extensions import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    login = db.Column(db.String(20))
    password = db.Column(db.String(150))
    group = db.Column(db.String(30))
    status = db.Column(db.Boolean, default=True)
    guid = db.Column(db.String, unique=True, default=lambda: str(uuid.uuid4()))

