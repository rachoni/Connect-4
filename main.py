from game_logic.game import obtain_position, is_winner
from board.display import print_board

ROWS = 6
COLUMNS = 7
CONNECT_WINNER_COUNT = 4

available_spots = {column_index: ROWS - 1 for column_index in range(COLUMNS)}

turns = 1
matrix = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

print_board(matrix)

while True:
    player_number = 1 if turns % 2 != 0 else 2
    row_index, column_index = obtain_position(player_number, available_spots)
    matrix[row_index][column_index] = player_number
    available_spots[column_index] -= 1
    print_board(matrix)

    if turns >= 7 and is_winner(row_index, column_index, matrix, player_number):
        print(f"WINNER: Player {player_number}")
        break

    if (ROWS * COLUMNS) + 1 == turns:
        print("GAME OVER!")
        break

    turns += 1