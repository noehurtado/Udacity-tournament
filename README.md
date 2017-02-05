# Udacity back end project - Swiss tournament

Project to track players and matches in a game tournament by Noe Hurtado. 

### Overview:
Python module that uses PSQL database to keep track of players and matches in a game tournament. 

The tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of winds, or as close as possible. 

### Files:
1. `tournament.py` is our python file that connects to the database. 
2. `tournament.sql` the database file to create the tables and views needed. 
3. `tournament_test.py` to run tests. 

### Instructions to create the database, tables and views needed:
1. Start Vagrant by opening Terminal and typing:
``` 
$  vagrant up
$  vagrant ssh
```
2. Change to the tournament directory by typing:
``` 
$  cd /vagrant/tournament
```
3. Access to PSQL tournament and paste the tournament.sql content and then quit the psql 
``` 
$  psql tournament 
-- CREATE TABLES AS PER tournament.sql -- 
$  \q
```

### Import tournament & tournament functions:
1. Inside python script, import tournament.py
2. Once tournament.py was imported, you will be able to use the following functions:

registerPlayer(name)<br />
Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

countPlayers()<br />
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

deletePlayers()<br />
Clear out all the player records from the database.

reportMatch(winner, loser)<br />
Stores the outcome of a single match between two players in the database.

deleteMatches()<br />
Clear out all the match records from the database.

playerStandings()<br />
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

swissPairings()<br />
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.


### Run Tests:
To make sure everything is working, we use the termainal inside `vagrant` to run the test: `$ python tournament_test.py`

```
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.`
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
```

The expected outcome after running the `tournament_test.py` is: `Success!  All tests pass!`
