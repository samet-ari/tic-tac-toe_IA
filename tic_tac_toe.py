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
    print(f"\t  {values[0]}  |  {values[1]}  |  {values[2]}")
    print("\t_____|_____|_____       1 | 2 | 3 ")
    print("\t     |     |          -------------")
    print(f"\t  {values[3]}  |  {values[4]}  |  {values[5]}         4 | 5 | 6 ")
    print("\t_____|_____|_____     -------------")
    print("\t     |     |            7 | 8 | 9 ")
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
def check_win(player_positions, current_player):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],    # rows 
        [1, 4, 7], [2, 5, 8], [3, 6, 9],   # columns
        [1, 5, 9], [3, 5, 7]               # diagonals
    ]
# Loop to check if any winning combination is satisfied   
    for winning_possibility in win_conditions:
        if all(position in player_positions[current_player] for position in winning_possibility): 
            return True    
    return False  

# Function to check if the game is a draw
def check_draw(player_positions):
    if len(player_positions['X']) + len(player_positions['O']) == 9: # If all the 'values" filled with "X" or "O"
        return True
    return False       

 
# Function for a single game of Tic Tac Toe
def single_game(current_player):
 
    # Initialize 'board' values
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_positions = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
         
        # Try exception block for MOVE input
        try:
            print("Player ", current_player, " turn. Choose a square : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Type a number")
            continue
 
        # Check if MOVE input in correct
        if move < 1 or move > 9:
            print("Wrong Input!!! the number must be between 1 and 9")
            continue
 
        # Check if the box is not occupied already. values are in range(9): 0 to 8 
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        # Update game information:
 
        # Updating grid status with the new input
        values[move-1] = current_player
 
        # Updating player positions add latest move to the list for this sign
        player_positions[current_player].append(move)
 
        # Function call for checking win
        if check_win(player_positions, current_player):
            print_tic_tac_toe(values)
            print("Player ", current_player, " has won the game!!")     
            print("\n")
            return current_player
 
        # Function call for checking draw game
        if check_draw(player_positions):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        # Switch player moves
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


# main
if __name__ == "__main__": # the game will only run if tic_tac_toe.py is lanched by itself, not if it's run through another file (imported)

    print("Player 1")
    player1 = input("Enter your name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter your name : ")
    print("\n")
     
    # Stores the player who chooses X and O
    current_player = player1
 
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
        print("Turn to choose for", current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Enter number '1', '2' or '3'\n")
            continue
 
        # Conditions for player choice  
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Input!!! Enter number '1', '2' or '3'\n")
 
        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])
         
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1








