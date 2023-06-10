from app.extensions import db

class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Numeric(10,2))
    
    def __repr__(self):
        return f'<Repair {self.id}, Name {self.name}>'