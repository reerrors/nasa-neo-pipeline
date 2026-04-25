import json
from datetime import datetime

def treat_neo_data(rawData,startDate,endDate):
    #near_earth_objects->'2024-01-02'->[lista]
    asteroidData = []
    closeAproachesData = []
    pipelineRunsData = []

    start = datetime.strptime(startDate,'%Y-%m-%d')
    end = datetime.strptime(endDate,'%Y-%m-%d')

    if not rawData:
        pipelineRunsData.append((datetime.now(),start,end,0,"failed"))
        return asteroidData, closeAproachesData, pipelineRunsData

    sample = rawData['near_earth_objects']

    for day in sample:
        for asteroid in sample[day]:
            tmp_ast = (asteroid['id'],
                       asteroid['name'],
                       float(asteroid['absolute_magnitude_h']),
                       asteroid['is_potentially_hazardous_asteroid']=='True',
                       float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']),
                       float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'])
	    )
            tmp_cap = (asteroid['id'],
                       asteroid['close_approach_data'][0]['close_approach_date'],
                       float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),
                       float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
            )
            asteroidData.append(tmp_ast)
            closeAproachesData.append(tmp_cap)
    tmp_run = (datetime.now(),start,end, len(asteroidData),"running")
    pipelineRunsData.append(tmp_run)

    return asteroidData, closeAproachesData, pipelineRunsData
