import Game
from Game import *

class Node:
 def __init__(self, x, y):
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
	self.node = SearchSpace
	self.start = Start
	self.goal = Goal
	self.current = self.start
	self.nodewithLowestF = None
	self.white = (255,255,255)
	self.red = (255,0,0)
	self.blue = (0,0,255)
	self.green = (0,255,0)
	self.purple = (255,0,255)
	self.line = (0,0,0)
	self.color = self.white
	self.width = 20
	self.height = 20
	self.margin = 5
	self.left = (self.margin + self.width) *  x + self.margin
	self.top = (self.margin + self.height) *  y + self.margin
	self.pos = (x, self.height - y)
	self.center = (self.left + (self.width/2)), (self.top + (self.height/2))
	self.parent = self.current
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

 def draw_line(self, screen):
	current = self.start
	while current.parent != None:
		self.current = current.parent
		gfx.draw.line(screen, line,(current.center, current.parent.center), 5)

 def LowestF(self, Nodes):
	lowestF = nodeWithLowestF
	for node in Nodes:
		if(lowestF == None) or (node.getF() < lowestF.getF()):
			lowestF = node
	return nodeWithLowestF

 def current(self, x, y):
    return self.node(x,y)

 def GScore(self, node1, node2):
	if (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 6) or (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 1):
		return 10
	if (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 7) or (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 5):
		return 14

 def HScore(self, Start, Goal):
	(self.start.x - self.goal.x), (self.start.y - self.goal.y)

 def Nextnode(self, neighbor, node):
	if (neighbor.walkable == True):
		neighbor.g = self.GetG(node, neighbor)
		neighbor.h = self.diagonal(neighbor)
		neighbor.f = neighbor.h + neighbor.g
		neighbor.parent = node.current
		node.append(closed)

 def neighbor(self, current):
	if (node == walkable and open):
		west = current.node - 1
		east = current.node + 1
		north = current.node - width
		south = current.node + width
		northwest = current.node - width - 1
		northeast = current.node - width + 1
		southwest = current.node + width - 1
		southeast = current.node + width + 1

		wnode = SearchSpace[west]
		enode = SearchSpace[east]
		nnode = SearchSpace[north]
		snode = SearchSpace[south]
		nwnode = SearchSpace[northwest]
		nenode = SearchSpace[northeast]
		swnode = SearchSpace[southwest]
		senode = SearchSpace[southeast]

		#the cost of each move.
		wnode = 10
		enode = 10
		nnode = 10
		snode = 10
		nwnode = 14
		nenode = 14
		swnode = 14
		senode = 14 
		
 def find_path(screen, start, end, path=[]):
	path = path + [start]
	if(start == end):
		return[path]
	if(not screen.has_key(start)):
		return None
	Shortest = None
	for node in screen[start]:
		if(node not in path):
			newpath = find_path(screen, node, end, path)
			if (newpath):
				if(not shortest or len(newpath) < len(shortest)):
					shortest = newpath
	return shortest

 def Run(self, screen):
		open = self.OPEN
		closed = self.CLOSED
		open.append(current)
		if neighbor.walkable and open:
			find_path(screen, start, end)
			current = open[0]
			open.remove(current)
			closed.append(current)
			if(neighbor.walkable and neighbor not in open):
				open.append(neighbor)
				neighbor.parent = current
				neighbor.g = 10 if i < 4 else 14
			else:
				move = 10 if i < 4 else 14
				neighbor = move + current.g
				if neighbor < neighbor.g: 
					neighbor.parent = current
					neighbor.g = neighbor
			i+=1
			if goal in open:
				self.close(open)