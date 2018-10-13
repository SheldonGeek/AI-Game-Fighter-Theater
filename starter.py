import pygame
from vector2 import Vector2
from pytmx.util_pygame import load_pygame

from entities import EnergyStore, Hero
from game_funcs import draw_background_with_tiled_map, load_alpha_image
from settings import game_settings


def game_loop():
    game_exit = False
    pygame.init()
    pygame.display.set_caption('Python Game')
    game_screen = pygame.display.set_mode(
        game_settings.SCREEN_SIZE,
    )
    game_map = load_pygame(game_settings.MAP_DIR)
    draw_background_with_tiled_map(game_screen, game_map)
    green_energy_img = load_alpha_image('green_energy.png')
    energy_stone = EnergyStore(green_energy_img, 'green-stone')

    green_hero_img = load_alpha_image('green_hero.png')
    graves_img = load_alpha_image('graves.png')
    green_hero = Hero(green_hero_img, graves_img, 'green-hero')
    green_hero.location = Vector2(200, 200)

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        energy_stone.render(game_screen)
        green_hero.render(game_screen)

        pygame.display.update()
