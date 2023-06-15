from window import window
from menu import Menu
import pygame
import sys


# Redraws
def redraw_menu():
    # Draw menu
    menu.draw(win)

    # Update display
    pygame.display.update()


# Loops
def menu_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

        # Update display
        redraw_menu()

    pygame.quit()
    sys.exit()


# Execute
if __name__ == "__main__":
    pygame.init()

    # Initialize window
    win = pygame.display.set_mode(window.rect.size)  # !!! TEMPORARY
    pygame.display.set_caption("Math Trainer")

    # Initialize windows
    menu = Menu()
    
    # Execute
    menu_loop()
