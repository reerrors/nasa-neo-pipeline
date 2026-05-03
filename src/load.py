import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def insert_neo_data(a,c):
    try:
        conn = psycopg2.connect(dbname  = os.getenv("DB_NAME"),
                                user = os.getenv("DB_USER"),
                                password = os.getenv("DB_PASSWORD"),
                                host = os.getenv("DB_HOST"),
                                port = os.getenv("DB_PORT")
                               )
        with conn:
            with conn.cursor() as curs:
                curs.executemany("INSERT INTO asteroids (id_asteroid,name,absolute_magnitude,is_potentially_hazardous,estimated_diameter_min_km,estimated_diameter_max_km) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (id_asteroid) DO NOTHING" ,a)
            with conn.cursor() as curs:
                curs.executemany("INSERT INTO close_approaches (id_asteroid, close_approach_date,relative_velocity_kmh,miss_distance_km,orbiting_body) VALUES (%s,%s,%s,%s,%s)",c)
        return 0

    except psycopg2.Error as e:
        print(f"Load error: {e}")
        return e

