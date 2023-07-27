from window import window
from menu import Menu
from difficulty import Difficulty
from game import Game
from gameover import Gameover
import pygame
import sys


# Functions
def get_key_pressed(event):
    if event.key == pygame.K_0 or event.key == pygame.K_KP_0: return "0"
    if event.key == pygame.K_1 or event.key == pygame.K_KP_1: return "1"
    if event.key == pygame.K_2 or event.key == pygame.K_KP_2: return "2"
    if event.key == pygame.K_3 or event.key == pygame.K_KP_3: return "3"
    if event.key == pygame.K_4 or event.key == pygame.K_KP_4: return "4"
    if event.key == pygame.K_5 or event.key == pygame.K_KP_5: return "5"
    if event.key == pygame.K_6 or event.key == pygame.K_KP_6: return "6"
    if event.key == pygame.K_7 or event.key == pygame.K_KP_7: return "7"
    if event.key == pygame.K_8 or event.key == pygame.K_KP_8: return "8"
    if event.key == pygame.K_9 or event.key == pygame.K_KP_9: return "9"


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


def redraw_gameover():
    # Draw gameover
    gameover.draw(win)

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
    stats = {
        "score": 0,
        "key_presses": 0,
        "wrg_ans": 0,
        "mistakes": 0
    }

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Input's key detection
            if event.type == pygame.KEYDOWN:
                # Popping at input's text list
                if event.key == pygame.K_BACKSPACE:
                    game.input.update_text("BS")
                    stats["mistakes"] += 1

                # Appending to input's text list
                key = get_key_pressed(event)
                if key != None:
                    efficient_press = game.input.update_text(key)
                    if efficient_press:
                        stats["key_presses"] += 1
                    else:
                        stats["mistakes"] += 1

                # Switch input's append direction
                if event.key == pygame.K_SPACE:
                    game.input.on_left = not game.input.on_left
                    game.inputappend_title.on_left = not game.inputappend_title.on_left

                # Submiting input
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if game.question.answer == game.input.get_intinput():
                        game.bg_color = game.bg_colors["correct"]
                        game.time_remaining = 2
                        game.bg_changed = True

                        game.question.get_question()
                        game.input.text = []

                        stats["score"] += 1
                    else:
                        game.bg_color = game.bg_colors["wrong"]
                        game.time_remaining = 2
                        game.bg_changed = True

                        stats["wrg_ans"] += 1

        # Update
        game.timer.update_countdown()
        game.update_background()

        # Redirect to gameover loop
        if game.timer.time_remaining <= 0:
            game.reset_background()
            gameover_loop(game_type, difficulty, stats)

        # Update display
        redraw_game()

    pygame.quit()
    sys.exit()


def gameover_loop(game_type, difficulty, stats):
    gameover.init(game_type, difficulty)
    gameover.statistics.init_stats(stats)

    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Gameover buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                button_pressed = gameover.buttons.button_down_detection()
                if button_pressed == "restart":
                    gameover.buttons.reset_overdetection()
                    game_loop(game_type, difficulty)
                elif button_pressed == "menu":
                    gameover.buttons.reset_overdetection()
                    menu_loop()

            # Gameover buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                gameover.buttons.button_over_detection()

        # Update display
        redraw_gameover()

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
    gameover = Gameover()

    # Execute
    menu_loop()
