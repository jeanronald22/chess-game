import pygame

from constantes import winner, font


def draw_game_over(screen):
    # pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    # screen.blit(font.render(
    #     f'{winner} Gagne la partie!', True, 'white'), (210, 210))
    # screen.blit(font.render(f'Appuyer Entrer pour recommencer!',
    #                         True, 'white'), (210, 240))
    # Fond du message avec un rectangle arrondi
    pygame.draw.rect(screen, (0, 0, 0), [200, 200, 600, 150], border_radius=20)
    pygame.draw.rect(screen, (255, 215, 0), [200, 200, 600, 150], 5, border_radius=20)  # Bordure dorée

    # Texte : nom du gagnant avec ombre pour le contraste
    winner_text = f'{winner} Gagne la partie!'
    winner_surface = font.render(winner_text, True, (255, 255, 255))  # Texte blanc
    shadow_surface = font.render(winner_text, True, (0, 0, 0))  # Ombre noire
    screen.blit(shadow_surface, (202, 202))  # Décalage pour ombre
    screen.blit(winner_surface, (200, 200))  # Texte principal

    # Texte : message pour recommencer, avec un léger effet de style
    restart_text = 'Appuyez sur Entrer pour recommencer!'
    restart_surface = font.render(restart_text, True, (200, 200, 200))  # Texte gris clair pour moins de contraste
    shadow_restart_surface = font.render(restart_text, True, (0, 0, 0))  # Ombre noire
    screen.blit(shadow_restart_surface, (202, 240))  # Décalage pour ombre
    screen.blit(restart_surface, (200, 240))  # Texte principal