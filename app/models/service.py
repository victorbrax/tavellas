from app.extensions import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Numeric(10,2))
    
    id_bike = db.Column(db.Integer, db.ForeignKey('bike.id', ondelete='CASCADE'))
    id_repair = db.Column(db.Integer, db.ForeignKey('repair.id', ondelete='CASCADE'))
    
    def __repr__(self):
        return f'<Service {self.id}, {self.name}, Bike {self.id_bike}>'