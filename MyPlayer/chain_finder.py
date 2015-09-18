import const

class ChainFinder():
    def _square_over_edge(self, edge, source_square, board):
        """
        get the square on the other side of an edge
        """
        two_squares = board.Edge2Squares[edge]
        if type(two_squares) is int:
            other_square = None
        else:
            for i in range(2):
                if two_squares[i] != source_square:
                    other_square = two_squares[i]
                    break

        return other_square

    
    def _get_traversable_squares(self, square, board):
        square_edges = board.Squares[square]
        unplayed_edges = []
        for edge in square_edges:
            if board.getEdgeState(edge) == const.UNPLAYED:
                unplayed_edges.append(edge)

        traversable_squares = []
        for unplayed_edge in unplayed_edges:
            other_square = self._square_over_edge(unplayed_edge, square, board)
            if other_square != None:
                traversable_squares.append(other_square)

        if len(traversable_squares) > 2:
            raise ValueError("The given square has not got enough played edges to be in a chain")

        return self._filter_edge_count(traversable_squares, board)


    def _filter_edge_count(self, squares, board):
        filtered_squares = []
        for square in squares:
            played_count = 0
            for edge in board.Squares[square]:
                if board.getEdgeState(edge) == const.PLAYED:
                    played_count += 1
            if played_count >= 2:
                filtered_squares.append(square)

        return filtered_squares


    def _filter_in_chain(self, squares, chain):
        filtered_squares = []
        for square in squares:
            if square not in chain:
                filtered_squares.append(square)

        return filtered_squares


    def _move(self, chain, board):
        possible_moves = self._filter_in_chain(self._get_traversable_squares(chain[-1], board), chain)
        no_of_possible = len(possible_moves)

        if no_of_possible == 0:
            return chain
        else:
            chain.append(possible_moves[0])
            return self._move(chain, board)


    def traverse(self, square, board):
        growing_chain = [square]
        traversable_squares = self._get_traversable_squares(square, board)
        no_of_traversable = len(traversable_squares)

        if no_of_traversable == 0:
            return [square]
        elif no_of_traversable == 1:
            growing_chain.append(traversable_squares[0])
            return self._move(growing_chain, board)
        else:
            growing_chain.append(traversable_squares[0])
            first_chain = self._move(growing_chain, board)
            growing_chain.append(traversable_squares[1])
            second_chain = self._move(growing_chain, board)
            first_chain.append(square)
            return first_chain + second_chain