CREATE TABLE IF NOT EXISTS cpu_benchmark (
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