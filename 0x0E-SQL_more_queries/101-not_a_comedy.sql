-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows
WHERE tv_genres.name = 'Comedy'
ORDER BY name ASC;
