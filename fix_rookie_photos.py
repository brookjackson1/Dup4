"""
Script to fix 2025 rookie driver photos with correct F1 2025 official URLs
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

# Correct 2025 F1 official driver photos - close-up headshot style
driver_photos = {
    'Kimi Antonelli': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2025/andant01.png',
    'Oliver Bearman': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2025/olibea01.png',
    'Gabriel Bortoleto': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2025/gabbor01.png',
    'Jack Doohan': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2025/jacdoo01.png',
    'Isack Hadjar': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2025/isahad01.png',
    'Liam Lawson': 'https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/2025/lialaw01.png'
}

def main():
    try:
        # Connect to database
        print(f"Connecting to database at {db_config['host']}...")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Update driver photos
        print("\nUpdating 2025 rookie driver photos with official F1 URLs...")
        for driver_name, photo_url in driver_photos.items():
            first_name, last_name = driver_name.split(' ', 1)
            cursor.execute("""
                UPDATE drivers
                SET photo_url = %s
                WHERE first_name = %s AND last_name = %s
            """, (photo_url, first_name, last_name))

            if cursor.rowcount > 0:
                print(f"  Updated: {driver_name}")
                print(f"    URL: {photo_url}")

        connection.commit()

        print("\n[OK] All rookie driver photos updated with 2025 official F1 URLs!")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
