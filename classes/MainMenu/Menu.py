import sys
import pygame
import os

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image

pygame.init()

clock = pygame.time.Clock()

window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Кликабельная кнопка')

font = pygame.font.Font(None, 24)

button_surface = pygame.Surface((150, 50))

text = font.render("Click Me", True, (0, 0, 0))
text_rect = text.get_rect(
    center=(button_surface.get_width() / 2,
            button_surface.get_height() / 2))

button_rect = pygame.Rect(125, 125, 150, 50)  # Менять положение кнопки

while True:
    clock.tick(60)
    fon = pygame.transform.scale(load_image('fon.jpg'), window_size)
    screen.blit((fon), (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

    button_surface.blit(text, text_rect)

    screen.blit(button_surface, (button_rect.x, button_rect.y))

    pygame.display.update()