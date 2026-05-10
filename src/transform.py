import json
from datetime import datetime

def treat_neo_data(raw_data):
    #near_earth_objects->'2024-01-02'->[lista]
    if not raw_data:
        return None

    asteroid_data = []
    close_approaches_data = []

    sample = raw_data['near_earth_objects']

    for day in sample:
        for asteroid in sample[day]:
            tmp_ast = (asteroid['id'],
                       asteroid['name'],
                       float(asteroid['absolute_magnitude_h']),
                       asteroid['is_potentially_hazardous_asteroid'],
                       float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']),
                       float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'])
	    )
            tmp_cap = (asteroid['id'],
                       datetime.strptime(asteroid['close_approach_data'][0]['close_approach_date'],'%Y-%m-%d'),
                       float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),
                       float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
                       asteroid['close_approach_data'][0]['orbiting_body']
            )
            asteroid_data.append(tmp_ast)
            close_approaches_data.append(tmp_cap)

    return asteroid_data, close_approaches_data
