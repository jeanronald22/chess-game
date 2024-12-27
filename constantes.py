from io import BytesIO

import pygame
import requests
import os

# définition des constantes de notre jeu

# définition des dimensions de l'écran de jeu

LARGEUR = 1000
HAUTEUR = 800
fps = 60
pygame.init()
# définition des polices d'écriture
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

# variable d'images
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

# 0 - Tour des blancs, aucune pièce sélectionnée :
# 1 - Tour des blancs, pièce sélectionnée :
# 2 - Tour des noirs, aucune pièce sélectionnée :
# 3 - Tour des noirs, pièce sélectionnée.

turn_step = 0
selection = 100
valid_moves = []
path = "./chess_images/"
# url des images des piéces du jeu, d'apres l'implementation l'ordre dans la liste des obligatoirs
image_urls = [
    os.path.join(path, 'black_queen.png'),
    os.path.join(path, 'black_king.png'),
    os.path.join(path, 'black_rook.png'),
    os.path.join(path, 'black_bishop.png'),
    os.path.join(path, 'black_knight.png'),
    os.path.join(path, 'black_pawn.png'),
    os.path.join(path, 'white_queen.png'),
    os.path.join(path, 'white_king.png'),
    os.path.join(path, 'white_rook.png'),
    os.path.join(path, 'white_bishop.png'),
    os.path.join(path, 'white_knight.png'),
    os.path.join(path, 'white_pawn.png'),
]

# chargement des pieces

# je charge l'image et je retire l'arriere plan
black_queen = pygame.image.load(image_urls[0])
# je redimension l'image
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
# cette operation est effectuer sur tous les piéces restantes

black_king = pygame.image.load(image_urls[1])
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load(image_urls[2])
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load(image_urls[3])
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load(image_urls[4])
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load(image_urls[5])
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load(image_urls[6])
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load(image_urls[7])
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load(image_urls[8])
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load(image_urls[9])
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load(image_urls[10])
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load(image_urls[11])
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

# organisation des pieces dans des listes pour une meileurs exploitation
white_images = [white_pawn, white_queen, white_king,
                white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king,
                black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small,
                      black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# variables compteur
counter = 0
winner = ''
game_over = False
