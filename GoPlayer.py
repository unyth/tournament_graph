"""
This is the base Player class to be used for representing players in the
tournament. It is assumed that the tournament will be held in the U.S.,
and under AGA rules.
"""

import unittest
from copy import copy


class Player(object):
    """Player Class that holds basic player information.

    Players needs to be unique, and be able to be sorted.

    The sort is based on player strength, which is measured by their AGA
    rating (higher is better). Two players with the same rating, will be
    ordered by their AGA ID (smaller is "better").
    """

    def __init__(self, name="by", aga_id=-1, aga_rating=-35):
        self.name = name
        self.id_num = aga_id
        self.rating = aga_rating

    def __str__(self):
        return ("<Player: %s, AGA ID: %i, AGA rating: %f>"
                % (self.name, self.id_num, self.rating))

    def __repr__(self):
        return ("Player(name='%s', aga_id=%i, aga_rating=%f)"
                % (self.name, self.id_num, self.rating))

    def __gt__(self, other):
        if self.rating > other.rating:
            return True
        elif self.rating == other.rating:
            return self.id_num < other.id_num

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.__repr__() == other.__repr__()
        else:
            return False

    def __hash__(self):
        return hash((self.name, self.id_num, self.rating))

########################################################################

# Unit tests for player class


class PlayerTest(unittest.TestCase):
    """PlayerTest class to get Player class"""

    def setUp(self):

        player0 = Player(name="Walther",
                         aga_id=12345,
                         aga_rating=4.90826)

        player1 = Player(name="Andrew",
                         aga_id=22345,
                         aga_rating=1.53764)

        player2 = Player(name="Milan",
                         aga_id=13346,
                         aga_rating=-5.45752)

        player3 = Player(name="Walther Clone",
                         aga_id=12346,
                         aga_rating=4.90826)

        player4 = copy(player0)

        self.player_list = [player0, player1, player2, player3, player4]

    def test_gt(self):
        """Test greater than relationship between 2 players"""

        self.assertTrue(self.player_list[0] > self.player_list[3])
        self.assertFalse(self.player_list[0] < self.player_list[3])

    def test_lt(self):
        """Test less than relationship between 2 players"""

        self.assertTrue(self.player_list[3] < self.player_list[0])
        self.assertFalse(self.player_list[3] > self.player_list[0])

    def test_eq(self):
        """Test equality relationship between 2 players"""

        self.assertTrue(self.player_list[1] == self.player_list[1])
        self.assertFalse(self.player_list[0] == self.player_list[3])

    def test_duplication(self):
        """Test to see if duplicates can be identified and eliminated"""

        player_set = set(self.player_list)
        self.assertIsInstance(player_set, set)
        self.assertEqual(len(player_set), 4)

    def test_proper_repr(self):
        """Test to see if __repr__ returns a proper python expression"""
        self.assertEqual(eval(repr(self.player_list[0])),
                         self.player_list[0])
        self.assertFalse(eval(repr(self.player_list[0])) is
                         self.player_list[0])

    def test_sorting(self):
        sorted_player_list = sorted(self.player_list)
        self.assertTrue(sorted_player_list[3] == self.player_list[4])

if __name__ == "__main__":
    unittest.main()
