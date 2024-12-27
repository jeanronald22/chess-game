from constantes import *


# designer les pieces sur l'échequier
def draw_pieces(screen):
    """
    dessin des pieces sur l'échequier

    :param screen: ecran principal
    :type screen: """

    for i in range(len(white_pieces)):  # on itére sur les pieces blanches
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(
                white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30)
            )
        else:
            screen.blit(white_images[index], (white_locations[i]
                                              [0] * 100 + 10, white_locations[i][1] * 100 + 10)
                        )
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2
                                 )

    for i in range(len(black_pieces)):  # les pieces noirs
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(
                black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30)
            )
        else:
            screen.blit(black_images[index], (black_locations[i]
                                              [0] * 100 + 10, black_locations[i][1] * 100 + 10)
                        )
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [
                    black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 2
                                 )
