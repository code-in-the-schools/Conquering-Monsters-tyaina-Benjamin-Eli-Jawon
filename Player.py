import pygame
import os

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
     

def movement(self):
      key = pygame.key.get_pressed()

      if key[pygame.K_DOWN]:
        self.y += 1

      if key[pygame.K_UP]:
        self.y -= 1

running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

  pygame.display.update() 

  pygame.quit()

Attacks = ['Punch', 'Kick', 'Dagger']


L2 = str(input("Type an attack"))

if L2 == input('Punch'):
  Player.forward(10)
print("You have punched the monster")

if L2 == input('Kick'): 
  Player.forward(10)
print("You have kicked the monster")

if L2 == input('Dagger'): 
  Player.forward(10)
print("You have dagggered the monster")

