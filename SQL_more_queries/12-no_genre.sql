-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- Select tv_genres.name as genre and count(tv_show_genres.show_id) as number_of_shows
SELECT z.name AS genre, count(x.show_id) AS number_of_shows
FROM tv_show_genres AS x
LEFT JOIN tv_genres As z
ON x.genre_id = z.id
GROUP BY x.genre_id
ORDER BY number_of_shows DESC;
