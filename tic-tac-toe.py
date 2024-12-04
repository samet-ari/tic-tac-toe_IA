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
def check_win(player_position, current_player):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],    # rows 
        [1, 4, 7], [2, 5, 8], [3, 6, 9],   # columns
        [1, 5, 9], [3, 5, 7]               # diagonals
    ]
    
    for condition in win_conditions:
        if all(pos in player_position for pos in condition):
            return True
    return False









 
 
# Function to check if the game is drawn
# def check_draw(player_pos):
  






 
# Function for a single game of Tic Tac Toe
# def single_game(cur_player):


 







# main
if __name__ == "__main__":
    
    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
     
    # Stores the player who chooses X and O
    cur_player = player1
 
    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}
 
    # Stores the options
    options = ['X', 'O']
 
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
 
        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
 
        # Conditions for player choice  
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])
         
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
     
    # Stores the player who chooses X and O
    cur_player = player1
 
    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}
 
    # Stores the options
    options = ['X', 'O']
 
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
 
        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
 
        # Conditions for player choice  
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])
         
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

    print_tic_tac_toe(values)







