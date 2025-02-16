def validate_column_choice(player_num, col_choice, spots_available):
    try:
        col = int(col_choice)
        if col < 1 or col > 7:
            print(f"Player {player_num}, please enter a number between 1 and 7!")
            return None
        row_available = spots_available[col - 1]
        if row_available < 0:
            print(f"Player {player_num}, please select a column with one or more available spots!")
            return None
        return col
    except ValueError:
        print(f"Player {player_num}, please enter a valid number!")
        return None