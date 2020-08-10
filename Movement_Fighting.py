import pygame
pygame.init()

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


