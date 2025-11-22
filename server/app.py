# server/app.py
from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db.init_app(app)

@app.route('/')
def index():
    return ''

if __name__ == '__main__':
    app.run(port=5555, debug=True)