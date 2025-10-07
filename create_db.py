"""
Script to create database tables from schema.sql using credentials from .env file
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

def run_sql_file(cursor, filepath):
    """Execute SQL statements from a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        sql_content = f.read()

    # Remove comments and split by semicolons
    lines = []
    for line in sql_content.split('\n'):
        line = line.strip()
        if line and not line.startswith('--'):
            lines.append(line)

    sql_content = ' '.join(lines)
    statements = sql_content.split(';')

    for statement in statements:
        statement = statement.strip()
        if statement:
            cursor.execute(statement)

def main():
    try:
        # Connect to database
        print(f"Connecting to database at {db_config['host']}...")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Run schema
        print("Creating tables from schema.sql...")
        run_sql_file(cursor, 'database/schema.sql')
        connection.commit()
        print("[OK] Tables created successfully")

        # Run seed data
        print("Inserting seed data...")
        run_sql_file(cursor, 'database/seed_data.sql')
        connection.commit()
        print("[OK] Seed data inserted successfully")

        # Verify tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"\nTables in database: {[table[0] for table in tables]}")

        # Show record counts
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"  - {table_name}: {count} records")

        cursor.close()
        connection.close()
        print("\n[OK] Database setup complete!")

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    main()
