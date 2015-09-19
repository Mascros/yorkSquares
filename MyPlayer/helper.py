import const

def edge_setter(edges, state, board):
    for edge in edges:
        board.setEdgeState(edge, state)


def unplay_all(board):
    for edge in range(72):
        board.setEdgeState(edge, const.UNPLAYED)