"""
Quick script to check Lewis Hamilton in database
"""
import os
from dotenv import load_dotenv
import pymysql

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_DATABASE')
}

try:
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Check for Lewis Hamilton
    cursor.execute("SELECT * FROM drivers WHERE first_name = 'Lewis' AND last_name = 'Hamilton'")
    lewis = cursor.fetchone()

    if lewis:
        print("Lewis Hamilton found in database:")
        print(f"  ID: {lewis['driver_id']}")
        print(f"  Team ID: {lewis['team_id']}")
        print(f"  Number: {lewis['driver_number']}")
        print(f"  Photo: {lewis['photo_url']}")
    else:
        print("Lewis Hamilton NOT found in database")

    # Check total drivers
    cursor.execute("SELECT COUNT(*) as count FROM drivers")
    total = cursor.fetchone()
    print(f"\nTotal drivers in database: {total['count']}")

    # List all drivers
    cursor.execute("SELECT first_name, last_name, driver_number FROM drivers ORDER BY last_name")
    all_drivers = cursor.fetchall()
    print("\nAll drivers:")
    for d in all_drivers:
        print(f"  - {d['first_name']} {d['last_name']} (#{d['driver_number']})")

    cursor.close()
    connection.close()

except Exception as e:
    print(f"Error: {e}")
