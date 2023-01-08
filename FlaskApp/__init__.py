from flask import (
   Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import os
import sqlite3 as sql

app = Flask(__name__, instance_relative_config=True)
# print(os.path.join('/var/www/corendon_raspi/FlaskApp/db', 'db.sqlite'))
app.config.from_mapping(
   SECRET_KEY='dev',
   DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
   )

# ensure the instance folder exists
try:
   os.makedirs(app.instance_path)
except OSError:
   pass

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
from FlaskApp.db import get_db

from . import auth
app.register_blueprint(auth.bp)

@app.route('/')
def main():
   return render_template('login.html')

@app.route('/en')
def login_en():
   return render_template('login_en.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
   if request.method == 'POST':
      flight_no = request.form['flight_no']
      seat_no = request.form['seat_no']
      db = get_db()
      error = None
      flight = db.execute(
         'SELECT * FROM Wifi_Registration WHERE Ticket_Nummer = ?', (flight_no)
      ).fetchone()

      if flight_no is None:
         error = 'Incorrect ticket number.'
      # elif seat_no != flight['Seat_Nummer']:
      #    error = 'seat number not correct'
      elif seat_no is None: 
         error = 'Ticket is required.'

      if error is None:
         # session.clear()
         # session['user_id'] = flight['id']
         # return redirect(url_for('index'))
         return "logged in successfully" 

      flash(error)
      return render_template('login.html')
   return render_template('login.html')

