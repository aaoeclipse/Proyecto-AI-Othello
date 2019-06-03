from Othello import Othello
import math
import copy

class Minimax:
    """ AI minimax, it tries to predict future consecuences of the oponent and takes descisions on which move is the correct one based on this """
    def __init__(self, player, enemy):
        """  """
        self.player = player
        self.enemy = enemy
    
    def minimax_a_b_p(self, boardObj, maximizingPlayer, alpha=-math.inf, beta=math.inf,  depth=0):
        print(depth)
        # print('boardObj: {}'.format(boardObj.Heuristic(1,2)))
        # boardObj.printBoard()
        """ recursion, finds the best move based on the heuristic of the board """
        if depth == 0 or boardObj.Game_Finish():
            # print('TEST!!!!S')
            # print(boardObj.Heuristic(1,2))
            return boardObj # .Heuristic(self.player,self.enemy)

        if maximizingPlayer:
             maxEval = Othello()
             maxEval.setHeuristic(-math.inf)
             
             test = self.posibleMoves(boardObj, self.player)
             if test == []:
                 return boardObj
            #  for xi in test:
            #     print('test: {}'.format(xi.moves))
            #     xi.printBoard()
            #     print(xi.Heuristic(1,2))
            #  if test == []:
            #      return maxEval

             for child in test:
                #  print('in loop')
                #  print(child.moves)

                 evalBoard = self.minimax_a_b_p(child, False, alpha=alpha, beta=beta, depth=depth-1)

                #  if evalBoard == None:
                #      break
                #      return maxEval
                #  if evalBoard == None:
                #      break
                #      return maxEval
                #  print(maxEval.Heuristic(1,2))
                #  print(evalBoard)
                 if maxEval.Heuristic(self.player,self.enemy) < evalBoard.Heuristic(self.player,self.enemy):
                     maxEval = evalBoard

                 alpha = max(alpha, evalBoard.Heuristic(self.player,self.enemy))

                 if beta <= alpha:
                     break
                     
                 return maxEval

        else:
             minEval = Othello()
             minEval.setHeuristic(math.inf)
             test = self.posibleMoves(boardObj, self.enemy)

             if test == []:
                 return boardObj

             for child in test:
                 evalBoard = self.minimax_a_b_p(child, True, alpha=alpha, beta=beta, depth=depth-1)

                #  if evalBoard == None:
                #     #  return minEval
                #      break
                #  if evalBoard == None:
                #      break
                #      return minEval

                 if minEval.Heuristic(self.player,self.enemy) > evalBoard.Heuristic(self.player,self.enemy):
                     minEval = evalBoard
                 beta = min(beta, evalBoard.Heuristic(self.player,self.enemy))
                 if beta <= alpha:
                     break
                 return minEval


    def posibleMoves(self, boardObject, player):
        """ Checks which possible moves it can make and returns the board """
        enemy = (player % 2) + 1
        posToEval = self.surrounding(boardObject.board, enemy)
        currBoard = copy.deepcopy(boardObject.board)

        possibleBoardResults = []

        for position in posToEval:
            if (boardObject.checkIfAvailable(x=position[0]+1, y=position[1]+1, player=player)):
                new = copy.deepcopy(boardObject)
                possibleBoardResults.append(copy.deepcopy(new))
                boardObject.setBoard(currBoard)

        return possibleBoardResults

    def surrounding(self, board, enemy):
        """ Check which moves to evaluate """
        # print(board)
        positionsToEval = []
        for x in range(8):
            for y in range(8):
                if board[y][x] == enemy:
                    if y < 7:
                        if board[y+1][x] == 0:
                            if [x,y+1] in positionsToEval:
                                pass
                            else:
                                positionsToEval.append([x,y+1])
                    if y > 0:
                        if board[y-1][x] == 0:
                            if [x,y-1] in positionsToEval:
                                pass
                            else:
                                positionsToEval.append([x, y-1])
                    if x > 0:
                        if board[y][x-1] == 0:
                            if [x-1,y] in positionsToEval:
                                pass
                            else:
                                positionsToEval.append([x-1, y])
                    if x < 7:
                        if board[y][x+1] == 0:
                            if [x+1,y] in positionsToEval:
                                pass
                            else:
                                positionsToEval.append([x+1, y])
                    
                    if x > 0 and y > 0:
                        if board [y-1][x-1] == 0:
                            if [x-1,y-1] in positionsToEval:
                                pass
                            else:
                                positionsToEval.append([x-1, y-1])

                    if x < 7 and y < 7:
                        if board [y+1][x+1] == 0:
                            if [x+1,y+1] in positionsToEval:
                                pass
                            else:
                                positionsToEval.append([x+1, y+1])

                    if y > 0 and x < 7:
                        if board [y-1][x+1] == 0:
                            if [x+1,y-1] in positionsToEval:
                                pass
                            else:
                                positionsToEval.append([x+1, y-1])

                    if x > 0 and y < 7:
                        if board [y+1][x-1] == 0:
                            if [x-1,y+1] in positionsToEval:
                                pass
                            else:
                                positionsToEval.append([x-1, y+1])
        return positionsToEval