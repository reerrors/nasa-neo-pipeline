from extract import fetch_neo_data
from transform import treat

raw_data = fetch_neo_data("2024-01-01","2024-01-05")
data = treat(raw_data)
print(data)
