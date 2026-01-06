CREATE TABLE IF NOT EXISTS load_metadata (
    run_id UUID PRIMARY KEY,
    dataset_name VARCHAR(100) NOT NULL,
    status VARCHAR(20),
    error_message TEXT,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cpu_benchmark (
    id SERIAL PRIMARY KEY,
    cpu_name VARCHAR(100),
    price NUMERIC,
    cpu_mark INT,
    cpu_value NUMERIC,
    thread_mark INT,
    thread_value NUMERIC,
    tdp INT,
    power_perf NUMERIC,
    cores INT,
    test_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);