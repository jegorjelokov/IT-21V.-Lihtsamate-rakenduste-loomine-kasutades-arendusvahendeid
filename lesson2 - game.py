map1 = [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 24]
]
map2 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 24]
]
map = map1

# step 1
start_position_x = 0
start_position_y = 0


def move(step, current_position_x, current_position_y):
    print("Current step is = ", step)
    print("Current correct_position_y = ", current_position_y)
    print("Current correct_position_x = ", current_position_x)
    can_move_right = current_position_x <= 2 and map[current_position_y][current_position_x+1] == 0
    can_move_bottom = current_position_y <= 2 and map[current_position_y+1][current_position_x] == 0

    if can_move_right:
        print("Should move right")
        current_position_x = current_position_x + 1
    if can_move_bottom:
        print("Should move down")
        current_position_y = current_position_y + 1

    return [current_position_x, current_position_y]

new_position = move(1, start_position_x, start_position_y)