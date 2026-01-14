CREATE TABLE IF NOT EXISTS metadata (
    run_id UUID PRIMARY KEY,
    status VARCHAR(20),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    errors TEXT
);