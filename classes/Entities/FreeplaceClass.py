from classes.Entities.EntityClass import Entity


class Freeplace(Entity):
    def __init__(self, screen, vec, player):
        super().__init__()
        self.image = None
        self.rect.update(screen.get_width() / 4 - vec[0] * player.speed, screen.get_height() / 4 - vec[1] ,
                                                screen.get_width() - screen.get_width() / 4 * 2 - vec[0] * player.speed,
                                                screen.get_height() - screen.get_height() / 4 * 2 - vec[1] * player.speed)