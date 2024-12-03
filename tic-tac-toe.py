values = [' ' for x in range(9)]
"""
This is the function to print the Tic Tac Toe game board.
It also shows the game board next to it with the numbers. 
This allow the player to see where their symbol will be.

"""
# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    # print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print(f"\t  {values[0]}  |  {values[1]}  |  {values[2]}")
    print("\t_____|_____|_____       1 | 2 | 3 ")
    print("\t     |     |          -------------")
    # print("\t  {}  |  {}  |  {}         4 | 5 | 6 ".format(values[3], values[4], values[5]))
    print(f"\t  {values[3]}  |  {values[4]}  |  {values[5]}         4 | 5 | 6 ")
    print("\t_____|_____|_____     -------------")
    print("\t     |     |            7 | 8 | 9 ")
    # print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print(f"\t  {values[6]}  |  {values[7]}  |  {values[8]}")
    print("\t     |     |")
    print("\n")


# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
 
# Function to check if any player has won
# def check_win(player_pos, cur_player):
 
 
# Function to check if the game is drawn
# def check_draw(player_pos):
  
 
# Function for a single game of Tic Tac Toe
# def single_game(cur_player):


 

# main
if __name__ == "__main__":

    print_tic_tac_toe(values)
