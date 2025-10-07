"""
Script to add team logos and secondary colors for enhanced branding
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

# F1 2025 team data with logos and secondary colors
team_branding = {
    'Ferrari': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/ferrari.png',
        'secondary_color': '#FFD700',  # Gold
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/ferrari.png'
    },
    'Mercedes': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/mercedes.png',
        'secondary_color': '#000000',  # Black
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/mercedes.png'
    },
    'Red Bull Racing': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/red%20bull.png',
        'secondary_color': '#FCD700',  # Yellow
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/red-bull-racing.png'
    },
    'McLaren': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/mclaren.png',
        'secondary_color': '#47C7FC',  # Blue
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/mclaren.png'
    },
    'Aston Martin': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/aston%20martin.png',
        'secondary_color': '#CEDC00',  # Lime
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/aston-martin.png'
    },
    'Alpine': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/alpine.png',
        'secondary_color': '#FF1801',  # Red
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/alpine.png'
    },
    'Williams': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/williams.png',
        'secondary_color': '#00A0DE',  # Light Blue
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/williams.png'
    },
    'RB': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/alphatauri.png',
        'secondary_color': '#FFFFFF',  # White
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/rb.png'
    },
    'Kick Sauber': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/alfa.png',
        'secondary_color': '#FFFFFF',  # White
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/kick-sauber.png'
    },
    'Haas': {
        'logo': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/haas.png',
        'secondary_color': '#B6BABD',  # Gray
        'car_image': 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/haas.png'
    }
}

def main():
    try:
        # Connect to database
        print(f"Connecting to database at {db_config['host']}...")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Check and add columns if they don't exist
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = %s
            AND TABLE_NAME = 'teams'
            AND COLUMN_NAME = 'team_logo'
        """, (db_config['database'],))

        if cursor.fetchone()[0] == 0:
            print("Adding team_logo column...")
            cursor.execute("ALTER TABLE teams ADD COLUMN team_logo VARCHAR(255) AFTER team_color")
            connection.commit()

        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = %s
            AND TABLE_NAME = 'teams'
            AND COLUMN_NAME = 'secondary_color'
        """, (db_config['database'],))

        if cursor.fetchone()[0] == 0:
            print("Adding secondary_color column...")
            cursor.execute("ALTER TABLE teams ADD COLUMN secondary_color VARCHAR(7) AFTER team_logo")
            connection.commit()

        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = %s
            AND TABLE_NAME = 'teams'
            AND COLUMN_NAME = 'car_image'
        """, (db_config['database'],))

        if cursor.fetchone()[0] == 0:
            print("Adding car_image column...")
            cursor.execute("ALTER TABLE teams ADD COLUMN car_image VARCHAR(255) AFTER secondary_color")
            connection.commit()

        # Update team branding
        print("\nUpdating team branding...")
        for team_name, branding in team_branding.items():
            cursor.execute("""
                UPDATE teams
                SET team_logo = %s, secondary_color = %s, car_image = %s
                WHERE team_name = %s
            """, (branding['logo'], branding['secondary_color'], branding['car_image'], team_name))

            if cursor.rowcount > 0:
                print(f"  Updated: {team_name}")

        connection.commit()

        print("\n[OK] Team branding enhanced successfully!")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
