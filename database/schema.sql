-- Database Schema for F1 Racing Application
-- Run this file to create the required database structure

-- Drop existing tables if they exist
DROP TABLE IF EXISTS drivers;
DROP TABLE IF EXISTS teams;

-- Create teams table
CREATE TABLE teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(100),
    team_principal VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create drivers table
CREATE TABLE drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    team_id INT,
    nationality VARCHAR(100),
    driver_number INT,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Add indexes for common queries
CREATE INDEX idx_drivers_name ON drivers (last_name, first_name);
CREATE INDEX idx_drivers_team ON drivers (team_id);
CREATE INDEX idx_teams_name ON teams (team_name);