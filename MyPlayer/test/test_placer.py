import unittest
import const
from game_board import GameBoardADT
from placer import Placer
from helper import unplay_all, edge_setter


placer = Placer()
board = GameBoardADT()


class TestGetSquareNoOfPlayed(unittest.TestCase):
    def test_with_zero(self):
        """
        should return 0 when the given square has 0 played edges
        """
        unplay_all(board)
        self.assertEqual(placer._get_square_no_of_played(5, board), 0)


    def test_with_one(self):
        """
        should return 1 when the given square has 1 played edges
        """
        unplay_all(board)
        board.setEdgeState(13, const.PLAYED)
        self.assertEqual(placer._get_square_no_of_played(5, board), 1)


    def test_with_two(self):
        """
        should return 2 when the given square has 2 played edges
        """
        unplay_all(board)
        board.setEdgeState(13, const.PLAYED)
        board.setEdgeState(14, const.PLAYED)
        self.assertEqual(placer._get_square_no_of_played(5, board), 2)


    def test_with_three(self):
        """
        should return 3 when the given square has 3 played edges
        """
        unplay_all(board)
        board.setEdgeState(13, const.PLAYED)
        board.setEdgeState(14, const.PLAYED)
        board.setEdgeState(22, const.PLAYED)
        self.assertEqual(placer._get_square_no_of_played(5, board), 3)


    def test_with_four(self):
        """
        should return 4 when the given square has 4 played edges
        """
        unplay_all(board)
        board.setEdgeState(13, const.PLAYED)
        board.setEdgeState(14, const.PLAYED)
        board.setEdgeState(22, const.PLAYED)
        board.setEdgeState(5, const.PLAYED)
        self.assertEqual(placer._get_square_no_of_played(5, board), 4)


