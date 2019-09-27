#first install pip install manager  and SQLalchemy stuff
#conda install-c conda-forge flask-sqlalchemy
from flask_sqlalchemy import QSLAlchemy
from app import app

app.config['SQLALCHEmy_DATABASE']='sqlite:////temp.db'
db =SQLAlchemy(app)
class Alcohol(db.Model):
    __tablename__ = "alcohol"

    id= do.Column(db.Integer, autoincrement=True, primary_key=True)
    pic = db.Column(db.String)
    name = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Alcohol:{self.name}>'