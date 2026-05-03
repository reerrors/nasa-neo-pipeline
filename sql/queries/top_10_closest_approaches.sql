WITH closest_asteroids AS(
SELECT
   *
FROM
   close_approaches
ORDER BY
   miss_distance_km ASC
LIMIT
   10
)

SELECT
    c.id_approach,
    c.close_approach_date,
    c.miss_distance_km,
    a.id_asteroid,
    a.name
FROM
    closest_asteroids c LEFT JOIN asteroids a ON c.id_asteroid = a.id_asteroid;

