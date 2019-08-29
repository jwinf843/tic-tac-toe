ttt_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

t_board1 = [
    ['x', 'x', 'x'],
    [4, 5, 6],
    [7, 8, 9]
]
t_board2 = [
    ['x', 2, 3],
    ['x', 5, 6],
    ['x', 8, 9]
]
t_board3 = [
    ['x', 2, 3],
    [4, 'x', 6],
    [7, 8, 'x']
]
t_board4 = [
    [1, 2, 'x'],
    [4, 'x', 6],
    ['x', 8, 9]
]

def display_board(board):
    for row in board: 
        row.insert(1, '|')
        row.insert(3, '|')
        str_row = ''.join([str(item) for item in row])
        print(str_row)   

def check_win(board):
    #rotate matrix 90deg
    rotate_board = [list(reversed(col)) for col in zip(*board)]

    # check rows
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2]:
            print('\nwin row')
            return True
        if rotate_board[i][0] == rotate_board[i][1] == rotate_board[i][2]:
            print('\nwin column')
            return True
    
    #check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        print('\nwin diagonal L->R')
        return True
    if rotate_board[0][0] == rotate_board[1][1] == rotate_board[2][2]:
        print('\nwin diagonal R->L')
        return True

def build_board(board, turn_info):
    position = turn_info[0]
    marker = turn_info[1]
    results = []
    for row in board:
        str_row = ''.join([str(item) for item in row])
        if position in str_row:
            str_row = str_row.replace(position, marker)
        new_row = [char for char in str_row if char != '|']
        results.append(new_row)
    return results

# board = build_board(ttt_board, ('1', 'x'))
# display_board(board)

def get_info(turn_number):
    marker = 'o'
    if turn_number % 2 == 0:
        marker = 'x'

    position = input('Select a position to place your {}: '.format(marker))
    
    return (position, marker)

def game():
    board = ttt_board
    turn = 0
    while turn < 9:
        display_board(board)
        turn_info = get_info(turn)
        turn += 1
        print('\n')
        board = build_board(board, turn_info)
        if check_win(board):
            display_board(board)
            return
    print('\nNo conclusive winner')
    display_board(board)

game()