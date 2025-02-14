import sys
import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join(os.path.abspath('../../scripts/data'), name)
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

window_size = (1280, 720)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Кликабельная кнопка')

font = pygame.font.Font(None, 24)


def draw_button(button_rect, text, hover):
    button_surface = pygame.Surface((button_rect.width, button_rect.height))
    button_surface.fill((0, 0, 0))
    if hover:
        pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, button_rect.width - 2, button_rect.height - 2))
    else:
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, button_rect.width - 2, button_rect.height - 2))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, button_rect.width - 2, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, button_rect.height - 2, button_rect.width - 2, 10), 2)

    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(button_rect.width / 2, button_rect.height / 2))
    button_surface.blit(text_surface, text_rect)
    screen.blit(button_surface, button_rect.topleft)


#Изменение положения и размеров кнопок
button_rects = [
    pygame.Rect(440, 280, 400, 60),
    pygame.Rect(440, 200, 400, 60),
    pygame.Rect(440, 360, 400, 60),
    pygame.Rect(1040, 640, 200, 60)
]

button_texts = ["Продолжить", "Новая игра", "Настройки", "Выйти"]
path = os.path.abspath('../../scripts/test.py')

while True:
    clock.tick(60)
    fon = pygame.transform.scale(load_image('fon.jpg'), window_size)
    screen.blit(fon, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, button_rect in enumerate(button_rects):
                if button_rect.collidepoint(event.pos):
                    os.system(path)
                    print(f"{button_texts[i]} нажата!")
                    if button_texts[i] == "Выйти":
                        pygame.quit()
                        sys.exit()

    for i, button_rect in enumerate(button_rects):
        hover = button_rect.collidepoint(pygame.mouse.get_pos())
        draw_button(button_rect, button_texts[i], hover)

    pygame.display.update()
