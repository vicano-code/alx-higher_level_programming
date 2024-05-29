-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows_rate;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows_rate
--
-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating FROM tv_shows
	INNER JOIN tv_show_ratings
	ON tv_show_ratings.show_id = tv_shows.id
	GROUP BY tv_shows.title
	ORDER BY rating DESC;
