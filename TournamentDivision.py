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

import networkx as nx
from GoPlayer import Player
from GoMatch import Match
from pprint import pprint
from fake_player_data import player_list
from random import choice

import unittest

G = nx.Graph()

G.add_nodes_from(player_list)

class Division(object):
    """Division Class

    It holds all the players in the division, and all the possible
    matches that has been played by players of this division and can be
    played by players of this division
    """

    def __init__(self, player_list=[]):
        self.players= nx.Graph()
        self.possible_matches = nx.Graph()
        self.played_matches = nx.Graph()

        if player_list:
            if len(player_list) % 2 == 1:
                """Add a player to represent a "by"

                Since there is an odd number of players, go is played
                between 2 people.
                """

                player_list.append(Player())

            player_dict = dict(enumerate(player_list))

            self.players.add_nodes_from(player_list)
            
            for player in self.players:
                for other_player in self.players:
                    if player != other_player:
                        self.possible_matches.add_edge(player,
                                                       other_player)

########################################################################

class DivisionTest(unittest.TestCase):

    def setUp(self):
        """Create a clique graph for players in the division"""

        self.division_graph = nx.Graph()
        self.division_graph.add_nodes_from(player_list)
        
        for i in range(len(player_list)):
            for j in range(i + 1, len(player_list)):
                self.division_graph.add_edge(player_list[i], player_list[j],
                object=Match(player_list[i], player_list[j]))
    
    def test_unittest_setUp(self):
        self.assertTrue(len(self.division_graph.nodes()) == len(player_list))
        self.assertTrue(len(self.division_graph.edges()) ==
                        sum(range(len(player_list))))

    def test_start_up(self):
        a_division = Division(player_list)

if __name__ == "__main__":
    unittest.main()
