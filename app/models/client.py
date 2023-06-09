from app.extensions import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cellphone = db.Column(db.String(20))
    telephone = db.Column(db.String(20))
    cep = db.Column(db.String(10))
    street = db.Column(db.String(100))
    number = db.Column(db.String(10))
    complement = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))

    def __repr__(self):
        return f'<Client {self.name}>'
