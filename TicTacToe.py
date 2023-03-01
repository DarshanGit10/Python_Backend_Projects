#Method to print Board
def print_ttt(values):
    print("\n")
    print("___ ___ ___")
    print("   |   |")
    print(" {} | {} | {}".format(values[0], values[1], values[2]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(values[3], values[4], values[5]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(values[6], values[7], values[8]))
    print("___|___|___")
    print("\n")

#Method for Score Board 
def print_ScoreBoard(score_board):
    print("---------Score Board----------")
    players = list(score_board.keys())
    print(players[0], score_board[players[0]])
    print(players[1], score_board[players[1]])
    print("------------------------------")

#Method to check if any player has won the game 
def check_winner(player_position, current_player):
    #Winning Combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]
    
    for x in soln:
        if all(y in player_position[current_player] for y in x):
            return True
    return False

#Method to check if game is a draw
def check_draw(player_position):
    if len(player_position['x']) + len(player_position['o']) == 9:
        return True
    return False

#Method for a single Game
def single_game(current_player):
    values = [' ' for x in range(9)]
    player_position = {'x': [], 'o': []} #To store the positions
    while True:
        print_ttt(values)

        try:
            print("Player ", current_player, "turn. Which box? : ", end='')
            move = int(input())
        except ValueError:
            print("Wrong Input!!!", ValueError)

        if move < 1 or move > 9:
            print("Please enter a number between 1 to 9 !")
            continue

        if values[move-1] != ' ':
            print("Place you chosen is already filled. Try again!!")
            continue

        #Update game status

        values[move-1] = current_player #Updating Board Status
        player_position[current_player].append(move) #Upadating player position 

        #Method call to check the winner
        if check_winner(player_position, current_player):
            print_ttt(values)
            print("Player ", current_player, " has won the game!!")
            print('\n')
            return current_player
        #Check for draw
        if check_draw(player_position):
            print_ttt(values)
            print("Match Draw!!!")
            print('\n')
            return 'D'

        #Switch player moves
        if current_player == 'x': current_player = 'o'
        else: current_player = 'x'

if __name__ == "__main__":

    print("Player 1 Details")
    play1 = input("Enter the name of the player: ")
    print('\n')

    print("Player 2 Details")
    play2 = input("Enter the name of the player: ")
    print('\n')

    current_player = play1 #chooses x or o
    player_choice = {'x' : "", 'o' : ""} #Store the values
    options = ['x', 'o']

    score_board = {play1: 0, play2: 0}
    print_ScoreBoard(score_board)

    while True:
        print("Turn to choose for", current_player)
        print("Enter 1 for x")
        print("Enter 2 for o")
        print("Enter 3 for quit")

        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!!", ValueError)

        if choice == 1:
            player_choice['x'] = current_player
            if current_player == play1: player_choice['o'] = play2
            else: player_choice['o'] = play1
        elif choice == 2:
            player_choice['o'] = current_player
            if current_player == play1: player_choice['x'] = play2
            else: player_choice['x'] = play1
        elif choice == 3:
            print("Final Score")
            print_ScoreBoard(score_board)
            break
        else: 
            print("Wrong Choice")


        winner = single_game(options[choice-1]) #Stores the winner in a single game 
    
        #Score Board edits according to the winner
        if winner != 'D':
            player_won  = player_choice[winner]
            score_board[player_won] = 1 + score_board[player_won]
        
        print_ScoreBoard(score_board)

        #switch players
        if current_player == play1: current_player = play2
        else: current_player = play2