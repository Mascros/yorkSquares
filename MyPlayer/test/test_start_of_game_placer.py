import unittest
import const
from start_of_game_placer import StartOfGamePlacer
placer = StartOfGamePlacer()


class TestGetMove(unittest.TestCase):
    def test_no_block(self):
        """
        should return each edge const.STARTERS, in order, if the opponent has not played any of those edges or any edges preventing us from doing so without giving the opponent a square
        """
        # Convert to list so we can use .remove()
        unplayed = list(range(72))
        
        # Get rid of some random non starter edges
        unplayed.remove(1)
        unplayed.remove(12)
        unplayed.remove(50)

        # Check it returns the right ones
        for edge in const.STARTERS:
            result = placer.get_move(unplayed)
            unplayed.remove(result)
            self.assertEqual(edge, result)


    @unittest.skip("Not Started")
    def test_help(self):
        """
        should return edges in const.STARTERS, in order, skipping those the opponent has placed for us
        """
        pass


    @unittest.skip("Not Started")
    def test_combo(self):
        """
        should return as many edges as possible from const.STARTERS, in order, missing those which would let the opponent create a square, skipping those that the opponent has placed for us
        """
        pass


    @unittest.skip("Not Started")
    def test_end(self):
        """
        should return None when all of const.STARTERS have been places, or can no longer be placed
        """
        pass


    @unittest.skip("Not Started")
    def test_block(self):
        """
        should return as many edges as possible from const.STARTERS, in order, missing those which would let the opponent create a square
        """
        pass


    @unittest.skip("Not Started")
    def test_never_returns_played(self):
        """
        should never return an edge which has already been played
        """
        pass
