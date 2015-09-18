import unittest
import const
from game_board import GameBoardADT
from placer import Placer

placer = Placer()
board = GameBoardADT()

class TestCheckSafe(unittest.TestCase):

    def test_when_safe_simple(self):
        """
        should return safe when placing an edge would not give anyone a square
        """
        # Check with 0,0 1,0 0,1 and 1,1 edges on each side
        # Also check when one side is not part of the board
        # so 0,0 means the squares on both sides of the edge have no edges

        # 0 Left & Right
        # Don't Need to set any edges
        self.assertEqual(placer.check_safe(9, board), True)

        # 0 Top & Bottom
        # Dont need to set any edges
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


    @unittest.skip("Not implemented")
    def test_when_safe_gain(self):
        # We get a chain
        # We get a chain they get one square
        # We get a chain they get a shorter chain
        # We get a chain they get an equal chain
        pass


    @unittest.skip("Not implemented")
    def test_when_unsafe_simple(self):
        # Also check when one side is not part of the board
        # Check with 2 edges on one side (for both sides) and 2 edges on both sides
        # also check for chains
        pass


    @unittest.skip("Not implemented")
    def test_when_unsafe_gain(self):
        # We get nothing they get one
        # We get one they get a chain
        # We get a chain they get a bigger chain
        pass


# Should check to see if there are any free sqaures available for taking safely
# Remember to prioritise taking chains over 2 squares (double cross) over 1 square
class TestFreeSquare(unittest.TestCase):
    @unittest.skip("Not implemented")
    def test_something(self):
        pass
        