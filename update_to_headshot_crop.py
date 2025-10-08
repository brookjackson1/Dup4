"""
Script to update driver photos to use headshot crops with Cloudinary transformations
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

# Driver photos showing from stomach and up
# Using c_crop,g_face with negative y offset to shift crop upward
driver_photos = {
    # Ferrari
    'Lewis Hamilton': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/ferrari/lewham01/2025ferrarilewham01right.webp',
    'Charles Leclerc': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/ferrari/chalec01/2025ferrarichalec01right.webp',

    # Mercedes
    'George Russell': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/mercedes/georus01/2025mercedesgeorus01right.webp',
    'Kimi Antonelli': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/mercedes/andant01/2025mercedesandant01right.webp',

    # Red Bull Racing
    'Max Verstappen': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/redbullracing/maxver01/2025redbullracingmaxver01right.webp',
    'Liam Lawson': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/redbullracing/lialaw01/2025redbullracinglialaw01right.webp',

    # McLaren
    'Lando Norris': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/mclaren/lannor01/2025mclarenlannor01right.webp',
    'Oscar Piastri': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/mclaren/oscpia01/2025mclarenocspia01right.webp',

    # Aston Martin
    'Fernando Alonso': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/astonmartin/feralo01/2025astonmartinferalo01right.webp',
    'Lance Stroll': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/astonmartin/lanstr01/2025astonmartinlanstr01right.webp',

    # Alpine
    'Pierre Gasly': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/alpine/piegas01/2025alpinepiegas01right.webp',
    'Jack Doohan': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/alpine/jacdoo01/2025alpinejacdoo01right.webp',

    # Williams
    'Carlos Sainz': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/williams/carsai01/2025williamscarsai01right.webp',
    'Alex Albon': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/williams/alealb01/2025williamsalealb01right.webp',

    # RB (Racing Bulls)
    'Yuki Tsunoda': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/racingbulls/yuktsu01/2025racingbullsyuktsu01right.webp',
    'Isack Hadjar': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/racingbulls/isahad01/2025racingbullsisahad01right.webp',

    # Kick Sauber
    'Nico Hulkenberg': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/kicksauber/nichul01/2025kicksaubernichul01right.webp',
    'Gabriel Bortoleto': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/kicksauber/gabbor01/2025kicksaubergabbor01right.webp',

    # Haas
    'Esteban Ocon': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/haas/estoco01/2025haasestoco01right.webp',
    'Oliver Bearman': 'https://media.formula1.com/image/upload/c_crop,g_face,w_800,h_1000,z_0.5,y_-0.3/q_auto/v1740000000/common/f1/2025/haas/olibea01/2025haasolibea01right.webp',
}

def main():
    try:
        # Connect to database
        print(f"Connecting to database at {db_config['host']}...")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Update all driver photos to headshot crops
        print("\nUpdating all driver photos to auto-cropped headshots...")
        updated_count = 0
        for driver_name, photo_url in driver_photos.items():
            first_name, last_name = driver_name.split(' ', 1)
            cursor.execute("""
                UPDATE drivers
                SET photo_url = %s
                WHERE first_name = %s AND last_name = %s
            """, (photo_url, first_name, last_name))

            if cursor.rowcount > 0:
                updated_count += 1
                print(f"  Updated: {driver_name}")

        connection.commit()

        print(f"\n[OK] Updated {updated_count} driver photos to headshot crops!")
        print("\nThese URLs use Cloudinary face detection to automatically crop to headshots")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
