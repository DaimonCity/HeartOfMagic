from classes.Entities.EntityClass import Entity
from  scripts.image_scripts import load_image
class Hero(Entity):
    def __init__(self):
        super().__init__()
        self.image = load_image('entity.png')
    def move(self, vec, left, top, screen):
        x_move_t = screen.get_width() / 3 - vec[0] * self.speed < self.rect.x < screen.get_width() / 3 * 2 - vec[0] * self.speed
        y_move_t = screen.get_height() // 3 - vec[1] * self.speed < self.rect.y + vec[1] < screen.get_height() / 3 * 2 - vec[1] * self.speed
        if  x_move_t or y_move_t :
            if x_move_t:
                self.rect.x = self.rect.x + vec[0] * self.speed
            if y_move_t:
                self.rect.y = self.rect.y + vec[1] * self.speed
            self.rect.x, self.rect.y = self.rect.x + vec[0] * self.speed, self.rect.y + vec[1] * self.speed
            return left, top
        else:
            return left - vec[0] * self.speed, top - vec[1] * self.speed