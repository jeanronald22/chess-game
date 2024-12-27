# check queen valid moves
from helpers.check_bishop import check_bishop
from helpers.check_roock import check_rook


def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list