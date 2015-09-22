UNCAPTURED = 0
UNPLAYED = 0
PLAYED = 1
PLAYER1 = 1
PLAYER2 = 2


############################################################
##
## User (Robin Stephenson) constants
##
############################################################
STRAIGHT = 0
INTRUDING = 1
EXTRUDING = 2
STARTERS = (18, 23, 53, 56, 27, 43, 19, 20, 21, 22, 31, 46)
EDGE_CHAIN = {0:EXTRUDING,1:STRAIGHT,2:STRAIGHT,3:STRAIGHT,4:STRAIGHT,5:STRAIGHT,6:STRAIGHT,
              7:EXTRUDING,16:EXTRUDING,15:INTRUDING,24:STRAIGHT,31:STRAIGHT,37:EXTRUDING,
              36:EXTRUDING,30:STRAIGHT,23:STRAIGHT,14:INTRUDING,13:STRAIGHT,12:STRAIGHT,
              11:INTRUDING,20:STRAIGHT,28:STRAIGHT,34:EXTRUDING,33:EXTRUDING,27:STRAIGHT,
              19:STRAIGHT,10:INTRUDING,9:EXTRUDING}


############################################################
##
## Constants used for the client/server functionalities
##
############################################################
# Constant containing the IP address of the server
GAME_SERVER_ADDR = ''   #meaning the server is on the local host. Comment if server is elsewhere and provide
                        # an address like the one below
# GAME_SERVER_ADDR = '10.240.74.225' 
 
# Port used for the socket communication. You must ensure the same port is used by the client & the server
# Note: another port number could be used
GAME_SERVER_PORT = 12345 

# Constant used in the communication to acknowledge a received message
# Typically this constant is used to synchronise the clients and the server
ACKNOWLEDGED = 'ACK'