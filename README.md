# A-Maze-ing

## Description

A-Maze-ing est un générateur de labyrinthes écrit en Python. Il génère un labyrinthe parfait ou imparfait à partir d'un fichier de configuration, sauvegarde le résultat dans un fichier texte en utilisant un encodage hexadécimal et permet d'afficher le labyrinthe directement dans le terminal.

---

## Requirements

- Python 3.10+
- Make
- flake8
- mypy

---

## Usage

Lancer le programme avec :

```bash
python3 a_maze_ing.py config.txt
```

Le programme prend un seul argument : le fichier de configuration. Toutes les erreurs (configuration invalide, fichier absent, paramètres incorrects...) sont gérées afin d'éviter tout arrêt brutal du programme.

---

## Configuration file

Le fichier de configuration est composé de lignes sous la forme :

```text
KEY=VALUE
```

Les lignes commençant par `#` sont ignorées.

### Clés obligatoires

| Key | Type | Description |
|------|------|-------------|
| WIDTH | int | Largeur du labyrinthe |
| HEIGHT | int | Hauteur du labyrinthe |
| ENTRY | tuple(int, int) | Coordonnées de l'entrée |
| EXIT | tuple(int, int) | Coordonnées de la sortie |
| OUTPUT_FILE | string | Nom du fichier de sortie |
| PERFECT | bool | Génère un labyrinthe parfait (`True`) ou imparfait (`False`) |

### Clé optionnelle

| Key | Type | Description |
|------|------|-------------|
| SEED | int | Permet de générer toujours le même labyrinthe |

### Exemple

```text
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```

---

## Maze generation

Le projet permet de générer deux types de labyrinthes :

### Perfect maze (`PERFECT=True`)

- exactement un chemin entre l'entrée et la sortie ;
- aucun cycle.

### Imperfect maze (`PERFECT=False`)

- plusieurs chemins possibles ;
- peu d'impasses afin d'obtenir un labyrinthe plus adapté à un jeu de type Pac-Man.

Lorsque la taille du labyrinthe le permet, le logo **42** est généré au centre. :contentReference[oaicite:3]{index=3}

---

## Output file

Le fichier généré contient :

1. les cellules du labyrinthe codées en hexadécimal (un caractère par cellule) ;
2. une ligne vide ;
3. les coordonnées de l'entrée ;
4. les coordonnées de la sortie ;
5. le plus court chemin sous forme des directions :

```
N E S W
```

Les murs sont codés sur 4 bits :

| Bit | Direction |
|-----|-----------|
| 0 | North |
| 1 | East |
| 2 | South |
| 3 | West |


---

# Reusing MazeGenerator

## Import

```python
from Maze import MazeGenerator
from Color import Color
```

---

## Create a generator

```python
maze = MazeGenerator()
```

---

## Generate a maze

```python
cells = maze.main()
```

La méthode `main()` :

- charge la configuration ;
- vérifie sa validité ;
- génère le labyrinthe ;
- résout le plus court chemin ;
- écrit le résultat dans le fichier de sortie ;
- retourne les cellules du labyrinthe.

---

## Display the maze

Choisir une couleur :

```python
color = Color.WHITE
```

Afficher le labyrinthe :

```python
maze.maze_show(cells, color)
```

Le chemin peut également être affiché en passant une liste de coordonnées :

```python
maze.maze_show(cells, color, path)
```

---

## Complete example

```python
from Maze import MazeGenerator
from Color import Color

maze = MazeGenerator()

cells = maze.main()

color = Color.WHITE

maze.maze_show(cells, color)
```

---

## Project structure

```
.
├── Maze.py
├── Color.py
├── a_maze_ing.py
├── config.txt
├── output_maze.txt
└── README.md
```

---

## Utilisation de l'IA

L'intelligence artificielle a été utilisée comme outil d'aide au développement et à l'apprentissage tout au long de ce projet.

Elle m'a notamment permis de :
- mieux comprendre les consignes du sujet ;
- approfondir certains concepts Python et les algorithmes de génération de labyrinthes ;
- rédiger et améliorer la documentation (README et docstrings) ;
- relire le code afin d'identifier d'éventuelles erreurs ou pistes d'amélioration.

Toutes les réponses fournies par l'IA ont été vérifiées, comprises et adaptées avant d'être intégrées au projet. Les choix d'implémentation et le code final ont été réalisés et validés après une compréhension complète de leur fonctionnement.

L'IA a été utilisée comme un outil d'assistance et non comme un remplacement de la compréhension ou du travail personnel.