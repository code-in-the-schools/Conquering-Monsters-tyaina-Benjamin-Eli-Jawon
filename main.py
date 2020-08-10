import pygame
import os
import random
 
img_path = os.path.join('Grey.png')
img_path = os.path.join('Pink.png')
img_path = os.path.join('Potion.png')
img_path = os.path.join('Knife.png')

class Potion(object):
 def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Potion.image = pygame.image.load('Potion.png')

   self.image = pygame.transform.scale(self.image, (50, 50))

   self.y = 20
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
       MonsterAttack = random.randint(5,10)
       if input('Punch'):
          MonsterAttack - PlayerHealth

class Player(object):
  def __init__(self):
   pygame.sprite.Sprite.__init__(self)

   Player.image = pygame.image.load('Pink.png')

   self.image = pygame.transform.scale(self.image, (50, 50))

   
   self.x = 50
   self.y = 50

  def draw(self, surface):
     surface.blit(self.image, (self.x, self.y))
 
  def Inventory(self):
      Inventory = []

       #repl loves to complain
    if Player(self.x and self.y)  == Potion(self.x and self.y):
     Potion.append(Inventory)
     print(Inventory)
  
  def HealthBar():
      MonsterAttack = random.randint(5,10)
      MonsterHealth = 100
      while MonsterHealth != 0 and 'Punch' in Attacks:
       b = input('Attack with weapon? YES or NO. ')
      print(b)
      if b == 'YES':
        c =input('Choose your weapon')
      if c == 'Punch':
        MonsterHealth = MonsterHealth - 5
      if c == 'Block':
          MonsterAttack = MonsterAttack // 2
    
      if MonsterHealth == 0:
        print('CONGRADULATIONS you have defated the monster!Advaced to next level')


def movement(self):
      key = pygame.key.get_pressed()

      if key[pygame.K_DOWN]:
        self.y += 1

      if key[pygame.K_UP]:
        self.y -= 1

Attacks = ['Punch', 'Block']

L2 = str(input("Type an attack"))

if L2 == input('Punch'):
  Player.forward(10)
print("You have punched the monster")

if L2 == input('Block'): 
  Player.forward(10)
print("You have kicked the monster")


  


          
pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))


running = True
Players = Player()
Monsters = Monster()
Potions = Potion()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    screen.fill((255, 255, 255))
    Players.draw(screen)
    Players.HealthBar(screen)
    Monsters.draw(screen)
    Potions.draw(screen)
    pygame.display.update()                     
   