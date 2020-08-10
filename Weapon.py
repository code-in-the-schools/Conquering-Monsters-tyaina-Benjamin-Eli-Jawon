import pygame
import os

img_path = os.path.join('Knife.png')


class Weapon(object):
 def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Weapon.image = pygame.image.load('Knife.png')

   self.image = pygame.transform.scale(self.image, (50, 50))

   self.y = 20
   self.x = 70

   def draw(self, surface):
     surface.blit(self.image, (self.x, self.y))