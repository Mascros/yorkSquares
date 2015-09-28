import unittest
import const
from chain_finder import ChainFinder
from game_board import GameBoardADT
from helper import edge_setter, unplay_all

board = GameBoardADT()
finder = ChainFinder()


class TestCombine(unittest.TestCase):
    def test_overlap(self):
        """
        if an edge chain and a middle chain overlap it should return the chain, in order, with no duplicates
        """
        # in order just means from one square to another, can be reversed
        unplay_all(board)

        # Overlap of 2 squares
        chains = [[1,10,19,27],[20,28,34,33,27,19]]
        edges = (1,9,26,27,42,43,52,53)
        edge_setter(edges, const.PLAYED, board)

        result = finder._combine(chains, board)

        if result[0] == 20:
            result.reverse()

        self.assertEqual(result, [1,10,19,27,33,34,28,20])


    def test_normal(self):
        """
        if an edge chain and a middle chain start and finish on either side of an edge return the chain in order
        """
        unplay_all(board)

        chains = [[12,13],[14,15]]
        edges = (20,21,22,23,39,40)
        edge_setter(edges, const.PLAYED, board)

        result = finder._combine(chains, board)

        if result[0] == 15:
            result.reverse()

        self.assertEqual(result, [12,13,14,15])
        

    @unittest.skip("Move to test get_combined, ")
    def test_more_than_two(self):
        """
        should try to combine again because chains might have to be combined more than once
        """
        # keep on trying to combine until no more combinations are possible
        pass