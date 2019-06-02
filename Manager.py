from Communication import *
from Othello import *

def main():
    """ Main function: creates the communication and the Game in the front end """
    # Create the communication
    player = Communication('http://192.168.1.127:4000')
    # creates the game with board and commands
    
    # Get Username and tournament id
    # username = input("User Name: ")
    username = 'DejateVenir'
    # id = input("Tournament ID: ")
    id = 142857

    # Connect player to game
    # player.connect(username, int(id))



if __name__ == "__main__":
    """ Runs the main application first """
    main()