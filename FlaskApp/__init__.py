from flask import Flask, render_template
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
   SECRET_KEY='dev',
   DATABASE=os.path.join(app.instance_path, 'db', 'db.sqlite'),
   )
print(os.path.join(app.instance_path, 'db', 'db.sqlite'))
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