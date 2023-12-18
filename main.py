import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))

# Titre de la fenêtre
pygame.display.set_caption("Triv")

# Couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)

# Variables
joueur = 0
score = 0

# Fonction pour dessiner le plateau de jeu
def dessiner_plateau():
    # Dessine le fond
    fenetre.fill(noir)

    # Dessine les catégories
    for x in range(0, largeur, 100):
        for y in range(0, hauteur, 100):
            pygame.draw.rect(fenetre, blanc, (x, y, 100, 100))

    # Dessine la position du joueur
    pygame.draw.circle(fenetre, blanc, (joueur % 8 * 100 + 50, joueur // 8 * 100 + 50), 40)