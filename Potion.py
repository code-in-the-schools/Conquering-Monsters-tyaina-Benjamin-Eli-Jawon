import pygame
import os

img_path = os.path.join('Potion.png')

#Plus 20 health


class Potion(object):
 def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Potion.image = pygame.image.load('Potion.png')

   self.image = pygame.transform.scale(self.image, (50, 50))

   self.y = 20
   self.x = 50

   def draw(self, surface):
     surface.blit(self.image, (self.x, self.y))
   