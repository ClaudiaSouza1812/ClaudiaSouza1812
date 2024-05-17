-- select a list of movies ids where kevin bacon starred = (SELECT stars.movie_id FROM stars, people WHERE stars.person_id = (SELECT people.id WHERE name = "Kevin Bacon" AND birth = 1958))
-- select a list of people names where their id's are in the stars relational table = SELECT people.name FROM people, stars WHERE stars.person_id = people.id
-- and the movie_id from the relational database be in the list of id movies extracted before = AND stars.movie_id IN
-- finally select all names except the Kevin's Bacon name = AND people.name != "Kevin Bacon";

SELECT people.name FROM people, stars
WHERE people.id = stars.person_id
AND stars.movie_id IN (SELECT stars.movie_id FROM stars WHERE stars.person_id = (SELECT people.id FROM people WHERE people.name = "Kevin Bacon" AND people.birth = 1958))
AND people.name != "Kevin Bacon";




