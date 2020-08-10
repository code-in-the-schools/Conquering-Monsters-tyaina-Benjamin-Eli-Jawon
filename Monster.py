import pygame
import os
import random

img_path = os.path.join('Grey.png')
img_path = os.path.join('Pink.png')


class Player(object):
 def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Player.image = pygame.image.load('Pink.png')

   self.image = pygame.transform.scale(self.image, (50, 50))

   self.y = 50
   self.x = 50

   def draw(self, surface):
     surface.blit(self.image, (self.x, self.y))



class Monster(object):
 def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Monster.image = pygame.image.load('Grey.png')

   self.image = pygame.transform.scale(self.image, (50, 50))

   self.y = 100
   self.x = 100

   def draw(self, surface):
     surface.blit(self.image, (self.x, self.y))
   def Attack():
       PlayerHealth = 100
       if input('Punch'):
          random.randint(1,5) - PlayerHealth
          if input('Kick'):
            random.randint(1,5) - PlayerHealth
            if input('Dagger'):
                random.randint(1,5) - PlayerHealth 
 


