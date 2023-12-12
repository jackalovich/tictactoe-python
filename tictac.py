class TicTacBoard():
    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]


    def updateboard(self, rowpos, colpos, player):
            self.board[rowpos][colpos] = f"{player}"
            
    def __str__(self):
        a = f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n"
        b = "_ _ _ _ _\n"
        c = f"{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n"
        d = "_ _ _ _ _\n"
        e = f"{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}\n"
        return a + b + c + d + e
    
    def checkvictory(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] != " ":
                    print(f"player {self.board[0][i]} is victorious")
                    return True
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] != " ":
                    print(f"player {self.board[i][0]} is victorious")
                    return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] != " ":
                print(f"player {self.board[0][0]} is victorious")
                return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] != " ":
                print(f"player {self.board[0][2]} is victorious")
                return True
        
    def checkmoremoves(self):
        return any(col == " " for row in self.board for col in row)
    
    def checkvalidmove(self, rowpos, colpos):
        if self.board[rowpos][colpos] == " ":
            return True
        else:
            print("Invalid Move")
            return False

tictacboard = TicTacBoard()
setplayer = 1

while True:
    print(tictacboard)
    if tictacboard.checkvictory():
        break
    if not tictacboard.checkmoremoves():
        print("No more moves")
        break
    therow = int(input("Please enter the row: "))
    thecol = int(input("Please enter the col: "))
    while tictacboard.checkvalidmove(therow, thecol):
        if setplayer == 1:
            tictacboard.updateboard(therow, thecol, "X")
            setplayer = 2
            break
        elif setplayer == 2:
            tictacboard.updateboard(therow, thecol, "0")
            setplayer = 1
            break