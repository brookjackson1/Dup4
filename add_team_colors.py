"""
Script to add team colors to the teams table
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

# F1 2025 team colors (official brand colors)
team_colors = {
    'Ferrari': '#DC0000',  # Rosso Corsa
    'Mercedes': '#00D2BE',  # Petronas Teal
    'Red Bull Racing': '#0600EF',  # Red Bull Blue
    'McLaren': '#FF8700',  # Papaya Orange
    'Aston Martin': '#006F62',  # British Racing Green
    'Alpine': '#0090FF',  # Alpine Blue
    'Williams': '#005AFF',  # Williams Blue
    'RB': '#2B4562',  # AlphaTauri Navy
    'Kick Sauber': '#900000',  # Alfa Romeo Red
    'Haas': '#FFFFFF',  # Haas White/Red
}

def main():
    try:
        # Connect to database
        print(f"Connecting to database at {db_config['host']}...")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Check if color column exists
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = %s
            AND TABLE_NAME = 'teams'
            AND COLUMN_NAME = 'team_color'
        """, (db_config['database'],))

        column_exists = cursor.fetchone()[0]

        if not column_exists:
            # Add team_color column
            print("Adding team_color column to teams table...")
            cursor.execute("""
                ALTER TABLE teams
                ADD COLUMN team_color VARCHAR(7) AFTER team_principal
            """)
            connection.commit()
            print("[OK] Column added successfully")

        # Update team colors
        print("Updating team colors...")
        for team_name, color in team_colors.items():
            cursor.execute("""
                UPDATE teams
                SET team_color = %s
                WHERE team_name = %s
            """, (color, team_name))

            if cursor.rowcount > 0:
                print(f"  Updated: {team_name} -> {color}")

        connection.commit()

        # Verify updates
        cursor.execute("SELECT team_name, team_color FROM teams ORDER BY team_name")
        teams = cursor.fetchall()
        print("\n[OK] Team colors updated:")
        for team in teams:
            print(f"  {team[0]}: {team[1]}")

        cursor.close()
        connection.close()
        print("\n[OK] Team colors update complete!")

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
