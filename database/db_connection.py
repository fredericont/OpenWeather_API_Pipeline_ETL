import psycopg2
from psycopg2.extras import RealDictCursor
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import load_config

def get_db_connection():
    try:
        config = load_config('../config/db_config.json')
        
        conn = psycopg2.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password'],
            port=config['port']
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def execute_query(query, params=None):
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error executing query: {e}")
            return False
        finally:
            conn.close()
    return False 