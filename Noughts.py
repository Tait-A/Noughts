# Noughts and Crosses

import random


class Noughts:
    def __init__(self, player):
        self.board = [None] * 9
        self.player = player
        self.availiableMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.playGame()

    def turn(self):
        if self.player:
            self.playerTurn()
        else:
            self.computerTurn()

    # Function to get the players move

    def playerTurn(self):
        move = input("Enter your move (1-9): ")
        move = self.validateMove(move)
        self.board[move - 1] = "X"
        self.availiableMoves.remove(move)
        if self.checkWin():
            print("You won!")
        self.player = False

    # Function to get the computers move
    def computerTurn(self):
        move = self.determineBestMove()
        self.board[move - 1] = "O"
        self.availiableMoves.remove(move)
        if self.checkWin():
            print("Computer won!")
        self.player = True

    def validateMove(self, move):
        try:
            move = int(move)
            if move in self.availiableMoves:
                return move
            else:
                print("Invalid move, that space is already taken")
                print("The moves available are: " + str(self.availiableMoves))
                move = input("Enter your move (1-9): ")
                return self.validateMove(move)
        except ValueError:
            print("Invalid move, please enter a number between 1 and 9")
            print("The moves available are: " + str(self.availiableMoves))
            move = input("Enter your move (1-9): ")
            return self.validateMove(move)

    # Function to determine the best move for the computer

    def determineBestMove(self):
        winningMoves = self.getWinningMoves()
        lossSavingMoves = self.getLossSavingMoves()
        if winningMoves:
            return winningMoves[0]
        elif lossSavingMoves:
            return lossSavingMoves[0]
        elif self.availiableMoves.__contains__(5):
            return 5
        else:
            return random.choice(self.availiableMoves)

    def getWinningMoves(self):
        winningMoves = []
        for move in self.availiableMoves:
            self.board[move - 1] = "O"
            if self.checkWin():
                winningMoves.append(move)
            self.board[move - 1] = None
        return winningMoves

    def getLossSavingMoves(self):
        lossSavingMoves = []
        for move in self.availiableMoves:
            self.board[move - 1] = "X"
            if self.checkWin():
                lossSavingMoves.append(move)
            self.board[move - 1] = None
        return lossSavingMoves

    def checkWin(self):
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != None:
                return True
            if (
                self.board[i * 3]
                == self.board[i * 3 + 1]
                == self.board[i * 3 + 2]
                != None
            ):
                return True
            if self.board[0] == self.board[4] == self.board[8] != None:
                return True
            if self.board[2] == self.board[4] == self.board[6] != None:
                return True

        return False

    def prettyPrint(self):
        print("+---+---+---+")
        for i in range(3):
            print(
                "|",
                self.getPrintValue(self.board[i * 3]),
                "|",
                self.getPrintValue(self.board[(i * 3 + 1)]),
                "|",
                self.getPrintValue(self.board[(i * 3 + 2)]),
                "|",
            )
            print("+---+---+---+")

    def playGame(self):
        self.prettyPrint()
        while True:
            if self.player:
                self.playerTurn()
            else:
                self.computerTurn()
            self.prettyPrint()

            if self.checkWin():
                break
            elif self.availiableMoves == []:
                print("Draw! - Game Over")
                break

    def getPrintValue(self, value):
        if value == None:
            return " "
        else:
            return value


player = True

game = Noughts(player)
