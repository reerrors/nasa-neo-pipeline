WITH hazardous_approaches AS(
SELECT
    c.id_approach,
    EXTRACT(MONTH FROM c.close_approach_date) AS month,
    EXTRACT(YEAR FROM c.close_approach_date) AS year,
    a.id_asteroid,
    a.name,
    a.is_potentially_hazardous
FROM
    close_approaches c LEFT JOIN asteroids a ON c.id_asteroid = a.id_asteroid
WHERE
   a.is_potentially_hazardous = True
)
SELECT
   month,
   year,
   COUNT(DISTINCT id_approach) as hazardous_volume
FROM
   hazardous_approaches
GROUP BY
   month, year
ORDER BY
   hazardous_volume DESC
LIMIT
   1;
