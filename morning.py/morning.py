        self.position = make_enemy()
        self.hits = 0
    

#Ask if player wants to play again
def main():
    play_again = "yes"
    while play_again == "yes":
        play_game()
        print()
        play_again = input("Do you want to play again? (yes/no): ")
        play_again = play_again.lower() #make it lowercase so YES and Yes work too
    print("Thanks for playing!")

#Run the game
main()
#Setup variables to make the game work
game_board = create_board(5)
gamenumber = 1
play_again = "yes"
scorefile = open("score.csv","w")
scorefile.write("Gamenumber,Turns")
Battleship = Ship()
#Main game loop
while play_again == "yes":
    play_game()
    print()
    play_again = input("Do you want to play again? (yes/no): ")
    play_again = play_again.lower() #make it lowercase so YES and Yes work too
    gamenumber +=1
    Battleship.new_game()
scorefile.close()
print("Thanks for playing!")