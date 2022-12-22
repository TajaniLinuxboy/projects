from flask import Flask
from flask_bcrypt import Bcrypt
import secrets

app = Flask(__name__)
app.app_context().push()
bcrypt = Bcrypt(app)

secret_key = secrets.token_hex(16)
secret_key_hash = bcrypt.generate_password_hash(secret_key)
app.config['SECRET_KEY'] = secret_key_hash
