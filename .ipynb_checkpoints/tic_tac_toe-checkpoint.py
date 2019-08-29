ttt_board = '''1|2|3
4|5|6
7|8|9'''

test_board1 = '''x|x|x
4|5|6
7|8|9'''

test_board2 = '''1|2|x
4|5|x
7|8|x'''

test_board3 = '''x|2|3
4|x|6
7|8|x'''

def check_win(board):
    data = board.split('\n')
    data_dic = {}
    
    for index, row in enumerate(data, 1):
        key = 'r' + str(index)        
        data_dic.setdefault(key, row)
    
    for index, row in enumerate(data_dic.values()):
        if row == 'o|o|o' or row == 'x|x|x':
            print(row)
            return True
        if index % 2 == 0:
#             These index numbers are off
            if board[index] == board[index + 6] == board[index + 13]:
                print(board[index])
                print(board[index + 6])
                print(board[index + 12])
                return True
    if board[0] == board[8] == board[16] or board[4] == board[8] == board[12]:
        return True
    return False
    


def game(board, turn_number):
    if check_win(board):
        print(board)
        return "You win"
    marker = None
    if turn_number % 2 == 0:
        marker = 'x'
    else:
        marker = 'o'
    print('Select a position to place {}: '.format(marker))
    place = input()
    board = board.replace(place, marker)
    print(board)


check_win(ttt_board)
assert check_win(test_board1) == True
assert check_win(test_board2) == True
assert check_win(test_board3) == True
print("All checks passed")

print(game(ttt_board, 1))