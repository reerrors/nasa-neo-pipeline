from extract import fetch_neo_data
from transform import treat_neo_data

raw_data = fetch_neo_data("2024-01-01","2024-01-05")

a,c,r = treat_neo_data(raw_data,"2024-01-01","2024-01-05")
print("Asteroids Data")
print(f"{a}\n")

print("Close Aproaches")
print(f"{c}\n")

print("Pipeline runs")
print(f"{r}\n")
