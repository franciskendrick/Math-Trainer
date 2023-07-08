from window import window
from menu import Menu
from difficulty import Difficulty
from game import Game
import pygame
import sys


# Redraws
def redraw_menu():
    # Draw menu
    menu.draw(win)

    # Update display
    pygame.display.update()


def redraw_difficulty():
    # Draw difficulty
    difficulty.draw(win)

    # Update display
    pygame.display.update()


def redraw_game():
    # Draw game
    game.draw(win)

    # Update display
    pygame.display.update()


def redraw_pause():
    win.fill((235, 237, 233))

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

            # Menu buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                button_pressed = menu.buttons.button_down_detection()
                if button_pressed:
                    menu.buttons.reset_overdetection()
                    difficulty_loop(button_pressed)

            # Menu buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                menu.buttons.button_over_detection()

        # Update display
        redraw_menu()

    pygame.quit()
    sys.exit()


def difficulty_loop(game_type):
    difficulty.title.init_subtitle(game_type)
    difficulty.lvl_buttons.init_lvlbuttons(game_type)

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Difficulty buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                # Level buttons
                button_pressed = difficulty.lvl_buttons.button_down_detection()
                if button_pressed:
                    difficulty.lvl_buttons.reset_overdetection()
                    game_loop(game_type, button_pressed)

                # Back button
                button_pressed = difficulty.back_button.button_down_detection()
                if button_pressed:
                    menu_loop()

            # Difficulty buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                difficulty.lvl_buttons.button_over_detection()  # level buttons
                difficulty.back_button.button_over_detection()  # back button

        # Update display
        redraw_difficulty()
    
    pygame.quit()
    sys.exit()


def game_loop(game_type, difficulty):
    game.init(game_type, difficulty)
    game.question.get_question()

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Pause's down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                button_pressed = game.pause.button_down_detection()
                if button_pressed:
                    game.pause.reset_overdetection()
                    pause_loop()

            # Pause's over detection
            if event.type == pygame.MOUSEMOTION:
                # game.pause.button_over_detection()
                game.pause.button_over_detection()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # !!! TEMPORARY
                    game.question.get_question()

        # Update
        game.timer.update_countdown()

        # Update display
        redraw_game()

    pygame.quit()
    sys.exit()


def pause_loop():
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

        # Update display
        redraw_pause()

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
    difficulty = Difficulty()
    game = Game()

    # Execute
    menu_loop()
