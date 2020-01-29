# Radio Data Exercises

```sql
-- 1a. Which listener has the email address, 'nathaniel@hotmail.com'?
SELECT *
FROM listeners
WHERE email_address = 'nathaniel@hotmail.com';


-- 1b. Which listeners have an email address that contains the text, '@gmail.com'?
SELECT *
FROM listeners
WHERE email_address LIKE '%@gmail.com%';
```

```sql
-- 2a. What is the duration of the longest / shortest song?

SELECT max(duration_milliseconds) FROM songs;

SELECT duration_milliseconds
FROM songs
ORDER BY duration_milliseconds DESC
LIMIT 1;
```


```sql
-- 3a. How many songs have been played?
SELECT count(DISTINCT song_id) AS song_count
FROM plays;
```

```sql
-- 3b. How many songs have NOT been played?
SELECT count(DISTINCT songs.id) AS unplayed_song_count
FROM songs
LEFT JOIN plays on plays.song_id = songs.id
WHERE plays.song_id IS NULL;

-- which ones?
select distinct s.*
from songs s
left join plays p on p.song_id = s.id
where p.song_id is null
```

```sql
-- how many times has each song been played?
select
 s.id
 ,s.title
 ,s.artist_name
 ,count(distinct p.id) as play_count
from songs s
left join plays p on p.song_id = s.id
group by 1,2,3
order by play_count DESC;
```

```sql
-- 5a. What are the email addresses of the listeners whose credit cards are set to expire during the month of November 2020?

SELECT *
FROM listeners l
JOIN listener_accounts la ON l.id = la.listener_id
WHERE la.cc_exp_month = 11
  AND la.cc_exp_year = 2020;
```

```sql
-- 6a. How many times has each type of thumb button been pressed?

SELECT
 thumb_type
 ,count(DISTINCT id) as press_count
FROM thumbs
GROUP BY thumb_type;

--- ... between '2015-08-01' and '2015-09-15'?
SELECT
 thumb_type
 ,count(DISTINCT id) as press_count
FROM thumbs
where thumb_pressed_at between '2015-08-01' and '2015-09-30'
GROUP BY thumb_type;
```


```sql
-- 7c. Which 3 songs have been skipped the most?
SELECT
  songs.id
  ,songs.title
  ,count(DISTINCT skips.id) as skip_count
FROM songs
JOIN plays on plays.song_id = songs.id
JOIN skips on skips.play_id = plays.id
GROUP BY 1,2
ORDER BY skip_count DESC
LIMIT 3;
```
