def show_game_field(cells: str):
    head_str = "---------"
    print(head_str)
    for i in range(0, 3):
        print("| " + " ".join(cells[i * 3:i * 3 + 3]) + " |")
    print(head_str)


def get_game_sets(game_state: str):
    cells_list = [char for char in game_state]
    sets = [cells_list[:3], cells_list[3:6], cells_list[6:],            # rows
            cells_list[::3], cells_list[1::3], cells_list[2::3],    # columns
            cells_list[::4], cells_list[2:7:2]]                         # diagonals
    return sets


def current_game_state():
    global game_over
    game_over = True
    finished = True
    x_wins = False
    o_wins = False
    sets = get_game_sets(state)

    for item in sets:
        if all(cell == item[0] for cell in item):
            if item[0] == 'X':
                x_wins = True
            elif item[0] == 'O':
                o_wins = True
            else:
                pass

    if not x_wins and not o_wins:
        for char in state:
            finished = False if '_' in char else True

    if x_wins:
        print('X wins')
    elif o_wins:
        print('O wins')
    elif finished:
        print('Draw')
    else:
        game_over = False


def make_move():
    rows = get_game_sets(state)[:3]
    while True:
        coords = input('Enter the coordinates: ').split()

        try:
            x_coord = int(coords[0]) - 1
            y_coord = int(coords[1]) - 1
        except ValueError:
            print('You should enter numbers!')
            continue

        if not 0 <= x_coord <= 2 or not 0 <= y_coord <= 2:
            print('Coordinates should be from 1 to 3!')
        elif rows[x_coord][y_coord] != '_':
            print('This cell is occupied! Choose another one!')
        else:
            if state.count('X') == state.count('O'):
                rows[x_coord][y_coord] = 'X'
            else:
                rows[x_coord][y_coord] = 'O'
            new_state = ''
            for x in rows:
                for y in x:
                    new_state += y
            return new_state


state = '_________'
game_over = False
show_game_field(state)
while not game_over:
    state = make_move()
    show_game_field(state)
    current_game_state()
