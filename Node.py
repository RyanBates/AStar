import AStar
import Game
from AStar import *
from Game import *

class Node:
 def __init__(self, x, y):
	self.parent = None
	self.color = (255,255,255)	#walkable color
	self.width = 20
	self.height = 20
	self.margin = 5
	self.left = (self.margin + self.width) *  x + self.margin
	self.top = (self.margin + self.height) *  y + self.margin
	self.pos = (x, self.height - y)
	self.center = (self.left + (self.width/2)), (self.top + (self.height/2))
	self.g = None
	self.f = None
	self.h = None
	self.walkable = True
	 
 def draw(self, screen, color):
 	margin = self.margin
 	color = self.color if (self.walkable) else (255,0,0)
	if (self.IsStart == True):
		color = (0,0,255)
	if (self.IsGoal == True):
		color = (0,255,0)
 	gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))

 def setWalk(self, walkable):
  self.walkable = walkable

 def setH(self, val):
  self.h = val
 def setG(self, val):
  self.g = val
 def getF(self):
  if (self.h and self.g == None):
   self.h = 0
   self.g = 0
   self.f = self.h + self.g
  return self.f