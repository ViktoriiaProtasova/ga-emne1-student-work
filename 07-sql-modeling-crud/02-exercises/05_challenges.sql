-- Challenge 1: Volunteers and Animals.

-- https://drive.google.com/file/d/1wZZeFzZVost1Kz8yIT3HnO3mXFCxp3hY/view?usp=sharing

-- The pair (volunteer_id, animal_id) must be UNIQUE because one row means
-- "this volunteer follows up this animal". The same fact should be stored
-- only once. Without the constraint, the same volunteer could be linked to
-- the same animal twice, which gives duplicate and confusing data.

-- Each foreign key alone must NOT be UNIQUE:
-- If volunteer_id were UNIQUE, a volunteer could appear in only one row,
-- so one volunteer could follow only one animal.
-- If animal_id were UNIQUE, an animal could appear in only one row,
-- so each animal could have only one volunteer.
-- Both would break the many-to-many relationship, which is the whole
-- reason for having the link table.

-- Challenge 2: Build and test the junction table.

