import unittest
import const


class TestGetMove(unittest.TestCase):
    def test_no_block(self):
        """
        should return each edge const.STARTERS, in order, if the opponent has not played any of those edges or any edges preventing us from doing so without giving the opponent a square
        """
        # for edge in const.STARTERS:
        #     self.assertEqual(edge, <PUT get_move CALL HERE>)
        pass


    def test_help(self):
        """
        should return edges in const.STARTERS, in order, skipping those the opponent has placed for us
        """
        pass
        # get move could take a list of unplayed edges, we could fake this list to pretend the opponent has played one and check that it reacts accordingly


    def test_block(self):
        """
        should return as many edges as possible from const.STARTERS, in order, missing those which would let the opponent create a square
        """
        pass


    def test_combo(self):
        """
        should return as many edges as possible from const.STARTERS, in order, missing those which would let the opponent create a square, skipping those that the opponent has placed for us
        """
        pass


    def test_end(self):
        """
        should return None when all of const.STARTERS have been places, or can no longer be placed
        """
        pass


    def test_never_returns_played(self):
        """
        should never return an edge which has already been played
        """
        pass
