from flask import render_template
from . import app
from app.db_connect import get_db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/teams-info')
def teams_info():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM teams ORDER BY team_name')
    all_teams = cursor.fetchall()
    return render_template('teams_info.html', all_teams=all_teams)

@app.route('/drivers-info')
def drivers_info():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT d.*, t.team_name
        FROM drivers d
        LEFT JOIN teams t ON d.team_id = t.team_id
        ORDER BY d.last_name
    ''')
    all_drivers = cursor.fetchall()

    cursor.execute('SELECT * FROM teams ORDER BY team_name')
    all_teams = cursor.fetchall()

    return render_template('drivers_info.html', all_drivers=all_drivers, all_teams=all_teams)
