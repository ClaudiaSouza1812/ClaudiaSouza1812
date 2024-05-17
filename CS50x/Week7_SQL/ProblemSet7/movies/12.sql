-- select a list of titles from movies table
-- select Jennifer Lawrence's id from people table = (SELECT people.id FROM people WHERE people.name = "Jennifer Lawrence"))
-- select movie_id froms stars relational table where person_id be the same as Jennifer Lawrence id = (SELECT stars.movie_id FROM stars WHERE stars.person_id IN (SELECT people.id FROM people WHERE people.name = "Jennifer Lawrence"))
-- use the command INTERSECT to show the rows that are similar in both queries
-- select a list of titles from movies table
-- select Bradley Cooper's id from people table = (SELECT people.id FROM people WHERE people.name = "Bradley Cooper"))
-- select movie_id froms stars relational table where person_id be the same as Bradley Cooper id = (SELECT stars.movie_id FROM stars WHERE stars.person_id IN (SELECT people.id FROM people WHERE people.name = "Bradley Cooper"))

SELECT title FROM movies
WHERE movies.id IN (SELECT stars.movie_id FROM stars WHERE stars.person_id IN (SELECT people.id FROM people WHERE people.name = "Jennifer Lawrence"))
INTERSECT
SELECT title FROM movies
WHERE movies.id IN (SELECT stars.movie_id FROM stars WHERE stars.person_id IN (SELECT people.id FROM people WHERE people.name = "Bradley Cooper"));

