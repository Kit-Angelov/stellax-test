from flask import Flask

from views import api
from models import db, bcrypt

app = Flask(__name__)
app.register_blueprint(api)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    bcrypt.init_app(app)
    app.run(debug = True)