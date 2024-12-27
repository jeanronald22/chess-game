# draw valid moves on screen
import pygame

from constantes import turn_step


def draw_valid(moves, screen):
    color = ''
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)