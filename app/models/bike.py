from app.extensions import db

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), unique=True, nullable=False)
    model = db.Column(db.Integer, default=0, nullable=False)
    wheel = db.Column(db.Integer, default=0, nullable=False)
    iron = db.Column(db.Integer, default=0, nullable=False)
    color = db.Column(db.Text, nullable=False)
    
    owner = db.Column(db.Integer, db.ForeignKey('client.id', ondelete='CASCADE'), nullable=False)
    
    def __repr__(self):
        return f'<Bike {self.id}>, Owner {self.owner}'