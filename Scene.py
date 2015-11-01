

class Scene:

	"""Objet définissant une scène
	
	Attributs :
	- couleur du fond
	- liste des objets dans la scène
	
	"""
	
	def __init__(self,color):
		
		self.color = color
		self.entities = []
	
	def addEntity(self,entity):
		
		""""""
		self.entities.append(entity)

		
	def getBackgroundColor(self):
		
		return self.color
		
	def setBackgroundColor(self,color):	
	
		self.color=color
	
	def getEntities(self):
		
		return self.entities
	
	def printEntites(self):
		
		for entity in self.entities:
			entity.describe()