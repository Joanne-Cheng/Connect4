board = []

def makeBoard():
    for i in range(6):
        row = []
        for j in range(7):
            row.append(' ')
        board.append(row)

def printBoard():
    tracker = ['0','1','2','3','4','5','6']

    for row in board:
        r = " | "
        for item in row:
            r += item + " | "
        print(r)

    print(" " + "_" * len(tracker * 4) )

    newtracker = " | "
    for item in tracker:
        newtracker += item + " | "
    print(newtracker)


def checkwin(player):
    for r in range(len(board) - 3):
        for c in range(len(board[r]) - 3):
            if (board[r][c] != " " and board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]):
                return True
    for r in range(len(board)):
        for c in range(len(board[r]) - 3):
            if (board[r][c] != " " and board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]):
                return True
    for r in range(len(board) - 3):
        for c in range(len(board[r])):
            if (board[r][c] != " " and board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]):
                return True
    for r in range(len(board) - 3):
        for c in range(3, len(board[r])):
            if (board[r][c] != " " and board[r][c] == board[r+1][c-1] == board[r+2][c-2] == board[r+3][c-3]):
                return True
    return False


def insert (player):
    c = int(input("Choose a column to drop " + player + "\n"))
    if not (0 <= c <= 6):
        print("That column is out of bounds, try again.")
        return insert(player)

    replace = False
    for i in range(5,-1,-1):
        if (board[i][c] == " "):
            board[i][c] = player
            replace = True
            break

    if not replace:
        print("That column is full, try again.")
        return insert(player)


makeBoard()

win = False
for turn in range (0,42):
    printBoard()
    if turn % 2 == 0:
        insert ('x')
        if (checkwin('x')):
            printBoard()
            win = True
            print("you win player x")
            break
    else:
        insert ('o')
        if (checkwin('o')):
            printBoard()
            win = True
            print("you win player o")
            break

if not win:
    printBoard()
    print("Tie game!")
