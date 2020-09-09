/* Check what data we have */
SELECT *
FROM stream
LIMIT 20;

SELECT *
FROM chat
LIMIT 20;

/* What distinct games do we have */
SELECT DISTINCT game
FROM stream;

SELECT DISTINCT channel
FROM stream;

/* Get a count of the viewers for each game */
SELECT game, COUNT(*)
FROM stream
GROUP BY game 
ORDER BY COUNT(*) DESC;

/* Get a count of the streams of LoL for each country */ 
SELECT country, COUNT(country)
FROM stream
WHERE game = 'League of Legends'
GROUP BY country
ORDER BY COUNT(country) DESC;

/*Get a count of how many users use that playing device to view streams */
SELECT player, COUNT(player)
FROM stream
GROUP BY player
ORDER BY COUNT(player) DESC;

/*Create new column of genre of each game */

SELECT game,
  CASE 
    WHEN game = 'League of Legends' 
    THEN 'MOBA'
    WHEN game = 'DOTA 2' 
    THEN 'MOBA'
    WHEN game = 'Heroes of the Storm' 
    THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive' 
    THEN 'FPS'
    WHEN game = 'DayZ' 
    THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved' 
    THEN 'Survival'
    ELSE 'Other'
    END AS 'genre',
    COUNT(*)
FROM stream
GROUP BY game
ORDER BY COUNT(*) DESC;

/* Look at the change in view count across the day */
SELECT time
FROM stream
LIMIT 10;

/* Return a table of each hour in the day and view count of that hour in the UK*/
SELECT strftime('%H', time) AS hour, COUNT(*), country
FROM stream
WHERE country = 'GB'
GROUP BY hour
ORDER BY COUNT(*) DESC;

/* Do an inner join on device_id */
SELECT *
FROM stream 
INNER JOIN chat ON stream.device_id = chat.device_id;

/* Now review how chat and game users vary by country*/
SELECT country, COUNT(*)
FROM stream
GROUP BY country
ORDER BY COUNT(*) DESC;

SELECT country, COUNT(*)
FROM chat
GROUP BY country;
