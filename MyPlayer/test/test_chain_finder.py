import unittest
import const
from game_board import GameBoardADT
from chain_finder import ChainFinder
from helper import edge_setter


finder = ChainFinder()
board = GameBoardADT()


class TestTraverse(unittest.TestCase):
    def test_single(self):
        """
        should return a list of one square when the chain is one long
        """
        board.setEdgeState(66, const.PLAYED)
        board.setEdgeState(71, const.PLAYED)
        self.assertEqual([37], finder.traverse(37, board))
        board.setEdgeState(66, const.UNPLAYED)
        board.setEdgeState(71, const.UNPLAYED)


    def test_complex_chain_middle(self):
        """
        should return all the squares in the chain, including the one given, even when starting in the middle of the chain
        """
        # Set some random edges to played
        random_edges = (14, 33, 59, 60, 70, 71)
        edge_setter(random_edges, const.PLAYED, board)

        # Test a very complex chain, traversing squares 19, 20, 11, 12, 13, 14, 23, 24, 15
        square_ids = (19, 20, 11, 12, 13, 14, 23, 24, 15)
        chain_edges = (35, 48, 49, 44, 27, 19, 37, 20, 21, 38, 22, 31, 45, 50, 51, 47, 31, 23)
        edge_setter(chain_edges, const.PLAYED, board)
        
        traversal = finder.traverse(11, board)
        for square in square_ids:
            self.assertIn(square, traversal)

        edge_setter(chain_edges, const.UNPLAYED, board)

        # Unset the random edges
        edge_setter(random_edges, const.UNPLAYED, board)


    def test_complex_chain_end(self):
        """
        should return all the squares in the chain, including the one given
        """
        # Set some random edges to played
        random_edges = (14, 33, 59, 60, 70, 71)
        edge_setter(random_edges, const.PLAYED, board)

        # Test a very complex chain, traversing squares 19, 20, 11, 12, 13, 14, 23, 24, 15
        square_ids = (19, 20, 11, 12, 13, 14, 23, 24, 15)
        chain_edges = (35, 48, 49, 44, 27, 19, 37, 20, 21, 38, 22, 31, 45, 50, 51, 47, 31, 23)
        edge_setter(chain_edges, const.PLAYED, board)
        
        traversal = finder.traverse(15, board)
        for square in square_ids:
            self.assertIn(square, traversal)

        edge_setter(chain_edges, const.UNPLAYED, board)

        # Unset the random edges
        edge_setter(random_edges, const.UNPLAYED, board)


    def test_loop_chain_square(self):
        """
        should be able to return squares from a loop of a square chain
        """
        edges = (3, 4, 13, 30, 38, 37, 28, 11)
        squares = (3, 4, 12, 13)
        edge_setter(edges, const.PLAYED, board)
        traversal = finder.traverse(3, board)
        for square in squares:
            self.assertIn(square, traversal)

        edge_setter(edges, const.UNPLAYED, board)


    def test_loop_chain_rect(self):
        """
        should be able to return squares from a loop of a rectangular chain
        """
        # 3 x 2 rectangle, make sure edge count is always satisfied
        edges = (3, 4, 5, 14, 31, 39, 38, 37, 28, 11, 21)
        squares = (3, 4, 5, 14, 13, 12)
        edge_setter(edges, const.PLAYED, board)
        traversal = finder.traverse(3, board)
        for square in squares:
            self.assertIn(square, traversal)

        edge_setter(edges, const.UNPLAYED, board)


# Find all chains given a board
class TestFindAll(unittest.TestCase):
    @unittest.skip("Not implemented")
    def test_needs_writing(self):
        pass


class TestSquareOverEdge(unittest.TestCase):
    def test_left(self):
        """
        should return the square on the other side of the edge traversing left
        """
        self.assertEqual(finder._square_over_edge(9, 1, board), 0)
    

    def test_down(self):
        """
        should return the square on the other side of the edge traversing down
        """
        self.assertEqual(finder._square_over_edge(20, 3, board), 12)


    def test_edge(self):
        """
        should return None if there is no square on the other side
        """
        self.assertEqual(finder._square_over_edge(8, 0, board), None)


class TestGetTraversableSquares(unittest.TestCase):
    def test_needs_better_name(self):
        """
        should return the traversable edges of a square
        """
        # Square zero, edge 8 unplayed
        edges = (0,9,17)
        edge_setter(edges, const.PLAYED, board)
        self.assertEqual(finder._get_traversable_squares(0, board), [])
        
        # Square zero, edges 0,8,9 unplayed
        edges = (0,9)
        edge_setter(edges, const.UNPLAYED, board)
        result = finder._get_traversable_squares(0, board)
        self.assertEqual([1], result)
        board.setEdgeState(17, const.UNPLAYED)


class TestFilterEdgeCount(unittest.TestCase):
    def test_needs_better_name(self):
        """
        should return only squares which have 2 or more edges played
        """
        edges = (0, 1, 10, 2, 11)
        edge_setter(edges, const.PLAYED, board)

        squares = (0,1,2,3)
        filtered = finder._filter_edge_count(squares, board)
        self.assertNotIn(0, filtered)
        self.assertIn(1, filtered)
        self.assertIn(2, filtered)
        self.assertNotIn(3, filtered)


class TestFilterInChain(unittest.TestCase):
    def test_no_chain(self):
        """
        should return all the squares passed
        """
        squares = (5,14,15)
        result = finder._filter_in_chain(squares, [])
        for square in squares:
            self.assertIn(square, result)


    def test_chain(self):
        """
        should return all those passed, except those in the chain
        """
        squares = (5,14,15,20)
        chain = (12, 15, 6, 5)
        result = finder._filter_in_chain(squares, chain)
        self.assertIn(14, result)
        self.assertIn(20, result)
        self.assertNotIn(5, result)
        self.assertNotIn(15, result)
