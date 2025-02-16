def is_valid_position(r, col):
    return 0 <= r < 6 and 0 <= col < 7

def check_direction_count(cur_r_idx, cur_col_idx, r_idx_movement, col_idx_movement, board, cur_player_num, sign="+"):
    count = 0
    for idx in range(1, 4):
        next_r_idx = cur_r_idx + (r_idx_movement * idx) if sign == "+" else cur_r_idx - (r_idx_movement * idx)
        next_col_idx = cur_col_idx + (col_idx_movement * idx) if sign == "+" else cur_col_idx - (col_idx_movement * idx)
        if not is_valid_position(next_r_idx, next_col_idx):
            return count
        if board[next_r_idx][next_col_idx] == cur_player_num:
            count += 1
        else:
            return count
    return count