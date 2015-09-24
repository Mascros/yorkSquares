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

            # If its a loop chain, the second traversable square will already have been found
            if traversable_squares[1] not in growing_chain:  
                growing_chain.append(traversable_squares[1])
                second_chain = self._move(growing_chain, board)
                
            return growing_chain


    def find_all(self, board):
        chains = []
        for square in board.Squares:
            played_count = 0
            for edge in board.Squares[square]:
                if board.getEdgeState(edge) == const.PLAYED:
                    played_count += 1

            if played_count == 2 or played_count == 3:
                in_a_chain = False
                for chain in chains:
                    if square in chain:
                        in_a_chain = True
                        break

                if not in_a_chain:
                    chains.append(self.traverse(square, board))

        return chains


    def _straight_in_chain(self, square, board):
        for edge in board.Squares[square]:
            if edge in const.STARTERS:
                if board.getEdgeState(edge) == const.PLAYED:
                    return True

        return False


    def _intruding_in_chain(self, square, board):
        played_count = 0
        for edge in board.Squares[square]:
            if edge in const.STARTERS:
                if board.getEdgeState(edge) == const.PLAYED:
                    played_count += 1

        if played_count == 2:
            return True
        else: 
            return False


    def _extruding_in_chain(self, square, board):
        for edge in board.Squares[square]:
            two_squares = board.Edge2Squares[edge]
            if type(two_squares) is tuple:
                for two_square in two_squares:
                    if two_square != square:
                        if const.EDGE_CHAIN[two_square] == const.STRAIGHT:
                            return self._straight_in_chain(two_square, board)
                        elif const.EDGE_CHAIN[two_square] == const.INTRUDING:
                            return self._intruding_in_chain(two_square, board)
        


    def find_edge_chains(self, board):
        chains = []
        current_chain = []

        # points to the index in EDGE_CHAIN.keys() which holds the current square 
        square_pointer = 0

        for square in const.EDGE_SQUARES:
            if const.EDGE_CHAIN[square] == const.STRAIGHT:
                if self._straight_in_chain(square, board):
                    current_chain.append(square)
                elif len(current_chain) > 0:
                    chains.append(current_chain)
                    current_chain = []
            elif const.EDGE_CHAIN[square] == const.INTRUDING:
                if self._intruding_in_chain(square, board):
                    current_chain.append(square)
                elif len(current_chain) > 0:
                    chains.append(current_chain)
                    current_chain = []
            else:
                # Must be extruding
                if self._extruding_in_chain(square, board):
                    current_chain.append(square)
                elif len(current_chain) > 0:
                    chains.append(current_chain)
                    current_chain = []

            if square_pointer == 27:
                next_square = list(const.EDGE_SQUARES)[0]
            else:
                next_square = list(const.EDGE_SQUARES)[square_pointer + 1]

            if len(current_chain) > 0:
                for edge in board.Squares[square]:
                    two_squares = board.Edge2Squares[edge]
                    if type(two_squares) is tuple:
                        for two_square in two_squares:
                            if two_square == next_square:
                                if board.getEdgeState(edge) == const.PLAYED:
                                    chains.append(current_chain)
                                    current_chain = []

            square_pointer += 1

        if len(current_chain) > 0:
            chains.append(current_chain)

        # if the first chain startes with square 0 and the last chain ends with 9 then and edge 17 is unplayed join them into one chain
        if chains[0][0] == 0 and chains[-1][-1] == 9 and board.getEdgeState(17) == const.UNPLAYED and len(chains) > 1:
            chains[-1].extend(chains[0])
            chains.pop(0)

        return chains