class TestCheckSafe(unittest.TestCase):
    def test_when_safe(self):
        """
        should return safe when placing an edge would not give the opponent a square
        """
        unplay_all(board)

        # 0 Left & Right
        self.assertEqual(placer.check_safe(9, board), True)

        # 0 Top & Bottom
        self.assertEqual(placer.check_safe(18, board), True)

        # 1 Left Parralel 
        edge = 9
        board.setEdgeState(edge, const.PLAYED)
        self.assertEqual(placer.check_safe(10, board), True)
        board.setEdgeState(edge, const.UNPLAYED)

        # 1 Left Top 
        edge = 1
        board.setEdgeState(edge, const.PLAYED)
        self.assertEqual(placer.check_safe(10, board), True)
        board.setEdgeState(edge, const.UNPLAYED)

        # 1 Left Bottom 
        edge = 1
        board.setEdgeState(edge, const.PLAYED)
        self.assertEqual(placer.check_safe(10, board), True)
        board.setEdgeState(edge, const.UNPLAYED)

        # 1 Right Parralel 
        edge = 11
        board.setEdgeState(edge, const.PLAYED)
        self.assertEqual(placer.check_safe(10, board), True)
        board.setEdgeState(edge, const.UNPLAYED)

        # 1 Right Top 
        edge = 2
        board.setEdgeState(edge, const.PLAYED)
        self.assertEqual(placer.check_safe(10, board), True)
        board.setEdgeState(edge, const.UNPLAYED)

        # 1 Right Bottom 
        edge = 19
        board.setEdgeState(edge, const.PLAYED)
        self.assertEqual(placer.check_safe(10, board), True)
        board.setEdgeState(edge, const.UNPLAYED)

        # 1 Top Left & 1 Bottom Parralel
        edge1 = 30
        edge2 = 50
        board.setEdgeState(edge1, const.PLAYED)
        board.setEdgeState(edge2, const.PLAYED)
        self.assertEqual(placer.check_safe(39, board), True)
        board.setEdgeState(edge1, const.UNPLAYED)
        board.setEdgeState(edge2, const.UNPLAYED)

        # 1 Top Parralel & 1 Bottom Right
        edge1 = 22
        edge2 = 46
        board.setEdgeState(edge1, const.PLAYED)
        board.setEdgeState(edge2, const.PLAYED)
        self.assertEqual(placer.check_safe(39, board), True)
        board.setEdgeState(edge1, const.UNPLAYED)
        board.setEdgeState(edge2, const.UNPLAYED)
        
        # Top no square bottom parralel 
        edge = 10
        board.setEdgeState(edge, const.PLAYED)
        self.assertEqual(placer.check_safe(1, board), True)
        board.setEdgeState(edge, const.UNPLAYED)

        # Left no square right top
        edge = 0
        board.setEdgeState(edge, const.PLAYED)
        self.assertEqual(placer.check_safe(8, board), True)
        board.setEdgeState(edge, const.UNPLAYED)


    def test_when_unsafe(self):
        """
        should return unsafe when placing an edge would give the opponent a square
        """
        unplay_all(board)

        edge1 = 30
        edge2 = 22
        edge3 = 50
        board.setEdgeState(edge1, const.PLAYED)
        board.setEdgeState(edge2, const.PLAYED)
        board.setEdgeState(edge3, const.PLAYED)
        self.assertEqual(placer.check_safe(39, board), False)
        board.setEdgeState(edge1, const.UNPLAYED)
        board.setEdgeState(edge2, const.UNPLAYED)
        board.setEdgeState(edge3, const.UNPLAYED)

        edge1 = 30
        edge2 = 22
        edge3 = 32
        board.setEdgeState(edge1, const.PLAYED)
        board.setEdgeState(edge2, const.PLAYED)
        board.setEdgeState(edge3, const.PLAYED)
        self.assertEqual(placer.check_safe(31, board), False)
        board.setEdgeState(edge1, const.UNPLAYED)
        board.setEdgeState(edge2, const.UNPLAYED)
        board.setEdgeState(edge3, const.UNPLAYED)

        edge1 = 32
        edge2 = 24
        board.setEdgeState(edge1, const.PLAYED)
        board.setEdgeState(edge2, const.PLAYED)
        self.assertEqual(placer.check_safe(33, board), False)
        board.setEdgeState(edge1, const.UNPLAYED)
        board.setEdgeState(edge2, const.UNPLAYED)


        edge1 = 30
        edge2 = 22
        edge3 = 32
        edge4 = 23
        board.setEdgeState(edge1, const.PLAYED)
        board.setEdgeState(edge2, const.PLAYED)
        board.setEdgeState(edge3, const.PLAYED)
        board.setEdgeState(edge4, const.PLAYED)
        self.assertEqual(placer.check_safe(31, board), False)
        board.setEdgeState(edge1, const.UNPLAYED)
        board.setEdgeState(edge2, const.UNPLAYED)
        board.setEdgeState(edge3, const.UNPLAYED)
        board.setEdgeState(edge4, const.UNPLAYED)


# Should check to see if there are any free sqaures available for taking safely
# Remember to prioritise taking chains over 2 squares (double cross) over 1 square
class TestGetFreeSquares(unittest.TestCase):
    def test_none(self):
        """
        should return [] when there are no free sqaures
        """
        unplay_all(board)

        edges = (0,1,19,12,31,40,71,66,61,67)
        edge_setter(edges, const.PLAYED, board)

        self.assertEqual(placer.get_free_squares(board), [])




    def test_one(self):
        """
        should return the free square in an array (for consistancey)
        """
        unplay_all(board)

        edges = (0,1,19,12,31,40,71,66,61,67,56,57)
        edge_setter(edges, const.PLAYED, board)

        self.assertEqual(placer.get_free_squares(board), [31])


    def test_many(self):
        """
        should return all the free squares
        """
        unplay_all(board)

        edges = (0,1,19,12,31,40,71,66,61,67,56,57,62,58,63,52,53)
        edge_setter(edges, const.PLAYED, board)

        free_squares = placer.get_free_squares(board)

        self.assertIn(27, free_squares)
        self.assertIn(33, free_squares)
        self.assertIn(31, free_squares)
        self.assertNotIn(37, free_squares)