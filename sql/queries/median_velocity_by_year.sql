SELECT
    EXTRACT(YEAR FROM close_approach_date) as year,
    AVG(relative_velocity_kmh) as avg_velocity_kmh
FROM
    close_approaches
GROUP BY
    year
ORDER BY
    year ASC
