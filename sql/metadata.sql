CREATE TABLE IF NOT EXISTS metadata (
    run_id UUID PRIMARY KEY,
    dataset_name VARCHAR(100) NOT NULL,
    status VARCHAR(20),
    error_message TEXT,
    started_at TIMESTAMP,
    finished_at TIMESTAMP
);