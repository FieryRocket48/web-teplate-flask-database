from ..extensions import db

class RegionObject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    share_folder = db.Column(db.String(30), nullable=False)
    date_checked = db.Column(db.DateTime, nullable=False)
    responsible = db.Column(db.String(30))
    test =  db.Column(db.String(30))




