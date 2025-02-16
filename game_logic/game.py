from ..utils.helpers import check_direction_count
from ..utils.validation import validate_column_choice

direction_mapper = {
    "down": (1, 0),
    "right": (0, 1),
    "up_right": (1, 1),
    "up-left": (1, -1)
}

def is_winner(cur_r_idx, cur_col_idx, board, cur_player_num):
    total_count = 1
    for direction, movement in direction_mapper.items():
        count = check_direction_count(cur_r_idx, cur_col_idx, movement[0], movement[1], board, cur_player_num)
        total_count += count
        if direction != "down":
            count = check_direction_count(cur_r_idx, cur_col_idx, movement[0], movement[1], board, cur_player_num, sign="-")
            total_count += count
        if total_count >= 4:
            return True
    return False

def obtain_position(player_num, spots_available):
    while True:
        data = input(f"Player {player_num}, please select a column")
        col = validate_column_choice(player_num, data, spots_available)
        if not col:
            continue
        col_idx = col - 1
        return spots_available[col_idx], col_idx