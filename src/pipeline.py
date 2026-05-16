from extract import fetch_neo_data
from transform import treat_neo_data
from load import insert_neo_data
from datetime import datetime, timedelta, date
from dotenv import load_dotenv
import os
import psycopg2
import time
import sys

def send_Log(start,end,records,status):
    try:
        conn = psycopg2.connect(dbname  = os.getenv("DB_NAME"),
                                user = os.getenv("DB_USER"),
                                password = os.getenv("DB_PASSWORD"),
                                host = os.getenv("DB_HOST"),
                                port = os.getenv("DB_PORT")
                               )
        with conn:
    	    with conn.cursor() as curs:
                curs.execute("INSERT INTO pipeline_runs (run_at,start_date,end_date,records_extracted,status) VALUES (%s,%s,%s,%s,%s)",
                             (datetime.now(), start,end,records,status))
    except psycopg2.Error as e:
       print(f"Error: {e}")

load_dotenv()
today = datetime.today()
data_log = today.strftime("%Y-%m-%d %H:%M:%S")
try:
    conn = psycopg2.connect(dbname  = os.getenv("DB_NAME"),
                            user = os.getenv("DB_USER"),
                            password = os.getenv("DB_PASSWORD"),
                            host = os.getenv("DB_HOST"),
                            port = os.getenv("DB_PORT")
                               )
    with conn:
        with conn.cursor() as curs:
            curs.execute("SELECT end_date FROM pipeline_runs ORDER BY end_date DESC LIMIT 1;")
            query = curs.fetchone()
            last_date = query[0] if query else None
    if last_date == None:
        print(f"[{data_log}] No pipeline runs found.")
    if last_date == today.date():
        print(f"[{data_log}] The database is up to date.")
        sys.exit(0)
    else:
        print(f"[{data_log}] Database is not up to date. Last run: {last_date.strftime('%Y-%m-%d')}  ")

except Exception as e:
    print(f"[{data_log}] DB Error: {e}")
    sys.exit(1)

print(f"[{data_log}] Running ETL...")
records = 0
raw_data = fetch_neo_data(today.strftime("%Y-%m-%d"),today.strftime("%Y-%m-%d"))
if not raw_data:
    send_Log(today,today, records,"failed")
    sys.exit(0)
a,c = treat_neo_data(raw_data)
e = insert_neo_data(a,c)
if e:
    send_Log(today,today, records,"failed")
    sys.exit(0)

records += len(a)
send_Log(today, today, records,"loaded")
print(f"[{data_log}] Database successfully updated!")
