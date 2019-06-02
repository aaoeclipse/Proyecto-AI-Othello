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
            return [boardObj, (-1,-1)] # .Heuristic(self.player,self.enemy)

        if maximizingPlayer:
             maxEval = Othello()
             maxEval.setHeuristic(-math.inf)

            #  print(posScenarios)
             for child in self.posibleMovies(boardObj,self.player):
                 evalBoard = self.minimax_a_b_p(child[0], False, alpha=alpha, beta=beta, depth=depth-1)
                 if maxEval.Heuristic(self.player,self.enemy) < evalBoard[0].Heuristic(self.player,self.enemy):
                     maxEval = copy.deepcopy(evalBoard)
                #  maxEval = max(maxEval, evalBoard.Heuristic(self.player,self.enemy))
                 alpha = max(alpha, evalBoard[0].Heuristic(self.player,self.enemy))
                 if beta <= alpha:
                     break
                 return maxEval

        else:
             minEval = Othello()
             minEval.setHeuristic(math.inf)

             for child in self.posibleMovies(boardObj, self.enemy):
                 evalBoard = self.minimax_a_b_p(child[0], True, alpha=alpha, beta=beta, depth=depth-1)
                 if minEval.Heuristic(self.player,self.enemy) > evalBoard[0].Heuristic(self.player,self.enemy):
                     minEval = copy.deepcopy(evalBoard)
                #  minEval = min(minEval, evalBoard)
                 beta = min(beta, evalBoard[0].Heuristic(self.player,self.enemy))
                 if beta <= alpha:
                     break
                 return minEval


    def posibleMovies(self, boardObject, player):
        """ Checks which possible moves it can make and returns the board """
        posToEval = self.surrounding(boardObject.board, (player%2)+1)
        currBoard = copy.deepcopy(boardObject)
        possibleBoardResults = []

        for position in posToEval:
            if (boardObject.checkIfAvailable(x=position[0]+1, y=position[1]+1, player=player)):
                newboard = copy.deepcopy(boardObject)
                possibleBoardResults.append([newboard, (position[0],position[1])])
                boardObject.setBoard(currBoard.board)
            # else:
            #     print('Failed on: x: {}, y: {}'.format(position[0],position[1]))
        # if possibleBoardResults == []:
        #     print('[-] NO AVAILABLE MOVES!')
        #     currBoard.printBoard()
        #     print('Player {}!'.format(player))
        #     print(posToEval)
        #     print(currBoard.checkIfAvailable(x=3, y=1, player=player))
        return possibleBoardResults

    def surrounding(self, board, enemy):
        """ Check which moves to evaluate """
        positionsToEval = []
        for x in range(8):
            for y in range(8):
                if board[y][x] == enemy:
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
        # print('Positinos to Evaluate: {}'.format(positionsToEval))
        return positionsToEval