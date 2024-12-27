from helpers.check_bishop import check_bishop
from helpers.check_king import check_king
from helpers.check_knight import check_knight
from helpers.check_pwan import check_pawn
from helpers.check_queen import check_queen
from helpers.check_roock import check_rook


# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    """
    retourne la liste des déplacement possible d'une piece 

    :param pieces: piece
    :type pieces: 
    :param locations: sa position actuel sur l'échequier
    :type tuple: 
    :param turn: 
    :type turn: 
    :return: Description
    :rtype: list[Any]"""
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list
