import Game
from Game import *

class Node:
 def __init__(self, x, y, walkable):
	self.width = 20
	self.height = 20
	self.margin = 5
	self.g = None
	self.f = None
	self.h = None
	self.walkable = True

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
 def __init__(self, SearchSpace, Start, Goal, x, y):
	self.OPEN = []
	self.CLOSED = []
	self.path = []
	self.node = SearchSpace
	self.start = Start
	self.goal = Goal
	self.current = self.start
	self.NodeWithLowestF = None
	self.white = (255,255,255)
	self.red = (255,0,0)
	self.blue = (0,0,255)
	self.green = (0,255,0)
	self.purple = (255,0,255)
	self.color = self.white
	self.width = 20
	self.height = 20
	self.margin = 5
	self.left = (self.margin + self.width) * x + self.margin
	self.top = (self.margin + self.height) * y + self.margin
	self.pos = (x, self.height - y)
	self.center = (self.left + (self.width/2)), (self.top + (self.height/2))
	self.parent = None
	self.walkable = True

 def setWalk(self, walkable):
	self.walkable = walkable

 def setStart(self, Start):
	self.start = Start

 def setGoal(self, Goal):
	self.goal = Goal

 def draw(self, screen, color):
 	margin = self.margin
 	color = self.white if (self.walkable) else self.red
	if (self.start == True):
		color = self.blue
	if (self.goal == True):
		color = self.green
 	gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
	
 def Parent(self, current, center):
	if self.current == self.start:
		self.parent = self.start
		if self.start > NodeWithLowestF:
			self.parent = NodeWithLowestF
			if NodeWithLowestF > NodeWithLowestF:
				self.parent = NodeWithLowestF

 def current(self, x, y):
	return self.Node(x + self.height + y)
	self.Node = CLOSED

 def LowestF(self, node):
	lowestF = NodeWithLowestF
	for Node in node:
		if(lowestF == None) or (Node.getF() <= lowestF.getF()):
			lowestF = current.Node
	return NodeWithLowestF

 def HScore(self, Start, Goal):
	(self.start.x.id - self.goal.x.id), (self.start.y.id - self.goal.y.id)
	
 def GScore(self, node1, node2):
	if (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 6) or (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 1):
		return 10
	if (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 7) or (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 5):
		return 14

 def neighbor(self, current):
	if (Node == walkable):
		Node = OPEN
		west = current.Node - 1
		east = current.Node + 1
		north = current.Node - width
		south = current.Node + width
		northwest = current.Node - width - 1
		northeast = current.Node - width + 1
		southwest = current.Node + width - 1
		southeast = current.Node + width + 1
		
		wNode = SearchSpace[west].GScore 
		eNode = SearchSpace[east].GScore 
		nNode = SearchSpace[north].GScore
		sNode = SearchSpace[south].GScore
		nwNode = SearchSpace[northwest].GScore
		neNode = SearchSpace[northeast].GScore
		swNode = SearchSpace[southwest].GScore
		seNode = SearchSpace[southeast].GScore
		
 def print_path(self): 
	node = self.goal
	while node.parent is not self.start:
		node = node.parent
		print 'path: node: %d,%d' % (node.x, node.y)
		
 def draw_path(self, screen):
	n = self.goal
	while self.parent != self.start:
		gfx.draw.line(screen, self.purple, self.start, self.goal, 5)
		n = self.parent

 def find_path(self, grid, SearchSpace, start, goal):
	path = []
	self.path = path + [start]
	current = self.start
	if(start == goal):
		return[path]
	else:
		return[path]
	Shortest = None
	for Node in grid[start]:
		if(Node not in path):
			newpath = find_path(grid, Node, goal, path)
			if (newpath):
				if(not shortest or len(newpath) < len(shortest)):
					newpath = shortest
	return newpath

 def Run(self, screen):
	open = self.OPEN
	close = self.CLOSED
	self.current = self.start
	self.parent = self.current
	close.append(self.current)
	if self.neighbor == self.walkable and open:
		if self.neighbor <= lowestF:
			self.neighbor = new.current
	else:
		self.neighbor > self.NodeWithLowestF
		if self.neighbor > self.NodeWithLowestF:
			self.walkable == False
	if self.goal is open:
		self.draw_path(screen)
		return False
	else:
		self.draw_path(screen)
		return True