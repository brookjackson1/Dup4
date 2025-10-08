-- F1 Racing Complete Seed Data for 2025 Season
-- Run this after creating the schema to populate with complete records including branding and photos

-- Insert F1 Teams with Complete Branding
INSERT INTO teams (team_id, team_name, country, team_principal, team_color, team_logo, secondary_color, car_image) VALUES
(1, 'Ferrari', 'Italy', 'Frédéric Vasseur', '#E8002D', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/ferrari.png', '#FFD700', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/ferrari.png'),
(2, 'Mercedes', 'Germany', 'Toto Wolff', '#00D2BE', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/mercedes.png', '#000000', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/mercedes.png'),
(3, 'Red Bull Racing', 'Austria', 'Christian Horner', '#0600EF', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/red%20bull.png', '#FFD700', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/red-bull-racing.png'),
(4, 'McLaren', 'United Kingdom', 'Andrea Stella', '#FF8700', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/mclaren.png', '#47C7FC', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/mclaren.png'),
(5, 'Aston Martin', 'United Kingdom', 'Mike Krack', '#006F62', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/aston%20martin.png', '#00352F', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/aston-martin.png'),
(6, 'Alpine', 'France', 'Oliver Oakes', '#0090FF', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/alpine.png', '#FF1801', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/alpine.png'),
(7, 'Williams', 'United Kingdom', 'James Vowles', '#005AFF', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/williams.png', '#00A0DE', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/williams.png'),
(8, 'RB', 'Italy', 'Laurent Mekies', '#0600EF', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/rb.png', '#FFD700', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/rb.png'),
(9, 'Kick Sauber', 'Switzerland', 'Alessandro Alunni Bravi', '#00E700', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/kick-sauber.png', '#000000', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/kick-sauber.png'),
(10, 'Haas', 'United States', 'Ayao Komatsu', '#FFFFFF', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/2018-redesign-assets/team%20logos/haas.png', '#B6BABD', 'https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2024/haas.png');

-- Insert F1 Drivers with Photos (2025 season)
INSERT INTO drivers (first_name, last_name, team_id, nationality, driver_number, date_of_birth, photo_url) VALUES
-- Ferrari
('Lewis', 'Hamilton', 1, 'British', 44, '1985-01-07', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/ferrari/lewham01/2025ferrarilewham01right.webp'),
('Charles', 'Leclerc', 1, 'Monegasque', 16, '1997-10-16', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/ferrari/chalec01/2025ferrarichalec01right.webp'),
-- Mercedes
('George', 'Russell', 2, 'British', 63, '1998-02-15', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/mercedes/georus01/2025mercedesgeorus01right.webp'),
('Kimi', 'Antonelli', 2, 'Italian', 12, '2006-08-25', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/mercedes/kimant01/2025mercedeskimant01right.webp'),
-- Red Bull Racing
('Max', 'Verstappen', 3, 'Dutch', 1, '1997-09-30', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/red-bull-racing/maxver01/2025red-bull-racingmaxver01right.webp'),
('Liam', 'Lawson', 3, 'New Zealander', 30, '2002-02-11', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/red-bull-racing/lialaw01/2025red-bull-racinglialaw01right.webp'),
-- McLaren
('Lando', 'Norris', 4, 'British', 4, '1999-11-13', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/mclaren/lannor01/2025mclarenlannor01right.webp'),
('Oscar', 'Piastri', 4, 'Australian', 81, '2001-04-06', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/mclaren/oscpia01/2025mclarenoscp ia01right.webp'),
-- Aston Martin
('Fernando', 'Alonso', 5, 'Spanish', 14, '1981-07-29', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/aston-martin/feralo01/2025aston-martinferalo01right.webp'),
('Lance', 'Stroll', 5, 'Canadian', 18, '1998-10-29', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/aston-martin/lanstr01/2025aston-martinlanstr01right.webp'),
-- Alpine
('Pierre', 'Gasly', 6, 'French', 10, '1996-02-07', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/alpine/piegas01/2025alpinepiegas01right.webp'),
('Jack', 'Doohan', 6, 'Australian', 7, '2003-01-20', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/alpine/jacdoo01/2025alpinejacdoo01right.webp'),
-- Williams
('Alex', 'Albon', 7, 'Thai', 23, '1996-03-23', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/williams/alealb01/2025williamsalealb01right.webp'),
('Carlos', 'Sainz', 7, 'Spanish', 55, '1994-09-01', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/williams/carsai01/2025williamscarsai01right.webp'),
-- RB
('Yuki', 'Tsunoda', 8, 'Japanese', 22, '2000-05-11', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/rb/yuktsu01/2025rbyuktsu01right.webp'),
('Isack', 'Hadjar', 8, 'French', 6, '2004-09-28', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/rb/isahad01/2025rbisahad01right.webp'),
-- Kick Sauber
('Nico', 'Hulkenberg', 9, 'German', 27, '1987-08-19', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/kick-sauber/nichul01/2025kick-saubernichul01right.webp'),
('Gabriel', 'Bortoleto', 9, 'Brazilian', 5, '2004-10-14', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/kick-sauber/gabbor01/2025kick-saubergabbor01right.webp'),
-- Haas
('Esteban', 'Ocon', 10, 'French', 31, '1996-09-17', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/haas/estoco01/2025haasestocon01right.webp'),
('Oliver', 'Bearman', 10, 'British', 87, '2005-05-08', 'https://media.formula1.com/image/upload/c_thumb,g_face,w_600,h_600,z_1.2/q_auto/v1740000000/common/f1/2025/haas/olibea01/2025haasolibea01right.webp');
