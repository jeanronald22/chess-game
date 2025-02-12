import pygame
from constantes import *


def draw_board(screen):
    """
    dessin de l'échequier

    :param screen: ecran principal
    :type screen: """

    cell_size = HAUTEUR // 8  # Taille d'une cellule de l'échiquier (carré)
    board_size = cell_size * 8  # Taille totale de l'échiquier (900px)

    # Dessin de l'échiquier
    for i in range(32):
        column = i % 4
        row = i // 4
        x_offset = cell_size if row % 2 == 1 else 0  # Décalage horizontal alterné
        pygame.draw.rect(screen, 'light gray', [
            x_offset + (column * 2 * cell_size), row * cell_size, cell_size, cell_size]
                         )

    # Zone de pièces capturées
    sidebar_x = board_size
    pygame.draw.rect(screen, 'light gray', [sidebar_x, 0, LARGEUR - board_size, HAUTEUR])

    pygame.draw.line(screen, 'black', (board_size, 0), (board_size, sidebar_x), 2)
