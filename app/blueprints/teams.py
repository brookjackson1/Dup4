from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

teams = Blueprint('teams', __name__)

@teams.route('/', methods=['GET', 'POST'])
def show_teams():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new team
    if request.method == 'POST':
        team_name = request.form['team_name']
        country = request.form['country']
        team_principal = request.form['team_principal']

        # Insert the new team into the database
        cursor.execute('INSERT INTO teams (team_name, country, team_principal) VALUES (%s, %s, %s)',
                       (team_name, country, team_principal))
        db.commit()

        flash('New team added successfully!', 'success')
        return redirect(url_for('teams.show_teams'))

    # Handle GET request to display all teams
    cursor.execute('SELECT * FROM teams')
    all_teams = cursor.fetchall()
    return render_template('teams.html', all_teams=all_teams)

@teams.route('/update_team/<int:team_id>', methods=['POST'])
def update_team(team_id):
    db = get_db()
    cursor = db.cursor()

    # Update the team's details
    team_name = request.form['team_name']
    country = request.form['country']
    team_principal = request.form['team_principal']

    cursor.execute('UPDATE teams SET team_name = %s, country = %s, team_principal = %s WHERE team_id = %s',
                   (team_name, country, team_principal, team_id))
    db.commit()

    flash('Team updated successfully!', 'success')
    return redirect(url_for('teams.show_teams'))

@teams.route('/delete_team/<int:team_id>', methods=['POST'])
def delete_team(team_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the team (will cascade delete drivers)
    cursor.execute('DELETE FROM teams WHERE team_id = %s', (team_id,))
    db.commit()

    flash('Team deleted successfully!', 'danger')
    return redirect(url_for('teams.show_teams'))
