from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DbBaseModel(db.Model):
    __abstract__ = True
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class text_document(DbBaseModel):
    id = db.Column("text_id", db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    text = db.Column(db.Text)

