import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from FlaskApp.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        flight_no = request.form['flight_no']
        seat_no = request.form['seat_no']
        db = get_db()
        error = None
        flight = db.execute(
            'SELECT * FROM Wifi_Registration WHERE Ticket_Nummer = ?', (flight_no,)
        ).fetchone()

        if flight_no is None:
            error = 'Incorrect ticket number.'
        elif seat_no != flight['Seat_Nummer']:
            error = 'Incorrect seat number.'
        elif seat_no is None: 
            error = 'Ticket is required.'

        if error is None:
            session.clear()
            session['user_id'] = flight['id']
            return redirect(url_for('index'))

        flash(error)
    return render_template('/templates/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
