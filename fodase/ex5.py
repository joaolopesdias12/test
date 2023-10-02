board = [[]]

for i in range(9):
    board.append([])
    for j in range(8):
        if i == 8: board[i].append(chr(65+j))
        elif (i+j)%2==0: board[i].append("O")
        else: board[i].append("X")
    board[i].append(str(8-i))
    print(board[i])