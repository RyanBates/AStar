import Game
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
  
class Astar:

 def __init__(self, SearchSpace, Start, Goal):
	self.OPEN = []
	self.CLOSED = []
	self.node = SearchSpace
	self.start = Start
	self.goal = Goal
	self.current = self.start

 def LowestF(self, Nodes):
	lowestF = -1
	nodeWithLowestF = None 
	for node in Nodes:
		if(node.f > lowestF):
			lowestF = node.f
			nodeWithLowestF = node
	return nodeWithLowestF
		
 def current(self, x, y):
    return self.node[x + y]
	
 def GetG(self, node1, node2):
	if (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 6) or (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 1):
		return 10
	if (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 7) or (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 5):
		return 14

 def GetH(self, node):
	(self.start.x - self.goal.x),(self.start.y - self.goal.y)
	
 def neighbor(self, Node):
  nodes = []
  if node.walkable == True:
		if node.x < self.grid_width-1:
			nodes.append(self.current(node.x+1, node.y))
		if node.y > 0:
			nodes.append(self.current(node.x, node.y-1))
		if node.x > 0:
			nodes.append(self.current(node.x-1, node.y))
		if node.y < self.grid_height-1:
			nodes.append(self.current(node.x, node.y+1))
  return nodes

 def Nextnode(self, neighbor, node): 
	if neighbor.walkable == True:
		neighbor.g = self.GetG(node, neighbor)
		neighbor.h = self.diagonal(neighbor)
		neighbor.f = neighbor.h + neighbor.g
		neighbor.parent = node
		 
	
 def draw_path(self, screen):
	n = self.goal
	while n.parent != None:
		gfx.draw.line(screen, purple, n.center, n.parent.center, 5)
		n = n.parent
				
 def Run(self, screen):
		self.Reset()
		open = self.OPEN
		closed = self.CLOSED
		start = self._start
		goal = self._goal
		open.append(start)
		while open:						
			open.sort(key = lambda x : x.f)
			current = open[0]
			open.remove(current)			
			closed.append(current)
			i = 0
			for neighbor in current:
				if neighbor.walkable and neighbor not in closed:
					if neighbor not in open:
						open.append(neighbor)
						neighbor.parent = current						
						neighbor.g = 10 if i < 4 else 14
					else:
						move = 10 if i < 4 else 14
						movecost = move + current.g
						if movecost < neighbor.g: 
							neighbor.parent = current						
							neighbor.g = movecost
							
				i+=1
			if goal in open:
				self.PATH = self.GetPath(goal)
				break;