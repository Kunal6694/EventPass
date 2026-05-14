from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'prakrit_style_key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# --- LANDING & MARKETPLACE ---
@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/marketplace')
def index():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    return render_template('index.html', events=events)


# --- AUTHENTICATION ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username, role = request.form['username'], request.form['role']
        password = generate_password_hash(request.form['password'])
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
            conn.commit()
            flash('Account created! Please login.', 'success')
            return redirect(url_for('login'))
        except:
            flash('Username already exists', 'danger')
        finally:
            conn.close()
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'], session['username'], session['role'] = user['id'], user['username'], user['role']
            return redirect(url_for('organizer' if user['role'] == 'Organizer' else 'index'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing'))


# --- USER FEATURES ---
@app.route('/my_bookings')
def my_bookings():
    if not session.get('user_id'): return redirect(url_for('login'))
    conn = get_db_connection()
    query = """
            SELECT b.*, e.title, e.date, e.location
            FROM bookings b
                     JOIN events e ON b.event_id = e.id
            WHERE b.user_id = ? \
            """
    history = conn.execute(query, (session['user_id'],)).fetchall()
    conn.close()
    return render_template('my_bookings.html', bookings=history)


@app.route('/book/<int:event_id>', methods=('GET', 'POST'))
def book(event_id):
    if not session.get('user_id'):
        flash('Please login to book tickets', 'info')
        return redirect(url_for('login'))

    conn = get_db_connection()
    event = conn.execute('SELECT * FROM events WHERE id = ?', (event_id,)).fetchone()

    if request.method == 'POST':
        name, email, tickets = request.form['full_name'], request.form['email'], int(request.form['tickets'])
        if tickets <= event['available_seats']:
            conn.execute('UPDATE events SET available_seats = ? WHERE id = ?',
                         (event['available_seats'] - tickets, event_id))
            conn.execute(
                'INSERT INTO bookings (user_id, event_id, customer_name, customer_email, tickets) VALUES (?,?,?,?,?)',
                (session['user_id'], event_id, name, email, tickets))
            conn.commit()
            conn.close()
            flash(f'Confirmed! Tickets for {event["title"]} sent to {email}', 'success')
            return redirect(url_for('index'))
    conn.close()
    return render_template('booking.html', event=event)


# --- ORGANIZER FEATURES ---
@app.route('/organizer', methods=['GET', 'POST'])
def organizer():
    if session.get('role') != 'Organizer': return redirect(url_for('index'))
    conn = get_db_connection()
    if request.method == 'POST':
        conn.execute(
            'INSERT INTO events (title, date, location, description, available_seats, price) VALUES (?,?,?,?,?,?)',
            (request.form['title'], request.form['date'], request.form['location'],
             request.form['desc'], request.form['seats'], request.form['price']))
        conn.commit()
        flash('Event published successfully!', 'success')
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    return render_template('organizer.html', events=events)


if __name__ == '__main__':
    app.run(debug=True)