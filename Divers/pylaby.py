import pygame
import random

# Dimensions du labyrinthe
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonction pour générer un labyrinthe
def generate_maze(width, height):
    maze = [['1' for _ in range(width)] for _ in range(height)]

    # Algorithme de génération (simple DFS)
    def carve(x, y):
        maze[y][x] = '0'
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '1':
                maze[y + dy // 2][x + dx // 2] = '0'
                carve(nx, ny)

    carve(1, 1)  # Commencer à un point de départ
    return maze

# Fonction d'affichage
def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = WHITE if cell == '0' else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinthe 2D")

# Génération du labyrinthe
maze = generate_maze(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_maze(maze)
    pygame.display.flip()

pygame.quit()
