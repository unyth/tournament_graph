"""
This is the go division class.

It represents a playing division in a go tournament. In an (or the) open
division, all players play even games against each other. In a handicap
division, player play against each other with the higher ranked player
taking white, and giving the lower ranked player a number of handicap
stones equal to the different in their ranks. 

In some tournaments, the number of handicap stones are further modified
(AGA City League, ACGA CGL). 

A players in a division is represented by a graph. Each player in the
division is represented by a node. The graph is initialized into a
clique. Each edge represent a possible game that can be played in the
tournament in this division. The division class also hold another graph
to represent the games that has been played, which will be empty
initially.

As each game has been play, the edge that represent that game in the
clique is severed, and the edge is added to the graph that represent the
games that has been played.
"""
