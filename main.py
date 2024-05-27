import os
import sys
import pygame
import random

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Inicializace knihovny Pygame
pygame.init()

# Nastavení rozměrů obrazovky
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing DVD Logo Screensaver")

# Nastavení barev
black = (0, 0, 0)

# Nastavení rychlosti pohybu
speed_x = 0.1
speed_y = 0.1

# Načtení obrázku DVD loga
image_path = resource_path("dvd_logo.bmp")
dvd_logo = pygame.image.load(image_path)

# Získání rozměrů obrázku
logo_width, logo_height = dvd_logo.get_rect().size

# Počáteční umístění loga
x = random.randint(0, width - logo_width)
y = random.randint(0, height - logo_height)

# Mouse movement threshold
mouse_move_threshold = 5
last_mouse_position = pygame.mouse.get_pos()

# Hlavní smyčka programu
running = True
while running:
    screen.fill(black)
    
    # Pohyb loga
    x += speed_x
    y += speed_y
    
    # Odraz od okrajů obrazovky
    if x <= 0 or x >= width - logo_width:
        speed_x = -speed_x
    if y <= 0 or y >= height - logo_height:
        speed_y = -speed_y

    # Vykreslení loga na aktuální pozici
    screen.blit(dvd_logo, (x, y))
    
    # Aktualizace obrazovky
    pygame.display.flip()
    
    # Ošetření událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            current_mouse_position = pygame.mouse.get_pos()
            distance_moved = ((current_mouse_position[0] - last_mouse_position[0]) ** 2 + 
                              (current_mouse_position[1] - last_mouse_position[1]) ** 2) ** 2
            if distance_moved > mouse_move_threshold:
                running = False
            last_mouse_position = current_mouse_position

# Ukončení programu
pygame.quit()