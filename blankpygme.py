import pygame, sys


from pygame.locals import *

from Scene import Scene
from Circle import Circle

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')


"""Aller, on crée une scène et on y met un objet"""

myScene = Scene(123)

myObject = Circle(50)

myScene.addEntity(myObject)

print(myScene.getEntities())

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
