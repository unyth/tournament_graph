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

from GoPlayer import Player
import unittest

class Match(object):
    """This is the Match class.

    This class hold the relevant information about a go match."""
    
    def __init__(self, player_1, player_2=Player(), match_type="open"):
        """Initializing a match, optional before or after play

        komi is set to 7.5 by default due to AGA's Concise rule of go
        document (http://www.usgo.org/files/pdf/conciserules.pdf)."""

        assert (isinstance(player_1, Player) and 
                isinstance(player_2, Player))

        if match_type != "open":
            if player_1.rating > player_2.rating:
                self.w_player = player_1
                self.b_player = player_2
            else:
                self.w_player = player_2
                self.b_player = player_1
        else:
            players = [player_1, player_2]

            self.w_player = choice(players)
            players.pop(self.w_player)
            self.b_player = players[0]

        self.match_type = match_type

        if match_type != "open":
            self.handi = player.w_player.rating - player.b_player.rating

        if self.handi != 0:
            self.komi = 0.5
        
        self.result = "unplayed"
    
    def update_result(self, result):
        if self.result == "unplayed" and result != "unplayed":
            self.result = result

    def set_result(self, result):
        self.result = result



class MatchTestCase(unittest.TestCase):

    def setUp(self):
        self.player_list = sorted(player_list)

    def test_player_assignment_handi(self):
        self.match = Match(player_list[0], player_list[1],
                           match_type="handi")
        self.assertTrue(self.match.w_player == player_list[1] and
                        self.match.b_player == player_list[0])

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

if __name__ == "__main__":
    unittest.main()
