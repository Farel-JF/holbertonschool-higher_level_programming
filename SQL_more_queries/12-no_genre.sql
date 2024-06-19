-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- Select tv_genres.name as genre and count(tv_show_genres.show_id) as number_of_shows
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_genres g
LEFT JOIN (
    SELECT genre_id, show_id
    FROM tv_show_genres
    GROUP BY genre_id, show_id
) sg ON g.id = sg.genre_id
GROUP BY g.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
