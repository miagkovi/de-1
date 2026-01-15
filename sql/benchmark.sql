CREATE TABLE IF NOT EXISTS cpu_benchmark (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cpu_name VARCHAR(100),
    price NUMERIC,
    cpu_mark INT,
    cpu_value NUMERIC,
    thread_mark INT,
    thread_value NUMERIC,
    tdp NUMERIC,
    power_perf NUMERIC,
    cores INT,
    test_date INT,
    socket VARCHAR(50),
    category VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT now()
);