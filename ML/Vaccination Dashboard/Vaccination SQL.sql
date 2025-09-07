-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS vaccination_db;

-- Switch to the correct database
USE vaccination_db;

-- Table 1: Coverage Data
CREATE TABLE coverage (
    country_code VARCHAR(3) NOT NULL,
    country_name VARCHAR(255),
    record_year INT,
    antigen VARCHAR(50),
    antigen_description TEXT,
    target_number BIGINT,
    doses BIGINT,
    coverage_percentage FLOAT,
    PRIMARY KEY (country_code, record_year, antigen)
);

-- Rest of your tables remain the same...
