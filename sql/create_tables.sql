CREATE TABLE IF NOT EXISTS asteroids (
	id_asteroid TEXT PRIMARY KEY,
	name TEXT NOT NULL,
	absolute_magnitude FLOAT,
	is_potentially_hazardous BOOLEAN,
	estimated_diameter_min_km FLOAT,
	estimated_diameter_max_km FLOAT
);

CREATE TABLE IF NOT EXISTS close_aproaches (
	id_aproach SERIAL PRIMARY KEY,
	id_asteroid TEXT REFERENCES asteroids(id_asteroid),
	close_approach_date DATE,
	relative_velocity_kmh FLOAT,
	miss_distance_km FLOAT,
	orbiting_body TEXT
);

CREATE TABLE IF NOT EXISTS pipeline_runs (
	id_run SERIAL PRIMARY KEY,
	run_at TIMESTAMP DEFAULT NOW(),
	start_date DATE,
	end_date DATE,
	records_extracted INT,
	status TEXT
);
