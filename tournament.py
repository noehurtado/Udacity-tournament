#!/usr/local/bin/python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute('DELETE FROM Matches')
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute('DELETE FROM Players')
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute('SELECT COUNT (*) FROM Players')
    p_counter = c.fetchone()
    db.close()
    return p_counter[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    clean_name = bleach.clean(name)
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO Players (player_name) VALUES (%s);', (clean_name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute('SELECT * FROM standings')
    results = c.fetchall()
    db.close()
    return results

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winner = int(bleach.clean(winner))
    loser = int(bleach.clean(loser))
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO matches (winner, loser) VALUES (%d, %d)' % (winner, loser))
    db.commit()
    db.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
        
    As well, it makes sure that we have at least 2 players and that the total players are even. 
    """
    db = connect()
    c = db.cursor()
    c.execute('SELECT id, name, wins FROM standings ORDER by wins DESC')
    t_players = c.fetchall()
    db.close()

    p = 0
    pairing = []
    if len(t_players) % 2 == 0:
        while p < len(t_players):
            player1Id = t_players[p][0]
            player1Name = t_players[p][1]
            player2Id = t_players[p+1][0]
            player2Name = t_players[p+1][1]
            pairing.append((player1Id,player1Name,player2Id,player2Name))
            p += 2
        return pairing
    elif len(t_players) == 0:
            print "We need at least 2 players."
    else:
        print "We need one more player."

