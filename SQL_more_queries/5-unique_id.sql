-- Script to create the table unique_id with constraints

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
