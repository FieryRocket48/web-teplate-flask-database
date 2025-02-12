# from ..extensions import db
#
#
# class File(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(60), unique=True, nullable=False)
#     date = db.Column(db.DateTime, nullable=False)
#     size = db.Column(db.String(20), nullable=False)
#     # object_id = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)
#     object_id = db.Column(db.Integer, db.ForeignKey('region_object.id'), nullable=False)
#
#     region_object = db.relationship('RegionObject', backref='files', lazy=True)