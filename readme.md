Voici un modèle de **README** pour un projet de jeu d'échecs :

---

# Jeu d'Échecs en Python avec Pygame

## Description

Ce projet est un jeu d'échecs 2D développé en Python en utilisant la bibliothèque Pygame. Il permet aux utilisateurs de jouer à un jeu d'échecs classique, avec des graphismes simples mais attractifs, et des règles de base du jeu d'échecs.

Le jeu propose une interface graphique qui affiche l'échiquier avec des pièces et gère les règles des mouvements des pièces, la détection de la victoire, et la possibilité de recommencer une partie après une victoire.

## Fonctionnalités

- Échiquier 8x8 classique
- Gestion des mouvements de toutes les pièces (roi, reine, tour, cavalier, fou, pion)
- Prise en charge des règles de base du jeu d'échecs
- Détection de la victoire
- Possibilité de recommencer la partie après une victoire
- Interface graphique intuitive avec des pièces visuellement distinctes
- Support pour le déplacement et la prise de pièces
- Gestion des tours de jeu alternées entre le joueur blanc et le joueur noir

## Prérequis

Pour exécuter ce jeu, vous avez besoin des éléments suivants :

- **Python** : Version 3.x ou supérieure
- **Pygame** : Bibliothèque graphique pour Python, qui peut être installée via pip

## Installation

### 1. Installer Python

Téléchargez et installez Python à partir de [python.org](https://www.python.org/downloads/).

### 2. Installer Pygame

Installez la bibliothèque Pygame en exécutant la commande suivante dans votre terminal :

```bash
pip install pygame
```

### 3. Cloner le Référentiel

Clonez ce projet sur votre machine locale :

```bash
git https://github.com/jeanronald22/chess-game.git
```

### 4. Lancer le jeu

Naviguez vers le répertoire du projet cloné et lancez le jeu en exécutant le fichier principal :

```bash
cd "chess-game"
python main.py
```

## Utilisation

1. **Début de la partie** : Cliquez sur les pièces pour les déplacer.
2. **Mouvements** : Cliquez une première fois sur une pièce, puis sur une case valide pour la déplacer.
3. **Conditions de victoire** : La partie se termine dès qu'un roi est mis en échec et mat.
4. **Recommencer** : Après une victoire, appuyez sur `Entrée` pour recommencer une nouvelle partie.

## Commandes Clavier

- **Entrée** : Redémarre la partie après une victoire

## Structure du Projet

Voici une vue d'ensemble de la structure du projet :

```
/chess-game
│
├── /chess-images            # Dossier contenant les images des pièces d'échec (blanches et noires)
│   ├── white_king.png
│   ├── white_queen.png
│   ├── black_king.png
│   ├── black_queen.png
│   └── ...            # Autres pièces d'échec
├──/ helpers                 # Dossier contenqnt les fonctions de validations
│
├── main.py            # Fichier principal contenant le code pour exécuter le jeu
├── .....
├── draw_board.py      # Définition de l'échiquier
└── readme.md          # Ce fichier
```

### Pour contribuer :

1. Fork ce projet.
2. Créez une branche pour chaque nouvelle fonctionnalité ou correction.
3. Assurez-vous que les tests passent avant de soumettre votre pull request.

## Auteurs

- **RONALD MBOUMGNI**
