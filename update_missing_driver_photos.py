"""
Script to add photos for missing drivers
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

# Driver photos for the missing drivers (using placeholder or available F1 media)
driver_photos = {
    'Kimi Antonelli': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2024/antkim01.png',
    'Oliver Bearman': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2024/beaoli01.png',
    'Gabriel Bortoleto': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2024/borgab01.png',
    'Jack Doohan': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2024/doojac01.png',
    'Isack Hadjar': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2024/hadisa01.png',
    'Liam Lawson': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2024/lawlia01.png'
}

def main():
    try:
        # Connect to database
        print(f"Connecting to database at {db_config['host']}...")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Update driver photos
        print("\nUpdating missing driver photos...")
        for driver_name, photo_url in driver_photos.items():
            first_name, last_name = driver_name.split(' ', 1)
            cursor.execute("""
                UPDATE drivers
                SET photo_url = %s
                WHERE first_name = %s AND last_name = %s
            """, (photo_url, first_name, last_name))

            if cursor.rowcount > 0:
                print(f"  Updated: {driver_name}")

        connection.commit()

        # Verify all drivers now have photos
        cursor.execute("SELECT first_name, last_name FROM drivers WHERE photo_url IS NULL")
        missing = cursor.fetchall()

        if missing:
            print("\n[WARNING] Still missing photos for:")
            for driver in missing:
                print(f"  - {driver[0]} {driver[1]}")
        else:
            print("\n[OK] All drivers now have photos!")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
