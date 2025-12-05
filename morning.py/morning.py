import random
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
#Very jankey way to do exention with 0 being up,1 being right,2 being down and 3 being left
def rotation_num_to_position(inital_pos,rotation_num):
    if rotation_num == 0:
        extention_position = int(inital_pos[0][0]) - 1
        return f"{extention_position},{inital_pos[0][2]}"
    if rotation_num == 1:
        extention_position = int(inital_pos[0][2]) + 1
        return f"{inital_pos[0][0]},{extention_position}"
    if rotation_num == 2:
        extention_position = int(inital_pos[0][0]) + 1
        return f"{extention_position},{inital_pos[0][2]}"
    if rotation_num == 3:
        extention_position = int(inital_pos[0][2]) - 1
        return f"{inital_pos[0][0]},{extention_position}"

#Makes an enemy with and outputs a list with the cordinates of the two positions the ship is in    
def make_enemy():
    inital_enemy_placement_row = random.randint(1,5)
    inital_enemy_placement_collum = random.randint(1,5)
    enemy_rotation = random.randint(0,3)
    #For if inital placement is on the edge to prevent going past the playable area
    if inital_enemy_placement_row == 1:
        enemy_rotation = random.randint(1,3)
    elif inital_enemy_placement_row == 5:
        enemy_rotation = random.randint(0,2)
        if enemy_rotation == 2:
            enemy_rotation = 3
    if inital_enemy_placement_collum == 1:
        enemy_rotation = random.randint(0,2)
    elif inital_enemy_placement_collum == 5:
        enemy_rotation = random.randint(0,2)
        if enemy_rotation == 1:
            enemy_rotation = 3
        if inital_enemy_placement_row == 1:
            enemy_rotation = random.randint(1,3)
        elif inital_enemy_placement_row == 5:
            enemy_rotation = random.randint(0,2)
            if enemy_rotation == 2:
                enemy_rotation = 3
    if inital_enemy_placement_collum == 1:
        enemy_rotation = random.randint(0,2)
    elif inital_enemy_placement_collum == 5:
        enemy_rotation = random.randint(0,2)
        if enemy_rotation == 1:
            enemy_rotation = 3
    #For edge cases if the selection is in the corner
    #Very jankey way to do exention with 0 being up,1 being right,2 being down and 3 being left
    if inital_enemy_placement_row == 1 and inital_enemy_placement_collum == 1:
        enemy_rotation = random.randint(1,2)
    elif inital_enemy_placement_row == 1 and inital_enemy_placement_collum == 5:
        enemy_rotation = random.randint(2,3)
    elif inital_enemy_placement_row == 5 and inital_enemy_placement_collum == 1:
        enemy_rotation = random.randint(0,1)
    elif inital_enemy_placement_row == 5 and inital_enemy_placement_collum == 5:
        enemy_rotation = random.randint(0,1)
        if enemy_rotation == 1:
            enemy_rotation = 3
    enemy_placement = [f"{inital_enemy_placement_row},{inital_enemy_placement_collum}"]
    enemy_placement.append(str(rotation_num_to_position(enemy_placement,enemy_rotation)))
    return enemy_placement

#Function to check if the guess is a hit or miss
def check_hit(guess, enemy_positions):
    if guess in enemy_positions:
        return True
    else:
        return False

#Function to get valid input from player
def get_player_guess():
    while True:
        user_guess = input("Enter your guess (row,collum like 2,3): ")
        #Check if the input is valid
        if len(user_guess) == 3 and user_guess[1] == ",":
            try:
                row = int(user_guess[0])
                collum = int(user_guess[2])
                if row >= 1 and row <= 5 and collum >= 1 and collum <= 5:
                    return user_guess
                else:
                    print("Numbers must be between 1 and 5!")
            except:
                print("Please enter valid numbers!")
        else:
            print("Invalid format! Use format like: 2,3")

#Main game function
def play_game():
    print("=== BATTLESHIP ===")
    print("Try to sink the enemy ship!")
    print("The ship takes up 2 spaces on the board.")
    print()
    
    game_board = create_board(5) #creates the gameboard
    enemy_ship = make_enemy() #places the enemy ship randomly
    hits = 0 #counter for how many hits
    turns = 0 #counter for how many turns taken
    guesses_made = [] #list to store previous guesses
    
    #Main game loop - keeps going until ship is sunk
    while hits < 2:
        print()
        print_gameboard(game_board)
        print()
        print(f"Hits: {hits}/2  |  Turns taken: {turns}")
        
        #Get player guess
        guess = get_player_guess()
        
        #Check if already guessed this spot
        if guess in guesses_made:
            print("You already guessed that spot! Try again.")
            continue
        
        guesses_made.append(guess) #add to list of guesses
        turns = turns + 1
        
        #Parse the guess to update the board
        guess_row = int(guess[0])
        guess_collum = int(guess[2])
        
        #Check if its a hit or miss
        if check_hit(guess, enemy_ship):
            print("HIT!")
            game_board[guess_row, guess_collum] = "X" #mark hit on board
            hits = hits + 1
        else:
            print("Miss...")
            game_board[guess_row, guess_collum] = "O" #mark miss on board
    
    #Game over - player won
    print()
    print_gameboard(game_board)
    print()
    print("=== YOU SUNK THE BATTLESHIP! ===")
    print(f"You won in {turns} turns!")
    
    #Rating based on how many turns it took
    if turns <= 5:
        print("Rating: AMAZING! You got lucky!")
        with open("score.csv","a") as scorefile:
            scorefile.write(f"{gamenumber},{turns}\n")
        scorefile.close()
    elif turns <= 10:
        print("Rating: Great job!")
        with open("score.csv","a") as scorefile:
            scorefile.write(f"{gamenumber},{turns}\n")
            scorefile.close()
    elif turns <= 15:
        print("Rating: Good work!")
        with open("score.csv","a") as scorefile:
            scorefile.write(f"{gamenumber},{turns}\n")
        scorefile.close()
    else:
        print("Rating: You got there eventually!")
        with open("score.csv","a") as scorefile:
            scorefile.write(f"{gamenumber},{turns}\n")
        scorefile.close()

#Ask if player wants to play again
gamenumber = 1
play_again = "yes"
scorefile = open("score.csv","w")
scorefile.write("Gamenumber,Turns")
scorefile.close()
while play_again == "yes":
    play_game()
    print()
    play_again = input("Do you want to play again? (yes/no): ")
    play_again = play_again.lower() #make it lowercase so YES and Yes work too
    gamenumber +=1
print("Thanks for playing!")

#Run the game
gamenumber = 1