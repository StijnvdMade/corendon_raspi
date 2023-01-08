-- DROP TABLE IF EXISTS user;

-- CREATE TABLE user (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   username TEXT UNIQUE NOT NULL,
--   password TEXT NOT NULL,
--   ticket TEXT NOT NULL
-- );
-- Create database Corendon_Wifi;
-- USE Corendon_Wifi;
DROP TABLE IF EXISTS Wifi_Registration ;
CREATE TABLE Wifi_Registration (
  Seat_Nummer VARCHAR(4),
  Ticket_Nummer VARCHAR(10),
  PRIMARY KEY(Ticket_Nummer)
);
Insert into Wifi_Registration values("F-05","XD03");
Insert into Wifi_Registration values("E-08","ZV07");
Insert into Wifi_Registration values("B-17","XD67");