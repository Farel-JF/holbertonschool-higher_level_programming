-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- Select tv_genres.name as genre and count(tv_show_genres.show_id) as number_of_shows
SELECT AFTER.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres AS b
INNER JOIN tv_genres AS a
ON a.id = b.genre_id
GROUP BY a.name
ORDER BY number_of_shows DESC;
