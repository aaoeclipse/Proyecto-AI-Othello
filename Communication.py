import socketio
import requests
import random
from Othello import *
from aiohttp import web
from minimax_a_b import Minimax

class Communication:
    """ Aqui va a estar la comunicacion entre el player y el backend """

    def __init__(self, ip):
        self.ip = ip
        self.sio = socketio.Client()
        self.game = Othello()
        self.columns = {
            1 : 'A',
            2 : 'B',
            3 : 'C',
            4 : 'D',
            5 : 'E',
            6 : 'F',
            7 : 'G',
            8 : 'H'
        }

        count = 0
        while count < 10:
            if self.game.checkIfAvailable(y=random.randint(1,8),x=self.columns.get(random.randint(1,8)),player=(count % 2)+1, dynamic=False):
                count += 1

        mini_max = Minimax(3,1,2)
        # mini_max.posibleMovies(self.game)
        mini_max.minimax_a_b_p(self.game, maximizingPlayer=True, depth=3)
        self.game.printBoard()

        # self.game.checkIfAvailable(y=3,x='E',player=1)
        # self.game.printBoard()

        # count = 0
        # while not self.game.Game_Finish():
        #     self.game.printBoard()
        #     if self.game.checkIfAvailable(y=random.randint(1,8),x=self.columns.get(random.randint(1,8)),player=(count % 2)+1, dynamic=False):
        #         count += 1
        # self.game.printBoard()
        # winner = self.game.Heuristic(1,2)
        # if  winner < 0:
        #     print('Player 2 wins by {} points'.format(-winner))    
        # if  winner > 0:
        #     print('Player 1 wins by {} points'.format(winner))    
        # if  winner == 0:
        #     print('Draw!')    
        # print('Game Finish')

    def connect(self, username, id):
        """ Connects and responds with signin """

        @self.sio.on('connect')
        def on_connect():
            self.sio.emit('signin', {
            'user_name': 'DejateVenir',
            'tournament_id': 142857,
            'user_role': 'player'
            })

        @self.sio.on('ok_signin')
        def on_signin():
            print('Success!')

        @self.sio.on('ready')
        def on_ready(data):
            gameID = data.get('game_id')
            playerTurnID = data.get('player_turn_id')
            board = data.get('board')

            print('Recived board: ')
            self.game.setBoard(board)

            while True:
                idx = random.randint(1,8)
                x = self.columns.get(idx)
                y = random.randint(1,8)
                if (self.game.checkIfAvailable(y, x)):
                    break
            
            positionAttack = (y-1)*8 + idx
            # Mostramos el board
            print('Attack on : ({},{})'.format(x,y) )
            self.game.printBoard()

            self.sio.emit('play', {
                'tournament_id': 142857,
                'player_turn_id': playerTurnID,
                'game_id': gameID,
                'movement': positionAttack
                })

        @self.sio.on('finish')
        def on_finish(data):
            gameID = data.get('game_id')
            playerTurnID = data.get('player_turn_id')
            winnerTurnID = data.get('winner_turn_id')
            board = data.get('board')

            print('{},{},{},{}'.format(gameID, playerTurnID, winnerTurnID, board))
            print('GAME FINISH {}'.format(winnerTurnID))
            self.game.setBoard(board)
            self.game.printBoard()

            self.game.reset()

            self.sio.emit('player_ready', {
                'tournament_id': 142857,
                'player_turn_id': playerTurnID,
                'game_id': gameID
                })

        self.sio.connect(self.ip)

        self.sio.wait()