from Othello import Othello
import math
import copy

class Minimax:
    """ AI minimax, it tries to predict future consecuences of the oponent and takes descisions on which move is the correct one based on this """
    def __init__(self, depth, player, enemy):
        """  """
        self.depth = depth
        self.player = player
        self.enemy = enemy
    
    def minimax_a_b_p(self, boardObj, maximizingPlayer, alpha=-math.inf, beta=math.inf,  depth=0):
        """ recursion, finds the best move based on the heuristic of the board """
        if depth == 0 or boardObj.Game_Finish():
            # retyrb 
            return 5

        if maximizingPlayer:
             maxEval = -math.inf
             for child in self.posibleMovies(boardObj):
                 eval = minimax_a_b_p(child, False, alpha=alpha, beta=beta, depth=depth-1)
                 maxEval = max(maxEval, eval.Heuristic)
                 alpha = max(alpha, eval.Heuristic)
                 if beta <= alpha:
                     break
                 return maxEval

        else:
             minEval = math.inf
             for each in self.posibleMovies(boardObj):
                 eval = minimax_a_b_p(child, True, alpha=alpha, beta=beta, depth=depth-1)
                 minEval = min(minEval, eval)
                 beta = min(beta, eval)
                 if beta <= alpha:
                     break
                 return minEval


    def posibleMovies(self, boardObject):
        """ Checks which possible moves it can make and returns the board """
        posToEval = self.surrounding(boardObject.board)
        currBoard = copy.deepcopy(boardObject.board)

        possibleBoardResults = []

        for position in posToEval:
            if (boardObject.checkIfAvailable(position[0]+1, position[1]+1, player=self.player)):
                possibleBoardResults.append(copy.deepcopy(boardObject))
                boardObject.printBoard()
                boardObject.setBoard(currBoard)
            else:
                print('[-] This is not possible')

        for x in possibleBoardResults:
            print(x.Heuristic(self.player, self.enemy))

    def surrounding(self, board):
        """ Check which moves to evaluate """
        # print(board)
        positionsToEval = []
        for x in range(8):
            for y in range(8):
                if board[y][x] == self.enemy:
                    if y < 7:
                        if board[y+1][x] == 0:
                            positionsToEval.append([x,y+1])
                    if y > 0:
                        if board[y-1][x] == 0:
                            positionsToEval.append([x, y-1])
                    if x > 0:
                        if board[y][x-1] == 0:
                            positionsToEval.append([x-1, y])
                    if x < 7:
                        if board[y][x+1] == 0:
                            positionsToEval.append([x+1, y])
                    
                    if x > 0 and y > 0:
                        if board [y-1][x-1] == 0:
                            positionsToEval.append([x-1, y-1])

                    if x < 7 and y < 7:
                        if board [y+1][x+1] == 0:
                            positionsToEval.append([x+1, y+1])

                    if y > 0 and x < 7:
                        if board [y-1][x+1] == 0:
                            positionsToEval.append([x+1, y-1])

                    if x > 0 and y < 7:
                        if board [y+1][x-1] == 0:
                            positionsToEval.append([x-1, y+1])
        return positionsToEval