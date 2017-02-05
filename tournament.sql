-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- *** Table for players ***
----------------------------------
-- player_id |    player_name
-----------+-------------------
--       201 | Twilight Sparkle
--       202 | Fluttershy
--       203 | Applejack
--       204 | Pinkie Pie
----------------------------------

CREATE TABLE players (
  player_id SERIAL PRIMARY KEY,
  player_name TEXT NOT NULL
  );


-- *** Table for matches ***
----------------------------------
-- match_id | winner | loser
------------+--------+-------
--       23 |    201 |   207
--       24 |    202 |   205
--       25 |    208 |   206
--       26 |    204 |   203
----------------------------------
CREATE TABLE matches (
  match_id SERIAL PRIMARY KEY,
  winner INTEGER REFERENCES Players(player_id),
  loser INTEGER REFERENCES Players(player_id)
  );

-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- *** Create standings view ***
----------------------------------------------------
-- id  |       name        | wins | total_matches
-------+-------------------+------+---------------
-- 202 | Fluttershy        |    1 |             1
-- 208 | Princess Luna     |    1 |             1
-- 204 | Pinkie Pie        |    1 |             1
-- 201 | Twilight Sparkle  |    1 |             1
----------------------------------------------------
CREATE VIEW standings AS
  SELECT players.player_id AS id,
    players.player_name AS name,
    count(matches.winner) AS wins,
    (SELECT COUNT(*) FROM matches
      WHERE players.player_id = matches.winner
      OR players.player_id = matches.loser) AS total_matches
  FROM players
  LEFT JOIN matches
  ON players.player_id = matches.winner
  GROUP BY players.player_id
  ORDER BY wins DESC;
