-- Task 2 From description to data model

-- areas: id INT -  PK, name VARCHAR(30)
-- An animal must belong to exactly one area.

-- animals: id INT - PK, name VARCHAR(30), species VARCHAR(30), weight_kg DECIMAL(5,2), arrival_date DATE ('YYYY-MM-DD'), area_id INT NOT NULL - FK
-- An area can have zero or more animals.

-- https://drive.google.com/file/d/130zBkVWJqf1SbnHwLIdgPivuazpuyWeo/view?usp=sharing

-- Task 3.1 Choose your own database

CREATE DATABASE IF NOT EXISTS animal_shelter_practice;

USE animal_shelter_practice;

SELECT DATABASE();

-- Task 3.2 Create the areas table

CREATE TABLE areas(
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
);

-- Task 3.3 Create the animal table

CREATE TABLE animals(
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    species VARCHAR(20) NOT NULL,
    weight DECIMAL(5,2),
    admitted_on DATE,
    area_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (area_id) REFERENCES areas(id)
)

-- Task 3.4 Check the structure

-- The `areas` table must be created before `animals` because `animals.area_id` is a foreign key referencing `areas.id`.
-- Therefore, the `areas` table must exist before this reference can be created.

-- The columns `animals.area_id` and `areas.id` must have compatible data types because the foreign key links the values in these columns.
-- The data types must be compatible so that the database can verify that each value in `animals.area_id` refers to an existing value in `areas.id`.

