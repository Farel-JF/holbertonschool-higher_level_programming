-- Select the title of shows categorized as "Comedy"
-- From the tv_shows table, aliasing it as 's'
-- Join tv_show_genres table 'sg' on show_id from tv_shows matching id in tv_show_genres
-- Join tv_genres table 'g' on genre_id from tv_show_genres matching id in tv_genres
-- Filter the results to only include shows where the genre name is 'Comedy'
-- Order the results in ascending order by the show title
SELECT s.title
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN tv_genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;

