INSERT INTO rooms (name)
VALUES ('Studio A');

INSERT INTO rooms (name)
VALUES ('Studio B'),
       ('Practice Room');

INSERT INTO instruments (name, purchase_price, acquired_on, room_id)
VALUES ('Piano', 18000.00, '2026-09-01', 1);

SELECT *
FROM rooms;

SELECT *
FROM instruments;

UPDATE instruments
SET purchase_price = purchase_price * 1.10, name = 'Grand piano'
WHERE id = 1;

DELETE FROM instruments
WHERE id = 1;

ALTER TABLE rooms
ADD COLUMN capacity INT NOT NULL DEFAULT 1;

ALTER TABLE rooms
MODIFY COLUMN capacity INT NOT NULL DEFAULT 10;

ALTER TABLE rooms
DROP COLUMN capacity;

CREATE TABLE scratch_notes (
    note VARCHAR(100)
);

DROP TABLE scratch_notes;