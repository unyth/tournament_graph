"""
This is the Match class for the tournament graph. It's the payload for
the edges in the graph. Each match must have 2 players (rengo and other
exotic go variations are not considered at this point). 

Following the convention, if the tournament is not an "open" tournament,
where people belonging to the same division play evenly, the player with
the higher rating/ranking takes white.

In addition to which player takes white, and which player takes black,
other information recorded by the Match class include the number of
handicap stones that were used, komi, type of match (open/handicapped).

Finally, the Match class will record the result of the match, who won,
in what way (win by x points, resignation, time), 

The game is assumed to be played in U.S., and under AGA ruling.

"""

from fake_player_data import player_list
from random import choice
from copy import copy

from GoPlayer import Player
import unittest

class AlteringResultErrorion(Exception):
    pass

class Match(object):
    """This is the Match class.

    This class hold the relevant information about a go match."""
    
    def __init__(self, player_1, player_2=Player(), match_type="open"):
        """Initializing a match, optional before or after play

        komi is set to 7.5 by default due to AGA's Concise rule of go
        document (http://www.usgo.org/files/pdf/conciserules.pdf)."""

        assert (isinstance(player_1, Player) and 
                isinstance(player_2, Player))

        self.match_type = match_type

        if match_type != "open":
            if player_1.rating > player_2.rating:
                self.w_player = player_1
                self.b_player = player_2
            else:
                self.w_player = player_2
                self.b_player = player_1
            
            self.handi = self.w_player.rating - self.b_player.rating

        else:
            players = [player_1, player_2]

            self.w_player = choice(players)
            players.remove(self.w_player)
            self.b_player = players[0]
            
            self.handi = 0

        if self.handi != 0:
            self.komi = 0.5
        else:
            self.handi = 7.5
        
        self.result = "unplayed"
    
    def update_result(self, result):
        """The proper way to update the game result
        
        The game can only have one result, will raise exception when
        trying to change more than once.
        """
        if self.result == "unplayed" and result != "unplayed":
            self.result = result
        else:
            raise AlteringResultErrorion

    def set_result(self, result):
        """When the result must be changed, due to initial error."""

        self.result = result

    def __eq__(self, other):
        return (self.w_player == other.w_player and 
                self.b_player == other.b_player and
                self.match_type == other.match_type)

class MatchTestCase(unittest.TestCase):

    def setUp(self):
        self.player_list = sorted(player_list)

    def test_player_assignment_handi(self):
        self.match = Match(self.player_list[0], self.player_list[1],
                           match_type="handi")
        self.assertTrue(self.match.w_player == self.player_list[1] and
                        self.match.b_player == self.player_list[0])

    def test_player_assignment_open(self):
        as_black = 0
        as_white = 0
        for x in range(100):
            self.match = Match(player_list[2], player_list[3],
                           match_type="open")
            if self.match.w_player == player_list[2]:
                as_white += 1
            else:
                as_black += 1
        self.assertTrue(as_black > 0)
        self.assertTrue(as_white > 0)

    def test_result_assignment(self):
        self.match = Match(player_list[4], player_list[5])
        a_result = "White win by resignation"
        self.match.set_result(a_result)
        self.assertTrue(self.match.result == a_result)

    def test_update_result(self):
        self.match = Match(player_list[6], player_list[7])
        a_result = "White win by resignation"
        self.match.update_result(a_result)
        another_result = "Black win by 4.5 pt"
        with self.assertRaises(AlteringResultErrorion):
            self.match.update_result(another_result)

    def test_equality(self):
        self.match1 = Match(player_list[8], player_list[9])
        self.match2 = copy(self.match1)
        self.assertTrue(self.match1 == self.match2)

if __name__ == "__main__":
    unittest.main()
