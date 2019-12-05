import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
import bullet
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a group of aliens.
    aliens = Group()

    # Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                              aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship,
                             aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, play_button, ship,
                         aliens, bullets)

        # Redraw the screen during each pass.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Commented this out because aliens were flickering, this same code is
        # listed in game functions under update_screen.
        # Make the most recently drawn screen visible
        # pygame.display.flip()


run_game()
