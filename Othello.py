import numpy as np

class Othello:
    """ Esta clase va a crear el othello con todas las instruccioens y posibles jugadas """

    def __init__(self, givenBoard=None):
        """ Crea las dimensiones y el tablero vacio """
        self.columns = {
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4,
            'E' : 5,
            'F' : 6,
            'G' : 7,
            'H' : 8
        }
        self.set_heuristic = False
        if givenBoard is None:
            # Create board 8x8
            self.board = [
                [0,0,0,0,0,0,0,0], \
                [0,0,0,0,0,0,0,0], \
                [0,0,0,0,0,0,0,0], \
                [0,0,0,1,2,0,0,0], \
                [0,0,0,2,1,0,0,0], \
                [0,0,0,0,0,0,0,0], \
                [0,0,0,0,0,0,0,0], \
                [0,0,0,0,0,0,0,0]]
        else:
            self.board = givenBoard

    def setHeuristic(self, heuristic):
        self.setHeuristic = True
        self.given_heuristic = heuristic
    
    def checkIfAvailable(self, y, x, player, dynamic=True):
        """ Changes the value of the cell if it's available """
        currBoard = self.board
        if type(x) == int:
            x = x - 1
        else:
            x = int(self.columns.get(x)) - 1
        y = y - 1
        if x > 7 or y > 7:
            return False

        if self.board[y][x] == 0:
            self.board[y][x] = player
            if (self.checkFlip(x,y)):
                if not dynamic:
                    newBoard = self.board
                    self.board = currBoard
                    return True, newBoard
                else:
                    return True
            else:
                self.board[y][x] = 0
        # else:
        #     print('Casilla no displonible')
        return False

    def getAndTransform(self, number):
        x = number % 8
        y = number / 8
        self.board[y][x] = '1'

    def printBoard(self):
        print('    ', end='')
        for column in self.columns:
            print(column, end='  ')
        print('')
        for idx, x in enumerate(self.board):
            print('{} '.format(idx+1), end=' ')
            print(x)
        
    def setBoard(self, board):
        self.board = np.array(board).reshape((8, 8))

    def reset(self):
        print('[*] Board Reset')
        self.board = [
            [0,0,0,0,0,0,0,0], \
            [0,0,0,0,0,0,0,0], \
            [0,0,0,0,0,0,0,0], \
            [0,0,0,1,2,0,0,0], \
            [0,0,0,2,1,0,0,0], \
            [0,0,0,0,0,0,0,0], \
            [0,0,0,0,0,0,0,0], \
            [0,0,0,0,0,0,0,0]]

    def checkFlip(self, x, y):
        """ Recieves x and y from another def, which means we have dont have to subtract """
        # ----------------------------
        # --                          --
        # --     1    2    3          --
        # --     4    0    5          --
        # --     6    7    8          --
        # --                          --
        # ----------------------------

        player = self.board[y][x]
        if player == 1:
            enemy = 2
        else:
            enemy = 1

        countFails = 0
        for i in range(8):
            # print("i == {}".format(i))
            if(self.checkDirection(x,y,(i), player, enemy) == False):
                countFails = countFails + 1
                # print('Failed:',end=' ')
            # print('x: {}, y:{}, i:{}, player:{}, enemy:{}'.format(x,y,i,player,enemy))
            
        if countFails == 8:
            return False
        return True
        

    def checkDirection(self, x, y, dir, player, enemy):
        # ----------------------------
        # --    \      |    /         --
        # --     1    2    3          --
        # --   - 4    0    5   -      --
        # --     6    7    8          --
        # --   /      |      \        --
        # ----------------------------
        directions = {
            1: [-1,-1] ,
            2: [0,-1 ] ,
            3: [1,-1 ] ,
            4: [-1,0 ] ,
            5: [1,0  ] ,
            6: [-1, 1] ,
            7: [0,1  ] ,
            8: [1, 1 ]
        }
        dir += 1
        vector = directions.get(dir)
        positionToFlip = []
        tmpx = x
        tmpy = y

        while True:
            if dir <= 3:
                if tmpy == 0:
                    break
            if dir >= 5:
                if tmpy == 7:
                    break 
            if dir == 1 or dir == 4 or dir == 6:
                if tmpx == 0:
                    break
            if dir == 3 or dir == 5 or dir == 8:
                if tmpx == 7:
                    break
            tmpx = tmpx + vector[0]
            tmpy = tmpy + vector[1]
            if self.board[tmpy][tmpx] == enemy:
                positionToFlip.append((tmpx,tmpy))
                
            elif self.board[tmpy][tmpx] == player:
                self.flip(positionToFlip, player)
                break

            elif self.board[tmpy][tmpx] == 0:
                positionToFlip = []
                break
            else:
                print('[-] Error on Othello: expecting 0,1,2 got {}'.format(self.board[tmpy][tmpx]))
                break
        
        if positionToFlip == []:
            return False
        return True

    def flip(self, list_pos, player):
        for x,y in list_pos:
            self.board[y][x] = player
    def Game_Finish(self):
        for x in range(8):
            for y in range(8):
                if self.board[y][x] == 0:
                    return False
        return True
    
    def Heuristic(self, player, enemy):
        """ Gets the heuristics depending on the state of the board """
        # adds all the players coins
        if self.setHeuristic == True:
            return self.given_heuristic
        
        positive_points = 0
        negative_points = 0
        for xi in range(8):
            for yi in range(8):
                if self.board[yi][xi] == player:
                    positive_points += 1
                elif self.board[yi][xi] == enemy:
                    negative_points += 1
        result = positive_points - negative_points
        return result
    
