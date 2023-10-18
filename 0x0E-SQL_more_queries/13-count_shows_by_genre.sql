-- lists the number of shows by genre
SELECT name AS genre, COUNT(genre_id) AS number_shows FROM tv_show_genres
JOIN tv_genres
ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC; 
