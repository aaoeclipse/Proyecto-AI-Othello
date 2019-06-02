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
        self.moves = []
    
    def minimax_a_b_p(self, boardObj, maximizingPlayer, alpha=-math.inf, beta=math.inf,  depth=0):
        """ recursion, finds the best move based on the heuristic of the board """
        if depth == 0 or boardObj.Game_Finish():
            return boardObj # .Heuristic(self.player,self.enemy)

        if maximizingPlayer:
             maxEval = Othello()
             maxEval.setHeuristic(-math.inf)

            #  print(posScenarios)
             for child in self.posibleMovies(boardObj,self.player):
                 evalBoard = self.minimax_a_b_p(child, False, alpha=alpha, beta=beta, depth=depth-1)
                 if maxEval.Heuristic(self.player,self.enemy) < evalBoard.Heuristic(self.player,self.enemy):
                     maxEval = evalBoard
                #  maxEval = max(maxEval, evalBoard.Heuristic(self.player,self.enemy))
                 alpha = max(alpha, evalBoard.Heuristic(self.player,self.enemy))
                 if beta <= alpha:
                     break
                 return maxEval

        else:
             minEval = Othello()
             minEval.setHeuristic(math.inf)

             for child in self.posibleMovies(boardObj, self.enemy):
                 evalBoard = self.minimax_a_b_p(child, True, alpha=alpha, beta=beta, depth=depth-1)
                 if minEval.Heuristic(self.player,self.enemy) > evalBoard.Heuristic(self.player,self.enemy):
                     minEval = evalBoard
                #  minEval = min(minEval, evalBoard)
                 beta = min(beta, evalBoard.Heuristic(self.player,self.enemy))
                 if beta <= alpha:
                     break
                 return minEval


    def posibleMovies(self, boardObject, player):
        """ Checks which possible moves it can make and returns the board """
        posToEval = self.surrounding(boardObject.board)
        currBoard = copy.deepcopy(boardObject.board)

        possibleBoardResults = []

        for position in posToEval:
            if (boardObject.checkIfAvailable(position[0]+1, position[1]+1, player=player)):
                possibleBoardResults.append(copy.deepcopy(boardObject))
                # boardObject.printBoard()
                boardObject.setBoard(currBoard)

        # for x in possibleBoardResults:
        #     print(x.Heuristic(self.player, self.enemy))
        return possibleBoardResults

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