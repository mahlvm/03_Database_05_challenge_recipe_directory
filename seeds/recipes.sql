DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cooking_time INTEGER,
    rating INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Toast', 5, 2);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Ragou', 60, 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Pasta', 20, 3);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Rice', 35, 5);