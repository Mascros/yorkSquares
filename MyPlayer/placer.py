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
                return False
        else:
            for adj_square in adj_squares:
                if self._get_square_no_of_played(adj_square, board) == 2:
                    return False
            return True


    def get_free_squares(self, board):
        free_squares = []
        for square in board.Squares:
            played_count = 0
            for edge in board.Squares[square]:
                if board.getEdgeState(edge) == const.PLAYED:
                    played_count += 1
            if played_count == 3:
                free_squares.append(square)

        return free_squares
