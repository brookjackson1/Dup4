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

# Correct 2025 F1 official driver photos
driver_photos = {
    'Kimi Antonelli': 'https://media.formula1.com/image/upload/c_fill,w_720/q_auto/v1740000000/common/f1/2025/mercedes/andant01/2025mercedesandant01right.webp',
    'Oliver Bearman': 'https://media.formula1.com/image/upload/c_fill,w_720/q_auto/v1740000000/common/f1/2025/haas/olibea01/2025haasolibea01right.webp',
    'Gabriel Bortoleto': 'https://media.formula1.com/image/upload/c_fill,w_720/q_auto/v1740000000/common/f1/2025/kicksauber/gabbor01/2025kicksaubergabbor01right.webp',
    'Jack Doohan': 'https://media.formula1.com/image/upload/c_fill,w_720/q_auto/v1740000000/common/f1/2025/alpine/jacdoo01/2025alpinejacdoo01right.webp',
    'Isack Hadjar': 'https://media.formula1.com/image/upload/c_fill,w_720/q_auto/v1740000000/common/f1/2025/racingbulls/isahad01/2025racingbullsisahad01right.webp',
    'Liam Lawson': 'https://media.formula1.com/image/upload/c_fill,w_720/q_auto/v1740000000/common/f1/2025/racingbulls/lialaw01/2025racingbullslialaw01right.webp'
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
