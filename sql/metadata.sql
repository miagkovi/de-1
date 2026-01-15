CREATE TABLE IF NOT EXISTS metadata (
    run_id UUID PRIMARY KEY,
    dataset_provider VARCHAR(50),
    dataset_name VARCHAR(50),
    status VARCHAR(20),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    errors TEXT
);