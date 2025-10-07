-- F1 Racing sample data for testing and development
-- Run this after creating the schema to populate with sample records

-- Insert F1 Teams
INSERT INTO teams (team_name, country, team_principal) VALUES
('Ferrari', 'Italy', 'Fred Vasseur'),
('Mercedes', 'Germany', 'Toto Wolff'),
('Red Bull Racing', 'Austria', 'Christian Horner'),
('McLaren', 'United Kingdom', 'Andrea Stella'),
('Aston Martin', 'United Kingdom', 'Mike Krack'),
('Alpine', 'France', 'Oliver Oakes'),
('Williams', 'United Kingdom', 'James Vowles'),
('RB', 'Italy', 'Laurent Mekies'),
('Kick Sauber', 'Switzerland', 'Alessandro Alunni Bravi'),
('Haas', 'United States', 'Ayao Komatsu');

-- Insert F1 Drivers (2025 season)
INSERT INTO drivers (first_name, last_name, team_id, nationality, driver_number, date_of_birth) VALUES
-- Ferrari
('Lewis', 'Hamilton', 1, 'British', 44, '1985-01-07'),
('Charles', 'Leclerc', 1, 'Monegasque', 16, '1997-10-16'),
-- Mercedes
('George', 'Russell', 2, 'British', 63, '1998-02-15'),
('Kimi', 'Antonelli', 2, 'Italian', 12, '2006-08-25'),
-- Red Bull Racing
('Max', 'Verstappen', 3, 'Dutch', 1, '1997-09-30'),
('Liam', 'Lawson', 3, 'New Zealander', 30, '2002-02-11'),
-- McLaren
('Lando', 'Norris', 4, 'British', 4, '1999-11-13'),
('Oscar', 'Piastri', 4, 'Australian', 81, '2001-04-06'),
-- Aston Martin
('Fernando', 'Alonso', 5, 'Spanish', 14, '1981-07-29'),
('Lance', 'Stroll', 5, 'Canadian', 18, '1998-10-29'),
-- Alpine
('Pierre', 'Gasly', 6, 'French', 10, '1996-02-07'),
('Jack', 'Doohan', 6, 'Australian', 7, '2003-01-20'),
-- Williams
('Alex', 'Albon', 7, 'Thai', 23, '1996-03-23'),
('Carlos', 'Sainz', 7, 'Spanish', 55, '1994-09-01'),
-- RB
('Yuki', 'Tsunoda', 8, 'Japanese', 22, '2000-05-11'),
('Isack', 'Hadjar', 8, 'French', 6, '2004-09-28'),
-- Kick Sauber
('Nico', 'Hulkenberg', 9, 'German', 27, '1987-08-19'),
('Gabriel', 'Bortoleto', 9, 'Brazilian', 5, '2004-10-14'),
-- Haas
('Esteban', 'Ocon', 10, 'French', 31, '1996-09-17'),
('Oliver', 'Bearman', 10, 'British', 87, '2005-05-08');
