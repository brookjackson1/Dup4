"""
Script to add missing drivers: Lewis Hamilton and Charles Leclerc
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

    # Get Ferrari team ID
    cursor.execute("SELECT team_id FROM teams WHERE team_name = 'Ferrari'")
    ferrari = cursor.fetchone()
    ferrari_id = ferrari['team_id'] if ferrari else 1

    print(f"Ferrari team ID: {ferrari_id}")

    # Check if Lewis Hamilton exists
    cursor.execute("SELECT driver_id FROM drivers WHERE first_name = 'Lewis' AND last_name = 'Hamilton'")
    lewis_exists = cursor.fetchone()

    if not lewis_exists:
        print("Adding Lewis Hamilton...")
        cursor.execute("""
            INSERT INTO drivers (first_name, last_name, team_id, nationality, driver_number, date_of_birth, photo_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            'Lewis',
            'Hamilton',
            ferrari_id,
            'British',
            44,
            '1985-01-07',
            'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/ferrari/lewham01/2025ferrarilewham01right.webp'
        ))
        print("✓ Lewis Hamilton added!")
    else:
        print("Lewis Hamilton already exists")

    # Check if Charles Leclerc exists
    cursor.execute("SELECT driver_id FROM drivers WHERE first_name = 'Charles' AND last_name = 'Leclerc'")
    charles_exists = cursor.fetchone()

    if not charles_exists:
        print("Adding Charles Leclerc...")
        cursor.execute("""
            INSERT INTO drivers (first_name, last_name, team_id, nationality, driver_number, date_of_birth, photo_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            'Charles',
            'Leclerc',
            ferrari_id,
            'Monegasque',
            16,
            '1997-10-16',
            'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/ferrari/chalec01/2025ferrarichalec01right.webp'
        ))
        print("✓ Charles Leclerc added!")
    else:
        print("Charles Leclerc already exists")

    connection.commit()

    # Verify
    cursor.execute("SELECT COUNT(*) as count FROM drivers")
    total = cursor.fetchone()
    print(f"\nTotal drivers now: {total['count']}")

    cursor.execute("SELECT first_name, last_name, driver_number, team_id FROM drivers WHERE team_id = %s ORDER BY last_name", (ferrari_id,))
    ferrari_drivers = cursor.fetchall()
    print("\nFerrari drivers:")
    for d in ferrari_drivers:
        print(f"  - {d['first_name']} {d['last_name']} (#{d['driver_number']})")

    cursor.close()
    connection.close()

    print("\n[OK] Missing drivers added successfully!")

except Exception as e:
    print(f"Error: {e}")
    raise
