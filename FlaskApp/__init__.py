from flask import Flask, render_template
import os

app = Flask(__name__)
app.config.from_mapping(
   SECRET_KEY='dev',
   PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)),
   DATABASE = os.path.join(PROJECT_ROOT, 'tmp', 'test.db')
   )

@app.route('/test')
def test():
   return "I can successfully copy and paste!"

@app.route('/temp')
def temp():
    return "deze pagina werkt"

if __name__ == "__main__":
   app.run()

from . import db
db.init_app(app)

from . import auth
app.register_blueprint(auth.bp)

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/en')
def login_en():
   return render_template('login_en.html')