from extract import fetch_neo_data
from transform import treat_neo_data
from load import insert_neo_data
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import psycopg2
import time

load_dotenv()


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
       print(f"log error: {e}")


start = datetime(2024,1,1)
end = datetime(2024,12,31)
records = 0

current = start
while current < end:
    chunk_end = min(current + timedelta(days=7),end)
    raw_data = fetch_neo_data(current.strftime("%Y-%m-%d"),chunk_end.strftime("%Y-%m-%d"))
    if not raw_data:
        send_Log(start,chunk_end, records,"failed")
        break
    a,c = treat_neo_data(raw_data)
    e = insert_neo_data(a,c)
    if e:
        send_Log(start,chunk_end, records,"failed")
        break
    time.sleep(5)
    current = chunk_end + timedelta(days=1)
    records += len(a)
if not e:
    send_Log(start,end,records,"loaded")
#Eu deveria carregar por chunk?
#Código deveria continuar com alguma execeção do load?
