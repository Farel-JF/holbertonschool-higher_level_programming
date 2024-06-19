-- Select the genre names associated with the show "Dexter"
-- From the tv_genres table, aliasing it as 'g'
-- Join tv_show_genres table 'sg' on genre_id from tv_genres matching id in tv_show_genresSELECT g.name
-- Join tv_shows table 's' on show_id from tv_show_genres matching id in tv_shows
-- Filter the results to only include genres associated with the show titled 'Dexter'
-- Order the results in ascending order by genre name
SELECT g.name
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
