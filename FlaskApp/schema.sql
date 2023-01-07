-- DROP TABLE IF EXISTS user;

-- CREATE TABLE user (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   username TEXT UNIQUE NOT NULL,
--   password TEXT NOT NULL,
--   ticket TEXT NOT NULL
-- );
-- Create database Corendon_Wifi;
USE Corendon_Wifi;
CREATE TABLE Wifi_Registration(
Seat_Nummer int,
Ticket_Nummer int,
PRIMARY KEY(Ticket_Nummer)
);