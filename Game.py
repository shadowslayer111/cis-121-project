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
#user_guess = input("Enter a guess to make: ")
#user_row_guess = int(user_guess[0]) #Take the first part of the user guess to parse later
#user_collum_guess = int(user_guess[-1]) #Take the second part of the user guess
#game_board[user_row_guess, user_collum_guess] = "x"
#Very jankey way to do exention with 0 being up,1 being right,2 being down and 3 being left
def rotation_num_to_position(inital_pos,rotation_num):
    if rotation_num == 0:
        extention_position = int(inital_pos[0][0]) + 1
        return f"{extention_position},{inital_pos[0][2]}"
    if rotation_num == 1:
        extention_position = int(inital_pos[0][2]) + 1
        return f"{inital_pos[0][0]},{extention_position}"
    if rotation_num == 2:
        extention_position = int(inital_pos[0][0]) - 1
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
#For edge cases if the selection is in the corner
    if inital_enemy_placement_row == 1 and inital_enemy_placement_collum == 1:
        enemy_rotation = random.randint(2,3)
    elif inital_enemy_placement_row == 1 and inital_enemy_placement_collum == 5:
        enemy_rotation = random.randint(1,2)
    elif inital_enemy_placement_row == 5 and inital_enemy_placement_collum == 1:
        enemy_rotation = random.randint(0,1)
    elif inital_enemy_placement_row == 5 and inital_enemy_placement_collum == 5:
        enemy_rotation = random.randint(0,1)
        if enemy_rotation == 1:
            enemy_rotation = 3
    enemy_placement = [f"{inital_enemy_placement_row},{inital_enemy_placement_collum}"]
    enemy_placement.append(str(rotation_num_to_position(enemy_placement,enemy_rotation)))
    return enemy_placement
print(make_enemy())