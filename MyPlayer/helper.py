def edge_setter(edges, state, board):
    for edge in edges:
        board.setEdgeState(edge, state)