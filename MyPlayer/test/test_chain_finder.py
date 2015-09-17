import unittest
import const
from game_board import GameBoardADT
from chain_finder import ChainFinder
from helper import edge_setter


finder = ChainFinder()
board = GameBoardADT()



# N.B FOR A SQUARE TO BE IN A CHAIN, IT MUST HAVE    ------>     at least 2 OR MORE      <-----    EDGES PLAYED
 


# Traverse chain, given a starting square, until you cant anymore, return all the squares in the chain, including the one given
# If the square given has more than one unplayed edge it could be an edge count or lack of board end. In these cases check the squares on the other sides of both unplayed edges, if the one you checked is one of the formentioned ends, traverse with the other edge
class TestTraverse(unittest.TestCase):
    def test_single(self):
        """
        should return the square given, as a single square is just a chain of length one
        """
        # Set some random edges to played
        random_edges = (33, 59, 60, 70, 71)
        edge_setter(random_edges, const.PLAYED, board)

        # Board end, count end
        edge_setter((8,9), const.PLAYED, board)
        self.assertEqual(finder.traverse(0, board), board.Squares[0])
        edge_setter((8,9), const.UNPLAYED, board)

        # 3 end, board end
        edge_setter((43,48,58), const.PLAYED, board)
        self.assertEqual(finder.traverse(0, board), board.Squares[0])
        edge_setter((43,48,58), const.UNPLAYED, board)

        # Unset the random edges
        edge_setter(random_edges, const.UNPLAYED, board)


    def test_complex_chain(self):
        """
        should return all the squares in the chain, including the one given
        """
        # Set some random edges to played
        random_edges = (33, 59, 60, 70, 71)
        edge_setter(random_edges, const.PLAYED, board)

        # Test a very complex chain, traversing squares 19, 20, 11, 12, 13, 14, 23, 24, 15
        square_ids = (19, 20, 11, 12, 13, 14, 23, 24, 15)
        chain_edges = (35, 48, 49, 44, 27, 19, 37, 20, 21, 38, 22, 31, 45, 50, 51, 47, 31, 23)
        edge_setter(chain_edges, const.PLAYED, board)
        self.assertEqual(finder.traverse(19, board), square_ids)

        # Unset the random edges
        edge_setter(random_edges, const.UNPLAYED, board)


# Find all chains given a board (this one needs to find the start of the chain)
class TestFindAll(unittest.TestCase):
    @unittest.skip("Not implemented")
    def test_something(self):
        pass