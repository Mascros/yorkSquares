'''
This module handles the game strategy (only) of a player.
'''

import random
import const
from game_board import GameBoardADT
from chain_finder import ChainFinder
from placer import Placer


# Enter your own player name
playerName = "Robin Stephenson"


# The game board
board = GameBoardADT()
finder = ChainFinder()
placer = Placer()

# This tells you which player you are, either const.PLAYER1 or const.PLAYER2
# It is set when the connection to the game server is made
# It may be useful if you want to know who occupies which square
myPlayerNumber = None


def chooseMove(state):
    """
    Should Decide what move to make based on current state of opponent's board and return it.
    Currently the strategy is completely random. It just chooses randomly from the list of unplayed edges.
    """
    global board
    global myPlayerNumber
    # Update your board to the current state:
    board.setGameState(state)
    # YOUR IMPROVED STRATEGY SHOULD GO HERE:

    unplayed = board.getUnplayedEdges()

    # Get all the chains
    chains = finder.find_all(board)
    
    # Sort the chains, longest to shortes length
    list_sorted = False
    while not list_sorted:
        list_sorted = True
        for i in range(len(chains)-1):
            if chains[i] < chains[i+1]:
                list_sorted = False
                temp = chains[i+1]
                chains[i+1] = chains[i]
                chains[i] = temp


    # Free squares are ones which have 3 edges, [] if no free squares
    free_squares = placer.get_free_squares(board)

    if len(free_squares) == 0:
        for edge in unplayed:
            if placer.check_safe(edge, board):
                return edge
        
        for chain in reversed(chains):
            for square in chain:
                for edge in board.Squares[square]:
                    if board.getEdgeState(edge) == const.UNPLAYED:
                        return edge

    else:
        for square in free_squares:
            for edge in board.Squares[square]:
                if board.getEdgeState(edge) == const.UNPLAYED:
                    return edge



    # Incase for some reason no move has been found
    print("CHOOSING A RANDOM MOVE")
    move = random.choice(unplayed)


def newGame():
    """
    This method is called when a new game is starting (new game with same player). This gives you the
    ability to update your strategy.
    Currently does nothing.
    """
    pass
