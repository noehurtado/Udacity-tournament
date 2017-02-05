# Udacity back end project - Swiss tournament

Project to track players and matches in a game tournament by Noe Hurtado. 

### Overview:
Python module that uses PSQL database to keep track of players and matches in a game tournament. 

The tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of winds, or as close as possible. 

### Files:
1. `tournament.py` is our python file that connects to the database. 
2. `tournament.sql` the database file to create the tables and views needed. 
3. `tournament_test.py` to run tests. 

### Instructions:
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
