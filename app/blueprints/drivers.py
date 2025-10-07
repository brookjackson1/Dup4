from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

drivers = Blueprint('drivers', __name__)

@drivers.route('/', methods=['GET', 'POST'])
def show_drivers():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new driver
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        team_id = request.form['team_id']
        nationality = request.form['nationality']
        driver_number = request.form['driver_number']
        date_of_birth = request.form['date_of_birth']

        # Insert the new driver into the database
        cursor.execute('INSERT INTO drivers (first_name, last_name, team_id, nationality, driver_number, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s)',
                       (first_name, last_name, team_id, nationality, driver_number, date_of_birth))
        db.commit()

        flash('New driver added successfully!', 'success')
        return redirect(url_for('drivers.show_drivers'))

    # Handle GET request to display all drivers with their teams
    cursor.execute('''
        SELECT d.*, t.team_name
        FROM drivers d
        LEFT JOIN teams t ON d.team_id = t.team_id
        ORDER BY d.last_name
    ''')
    all_drivers = cursor.fetchall()

    # Get all teams for the dropdown
    cursor.execute('SELECT team_id, team_name FROM teams ORDER BY team_name')
    all_teams = cursor.fetchall()

    return render_template('drivers.html', all_drivers=all_drivers, all_teams=all_teams)

@drivers.route('/update_driver/<int:driver_id>', methods=['POST'])
def update_driver(driver_id):
    db = get_db()
    cursor = db.cursor()

    # Update the driver's details
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    team_id = request.form['team_id']
    nationality = request.form['nationality']
    driver_number = request.form['driver_number']
    date_of_birth = request.form['date_of_birth']

    cursor.execute('UPDATE drivers SET first_name = %s, last_name = %s, team_id = %s, nationality = %s, driver_number = %s, date_of_birth = %s WHERE driver_id = %s',
                   (first_name, last_name, team_id, nationality, driver_number, date_of_birth, driver_id))
    db.commit()

    flash('Driver updated successfully!', 'success')
    return redirect(url_for('drivers.show_drivers'))

@drivers.route('/delete_driver/<int:driver_id>', methods=['POST'])
def delete_driver(driver_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the driver
    cursor.execute('DELETE FROM drivers WHERE driver_id = %s', (driver_id,))
    db.commit()

    flash('Driver deleted successfully!', 'danger')
    return redirect(url_for('drivers.show_drivers'))
