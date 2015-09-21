import unittest
import const
from start_of_game_placer import StartOfGamePlacer
from game_board import GameBoardADT
from helper import unplay_all, edge_setter

board = GameBoardADT()
placer = StartOfGamePlacer()


class TestGetMove(unittest.TestCase):
    def test_no_block(self):
        """
        should return each edge const.STARTERS, in order, if the opponent has not played any of those edges or any edges preventing us from doing so without giving the opponent a square
        """        
        unplay_all(board)

        random_edges = (1,12,50)
        edge_setter(random_edges, const.PLAYED, board)

        for edge in const.STARTERS:
            result = placer.get_move(board)
            board.setEdgeState(result, const.PLAYED)
            self.assertEqual(edge, result)


    def test_help(self):
        """
        should return edges in const.STARTERS, in order, skipping those the opponent has placed for us
        """
        unplay_all(board)
        
        edges = (1,12,50,20,31)
        edge_setter(edges, const.PLAYED, board)

        for edge in const.STARTERS:
            if edge not in edges:
                result = placer.get_move(board)
                board.setEdgeState(result, const.PLAYED)
                self.assertEqual(edge, result)


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
