-- Select tv_genres.name as genre and count(tv_show_genres.show_id) as number_of_shows
SELECT z.name AS genre, COUNT(x.show_id) AS number_of_shows
FROM tv_genres x
LEFT JOIN tv_show_genres z
ON z.id = x.genre_id
GROUP BY x.genre_id
ORDER BY 2 DESC;
