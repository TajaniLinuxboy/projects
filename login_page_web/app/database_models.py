from app import db, login_manager
from flask_login import UserMixin
from itsdangerous.serializer import Serializer

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    #authentication (possible) we'll see
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True, unique=True)
    password = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(75), nullable=True, unique=True)
    stored_link = db.relationship('StoreLinks', backref="users", lazy=True)


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def __repr__(self):
        return f"Users({self.id}/{self.username}/{self.email})"



class StoreLinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(50), nullable=True)
    link_title = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
