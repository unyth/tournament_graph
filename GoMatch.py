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
"""

from GoPlayer import Player
import unittest

class Match(object):
    """This is the Match class.

    This class hold the relevant information about a go match."""
    
    def __init__(self, w_player, b_player, result, 
                 match_type="open", handi=0, komi=7.5):
        """Initializing a match, optional before or after play

        komi is set to 7.5 by default due to AGA's Concise rule of go
        document (http://www.usgo.org/files/pdf/conciserules.pdf)."""

        assert isinstance(w_player, Player)
        assert isinstance(b_player, Player)

        self.w_player = w_player
        self.b_player = b_player
        self.match_type = match_type
        self.handi = handi
        self.komi = komi
        self.result = result
    



class MatchTestCase(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
