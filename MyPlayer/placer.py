import const
from chain_finder import ChainFinder


finder = ChainFinder()


class Placer():
    def _get_square_no_of_played(self, square, board):
        played_count = 0
        for edge in board.Squares[square]:
            if board.getEdgeState(edge) == const.PLAYED:
                played_count += 1

        return played_count


    def check_safe(self, edge, board):
        adj_squares = board.Edge2Squares[edge]
        played_count = 0
        if type(adj_squares) is int:
            if self._get_square_no_of_played(adj_squares, board) < 2:
                return True
        else:
            for adj_square in adj_squares:
                if self._get_square_no_of_played(adj_square, board) > 2:
                    return False
            return True
