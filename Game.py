def create_board(size): #Creates the game board
    dikt = {}
    for row in range (1,size+1): #Loops through the dictonary to create a grid
        for collum in range(1,size+1):
            dikt[row,collum] = "~"
    return dikt
def print_gameboard(gameboard): #prints the gameboard when the gameboard is passed in as input
    for row in range(1,6): 
        for collom in range(1,6):
            print(gameboard[row,collom],end="  ")
        print()
game_board = create_board(5) #hardcodes the gameboard size, maybe make it dynamic later
user_guess = input("Enter a guess to make: ")
user_row_guess = int(user_guess[0]) #Take the first part of the user guess to parse later
user_collum_guess = int(user_guess[-1]) #Take the second part of the user guess
game_board[user_row_guess, user_collum_guess] = "x"
print_gameboard(game_board)