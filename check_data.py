"""
Script to verify database data
"""
import os
from dotenv import load_dotenv
import pymysql

# Load environment variables
load_dotenv()

# Database connection parameters
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_DATABASE')
}

def main():
    try:
        # Connect to database
        print(f"Connecting to database at {db_config['host']}...\n")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # Check teams
        print("=== TEAMS DATA ===")
        cursor.execute("SELECT team_id, team_name, team_color, team_logo, secondary_color, car_image FROM teams ORDER BY team_name")
        teams = cursor.fetchall()
        print(f"Total teams: {len(teams)}\n")

        for team in teams:
            print(f"Team: {team['team_name']}")
            print(f"  Color: {team['team_color']}")
            print(f"  Secondary: {team['secondary_color']}")
            print(f"  Logo: {team['team_logo'][:50] + '...' if team['team_logo'] else 'NULL'}")
            print(f"  Car: {team['car_image'][:50] + '...' if team['car_image'] else 'NULL'}")
            print()

        # Check drivers
        print("\n=== DRIVERS DATA ===")
        cursor.execute("""
            SELECT d.driver_id, d.first_name, d.last_name, d.driver_number,
                   d.photo_url, t.team_name
            FROM drivers d
            LEFT JOIN teams t ON d.team_id = t.team_id
            ORDER BY d.last_name
        """)
        drivers = cursor.fetchall()
        print(f"Total drivers: {len(drivers)}\n")

        for driver in drivers:
            print(f"Driver: {driver['first_name']} {driver['last_name']} (#{driver['driver_number']})")
            print(f"  Team: {driver['team_name']}")
            print(f"  Photo: {driver['photo_url'][:50] + '...' if driver['photo_url'] else 'NULL'}")
            print()

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
