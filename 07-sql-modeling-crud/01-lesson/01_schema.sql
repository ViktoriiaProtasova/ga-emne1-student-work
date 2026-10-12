CREATE DATABASE IF NOT EXISTS music_school;

USE music_school;

SELECT DATABASE();

CREATE TABLE rooms(
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id)
);

CREATE TABLE instruments (
    id INT AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    purchase_price DECIMAL(8,2), -- 100000.00
    acquired_on DATE,
    room_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
