SELECT
    id_approach,
    miss_distance_km,
    AVG(miss_distance_km) OVER () AS avg_approach_distance,
    miss_distance_km - AVG(miss_distance_km) OVER () AS distance_from_avg
FROM
    close_approaches;

