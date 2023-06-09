from app.extensions import db

class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(180), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hint = db.Column(db.String(100))
    photo = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')

    def __repr__(self):
        return f'<Auth {self.username}>'
