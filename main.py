import pygame

from check_options import check_options
from constantes import *
from draw_board import draw_board
from draw_pieces import draw_pieces
from helpers.draw_captured import draw_captured
from helpers.draw_check import draw_check
from helpers.draw_valid import draw_valid
from helpers.game_over import draw_game_over

# initialisation du module Pygame

pygame.init()
ecran = pygame.display.set_mode([LARGEUR, HAUTEUR])
pygame.display.set_caption("Mon Jeu d'échec. ")
minuteur = pygame.time.Clock()  # temps de mise a jour de l'interface

black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')


def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# boucle principale

run = True
while run:
    minuteur.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    ecran.fill('dark gray')
    draw_board(ecran)
    draw_pieces(ecran)
    draw_captured(ecran)
    draw_check(ecran, black_options, white_options)
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves, ecran)

    # capture des evenement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(
                        black_pieces, black_locations, 'black'
                    )
                    white_options = check_options(
                        white_pieces, white_locations, 'white'
                    )
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(
                        black_pieces, black_locations, 'black'
                    )
                    white_options = check_options(
                        white_pieces, white_locations, 'white'
                    )
                    turn_step = 0
                    selection = 100
                    valid_moves = []

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(
                    black_pieces, black_locations, 'black'
                )
                white_options = check_options(
                    white_pieces, white_locations, 'white'
                )

    if winner != '':
        game_over = True
        draw_game_over(ecran)

    pygame.display.flip()

pygame.quit()
