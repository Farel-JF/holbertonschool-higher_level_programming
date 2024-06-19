-- Select tv_shows.title and tv_show_genres.genre_id from tv_shows and tv_show_genres tables
SELECT tv_shows.title As title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
