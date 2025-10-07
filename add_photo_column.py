"""
Script to add photo_url column to drivers table
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
        print(f"Connecting to database at {db_config['host']}...")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Check if column exists
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = %s
            AND TABLE_NAME = 'drivers'
            AND COLUMN_NAME = 'photo_url'
        """, (db_config['database'],))

        column_exists = cursor.fetchone()[0]

        if column_exists:
            print("Column 'photo_url' already exists in drivers table")
        else:
            # Add photo_url column
            print("Adding photo_url column to drivers table...")
            cursor.execute("""
                ALTER TABLE drivers
                ADD COLUMN photo_url VARCHAR(255) AFTER date_of_birth
            """)
            connection.commit()
            print("[OK] Column added successfully")

        cursor.close()
        connection.close()
        print("[OK] Database update complete!")

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
