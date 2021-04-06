-- Albums
CREATE TABLE Albums (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(70) NOT NULL,
  artist VARCHAR(70) NOT NULL,
  year_published INTEGER NOT NULL
);

-- Songs 
CREATE TABLE Songs (
  id INTEGER,
  album_id INTEGER NOT NULL,
  name VARCHAR(100) NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (album_id) REFERENCES Albums(id)
);

-- Dataset Insertion 
INSERT INTO Albums
  (name, artist, year_published)
VALUES
  ('The Dark Side of the Moon', 'Pink Floyd', 1973),
  ('Abbey Road', 'The Beatles', 1969),
  ('Hotel California', 'Eagles', 1976),
  ('Born in the U.S.A.', 'Bruce Springsteen', 1984),
  ('California', 'Blink-182', 2016)
;

INSERT INTO Songs 
  (name, album_id)
VALUES
  ('Hello from the other side', 1),
  ('On the run', 1),
  ('Time', 1),
  ('Come Together', 2),
  ('Something', 3),
  ('Oh, Darling!', 4)
;

/* Required to get result in column format */
.headers on
.mode column


/* Queries */

SELECT * FROM Albums;

SELECT * FROM Songs;

SELECT Songs.name as song, Albums.name as album 
FROM Songs 
JOIN Albums ON Songs.album_id = Albums.id;

SELECT *
From Albums
WHERE 1970 <= year_published AND year_published <= 1980;

SELECT Songs.name as song, Albums.name as album, Albums.year_published
FROM Songs
JOIN Albums ON Songs.album_id = Albums.id
WHERE 1970 <= year_published AND year_published <= 1980;

SELECT Songs.name as song, Albums.name as album
FROM Songs
JOIN Albums ON Songs.album_id = Albums.id
WHERE album LIKE "%California%";
