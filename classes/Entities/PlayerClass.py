from classes.Entities.EntityClass import Entity
from  scripts.image_scripts import load_image
class Hero(Entity):
    def __init__(self):
        super().__init__()
        self.image = load_image('entity.png')