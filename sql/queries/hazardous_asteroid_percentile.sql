WITH volume_by_hazardous AS(
SELECT
    is_potentially_hazardous,
    COUNT(*) AS volume
FROM
    asteroids
GROUP BY
    is_potentially_hazardous
)
SELECT
    is_potentially_hazardous,
    volume,
    100.0 * volume / SUM(volume) OVER() AS percentage
FROM
    volume_by_hazardous;

