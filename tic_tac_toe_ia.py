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
def check_win(player_pos, cur_player):

    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):

            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False

# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False

# Function for a single game of Tic Tac Toe
def single_game(cur_player, is_ai):

    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)

        if cur_player == 'O' and is_ai:
            move = ai_move(values, 'O', 'X')
        else:
            # Try exception block for MOVE input
            try:
                print("Player ", cur_player, " turn. Which box? : ", end="")
                move = int(input())
            except ValueError:
                print("Wrong Input!!! Enter a number")
                continue

        # Sanity check for MOVE input
        if move < 1 or move > 9:
            print("Wrong Input!!! The number must be between 1 and 9")
            continue

        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue

        # Update game information

        # Updating grid status
        values[move-1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")
            print("\n")
            return cur_player


        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("It's a Draw!")
            print("\n")
            return 'D'
        # Switch player moves
        cur_player = 'O' if cur_player == 'X' else 'X'

# Minimax algorithm for AI
def ai_move(values, ai_player, human_player):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if values[i] == ' ':
            values[i] = ai_player
            score = minimax(values, 0, False, ai_player, human_player)
            values[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i + 1
    return best_move

def minimax(values, depth, is_maximizing, ai_player, human_player ):
    if check_win({'X': [i+1 for i, x in enumerate(values) if x == 'X'], 'O': [i+1 for i, x in enumerate(values) if x == 'O']}, ai_player):
        return 1
    if check_win({'X': [i+1 for i, x in enumerate(values) if x == 'X'], 'O': [i+1 for i, x in enumerate(values) if x == 'O']}, human_player):
        return -1
    if check_draw({'X': [i+1 for i, x in enumerate(values) if x == 'X'], 'O': [i+1 for i, x in enumerate(values) if x == 'O']}):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if values[i] == ' ':
                values[i] = ai_player
                score = minimax(values, depth + 1, False, ai_player, human_player)
                values[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if values[i] == ' ':
                values[i] = human_player
                score = minimax(values, depth + 1, True, ai_player, human_player)
                values[i] = ' '
                best_score = min(score, best_score)
        return best_score

if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")

    print("Player 2 : AI")
    player2 = "AI"
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
        print("What do you want to do?")
        print("Enter 1 to play as X")
        print("Enter 2 to Quit")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Enter a number\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong Choice!!!! Type 1 or 2\n")

        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1], is_ai=True)

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
