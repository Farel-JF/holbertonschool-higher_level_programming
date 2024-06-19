-- Select the title of shows and their linked genre names
-- From the tv_shows table, aliasing it as 's'
-- Left join tv_show_genres table 'sg' on show_id from tv_shows matching id in tv_show_genres
-- Left join tv_genres table 'g' on genre_id from tv_show_genres matching id in tv_genres
-- Order the results in ascending order by the show title and genre name
SELECT s.title, COALESCE(g.name, 'NULL') AS name
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY s.title ASC, name ASC;
