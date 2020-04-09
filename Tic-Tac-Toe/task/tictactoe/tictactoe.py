def show_game_field(cells: str):
    head_str = "---------"
    print(head_str)
    for i in range(0, 3):
        print("| " + " ".join(cells[i * 3:i * 3 + 3]) + " |")
    print(head_str)


def get_game_sets():
    global cells_list
    cells_list = [char for char in state]
    sets = [cells_list[6:], cells_list[3:6], cells_list[:3],        # rows
            cells_list[6::-3], cells_list[7::-3], cells_list[8::-3],    # columns
            cells_list[::4], cells_list[2:7:2]]                     # diagonals
    return sets


def current_game_state():
    global game_over
    finished = True
    x_wins = False
    o_wins = False
    sets = get_game_sets()

    for _ in sets:
        if all(cell == _[0] for cell in _):
            if _[0] == 'X':
                x_wins = True
            elif _[0] == 'O':
                o_wins = True
            else:
                pass

    if not x_wins and not o_wins:
        for item in sets:
            if '_' in item:
                finished = False
        if finished:
            print('Draw')
            game_over = True
    elif x_wins:
        print('X wins')
        game_over = True
    elif o_wins:
        print('O wins')
        game_over = True
    else:
        pass


def make_move():
    columns = get_game_sets()[3:6]
    while True:
        user_move = input('Enter the coordinates: ')
        coords = user_move.split()

        try:
            x_coord = int(coords[0]) - 1
            y_coord = int(coords[1]) - 1
        except ValueError:
            print('You should enter numbers!')
            continue

        if not 0 <= x_coord <= 2 or not 0 <= y_coord <= 2:
            print('Coordinates should be from 1 to 3!')
        elif columns[x_coord][y_coord] != '_':
            print('This cell is occupied! Choose another one!')
        else:
            if state.count('X') == state.count('O'):
                columns[x_coord][y_coord] = 'X'
            else:
                columns[x_coord][y_coord] = 'O'
            new_state = ''
            temp = ''
            for x in columns:
                for y in x:
                    temp += y
            for i in range(3):
                new_state += temp[2-i::3]
            return new_state


state = '_________'
game_over = False
cells_list = []
show_game_field(state)
while not game_over:
    state = make_move()
    show_game_field(state)
    current_game_state()
