import os
import requests
from dotenv import load_dotenv
import datetime
from requests.exceptions import HTTPError

load_dotenv()

def fetch_neo_data(start_date, end_date):
    API_KEY = os.getenv("NASA_API_KEY")
    payload = {"api_key":API_KEY,"start_date":start_date,"end_date":end_date}
    try:
        r = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed",params=payload)
        r.raise_for_status()
        return r.json()
    except HTTPError as e:
        print(f"Erro HTTP: {e}")
        return None
    except Exception as e:
        print(f"Erro geral: {e}")
        return None
