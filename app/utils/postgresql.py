import psycopg2
from icecream import ic
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cur = conn.cursor()


def execute(command):
    cur.execute(command)
    conn.commit()


def close_connection():
    conn.close()
    cur.close()


def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS users ("
                "users_id SERIAL PRIMARY KEY, "
                "telegram_id VARCHAR(100), "
                "telegram_username TEXT)")
