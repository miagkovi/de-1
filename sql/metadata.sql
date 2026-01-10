CREATE TABLE IF NOT EXISTS metadata (
    run_id UUID PRIMARY KEY,
    run_status VARCHAR(20),
    run_start TIMESTAMP,
    run_end TIMESTAMP,
    run_errors TEXT
);