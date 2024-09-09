import os
import psycopg2  # Example using psycopg2 for PostgreSQL

# Load environment variables from the specified file
def load_env(file_path):
    """Loads environment variables from a specified file."""
    with open(file_path) as f:
        for line in f:
            if not line.startswith('#') and '=' in line:
                key, val = line.strip().split('=', 1)
                os.environ[key] = val

# Connect to the database
def connect_to_db(db_type, env_file):
    """Connects to a database based on the specified type and environment file."""
    load_env(env_file)
    
    if db_type == 'postgresql':
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            port=os.environ['DB_PORT']
        )
    # ... other database types (e.g., MySQL, Oracle)
    
    return conn

# Example usage:
conn = connect_to_db('postgresql', 'database_connections/postgresql/main.env')