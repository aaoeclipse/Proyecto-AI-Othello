from Communication import *
from Othello import *
import sys

def main():
    """ Main function: creates the communication and the Game in the front end """
    # Create the communication
    if len(sys.argv) != 3:
        print("$ python3 Manager.py [ip] [port]")
        exit(0)
    ip = sys.argv[1]
    port = sys.argv[2]
    # Get Username and tournament id
    username = input("User Name: ")
    id = input("Tournament id: ")
    ip = ip + ':' + port
    player = Communication(ip, username, int(id))
    # creates the game with board and commands
    

    # username = 'DejateVenir'
    # id = input("Tournament ID: ")
    # id = 142857

    # Connect player to game
    # player.connect(username, int(id))



if __name__ == "__main__":
    """ Runs the main application first """
    main()