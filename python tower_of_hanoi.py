import pygame
import sys
import time

def draw_pole(screen, pole_name, x):
    pygame.draw.rect(screen, (0, 0, 255), (x - 5, 150, 10, 350))
    font = pygame.font.Font(None, 36)
    text = font.render(pole_name, True, (0, 0, 0))
    screen.blit(text, (x - 15, 510))

def draw_disk(screen, size, color, x, y):
    pygame.draw.rect(screen, color, (x - size // 2, y, size, 20))

def draw_towers(screen, towers):
    screen.fill((255, 255, 255))
    poles = {'A': 200, 'B': 500, 'C': 800}
    for pole, disks in towers.items():
        draw_pole(screen, pole, poles[pole])
        height = 450
        for disk in disks:
            draw_disk(screen, disk * 20, (128, 128, 128), poles[pole], height)
            height -= 20
    pygame.display.flip()
    time.sleep(1)

def tower_of_hanoi_graphics(screen, n):
    towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    moves = []

    def move_disk(disk, from_pole, to_pole):
        towers[from_pole].remove(disk)
        towers[to_pole].append(disk)
        moves.append(f"Move disk {disk} from {from_pole} to {to_pole}")
        draw_towers(screen, towers)

    def tower_of_hanoi_recursive(n, source, target, auxiliary):
        if n > 0:
            tower_of_hanoi_recursive(n-1, source, auxiliary, target)

            move_disk(n, source, target)

            tower_of_hanoi_recursive(n-1, auxiliary, target, source)

    draw_towers(screen, towers)
    tower_of_hanoi_recursive(n, 'A', 'C', 'B')

    return moves

# Example Usage with User Input
pygame.init()

running = True
while running:
    num_disks = int(input("Enter the number of disks: "))

    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Tower of Hanoi")

    moves = tower_of_hanoi_graphics(screen, num_disks)

    print("\nAll moves:")
    for move in moves:
        print(move)

    print("\nDisplaying moves one by one. Close the window to end the animation.")

    # Display moves one by one
    for move in moves:
        # Wait for user to close the Pygame window
        waiting_for_quit = True
        while waiting_for_quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_quit = False
                    running = False
                    pygame.quit()
                    sys.exit()
