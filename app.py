from flask import Flask, render_template, jsonify
from models import db, MediaItem
import os

app = Flask(__name__)

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'xndrsound.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize DB
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html') # Minimal Splash Page

@app.route('/staging')
def staging():
    return render_template('staging.html') # Full Dev Site




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
