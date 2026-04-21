import json

def treat(rawData):
    #near_earth_objects->'2024-01-02'->[lista]
    asteroids = rawData['near_earth_objects']['2024-01-02']
    data = []
    for asteroid in asteroids:
        tmp = (asteroid['id'],
               asteroid['name'],
               float(asteroid['absolute_magnitude_h']),
               asteroid['is_potentially_hazardous_asteroid']=='True',
               float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']),
               float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'])
	)
        data.append(tmp)
    return data
