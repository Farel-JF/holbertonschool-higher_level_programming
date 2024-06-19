-- Select tv_genres.name as genre and count(tv_show_genres.show_id) as number_of_shows
SELECT z.name AS genre, COUNT(x.show_id) AS number_of_shows
FROM tv_genres x
INNER JOIN tv_show_genres z
ON z.id = x.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
