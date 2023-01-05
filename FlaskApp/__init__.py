from flask import Flask
app = Flask(__name__)

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

