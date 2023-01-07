-- DROP TABLE IF EXISTS user;

-- CREATE TABLE user (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   username TEXT UNIQUE NOT NULL,
--   password TEXT NOT NULL,
--   ticket TEXT NOT NULL
-- );
Create database Corendon_Wifi;
use Corendon_Wifi;
create table Wifi_Registration(
Seat_Nummer int,
Ticket_Nummer int,
primary key(Ticket_Nummer)
);