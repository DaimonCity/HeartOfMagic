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

window_size = (1600, 900)
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


#Рсположение и размеры кнопок
button_rects = [
    pygame.Rect(625, 400, 400, 60),
    pygame.Rect(625, 300, 400, 60),
    pygame.Rect(625, 500, 400, 60),
    pygame.Rect(1345, 800, 200, 60)
]

button_texts = ["Продолжить", "Новая игра", "Настройки", "Выйти"]

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
                    print(f"{button_texts[i]} нажата!")

    for i, button_rect in enumerate(button_rects):
        hover = button_rect.collidepoint(pygame.mouse.get_pos())
        draw_button(button_rect, button_texts[i], hover)

    pygame.display.update()
