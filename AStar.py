import Game
import Node
from Game import *
from Node import *

class Astar:

 def __init__(self, SearchSpace, Start, Goal):
	self.OPEN = []
	self.CLOSED = []
	self.nodes = SearchSpace
	self.grid_H = 10
	self.grid_W = 10
	self.start = Start
	self.goal = Goal
	self.current = self.start

 def Run(self):
	self.OPEN.append(Start)
	while not self.OPEN:
		current = self.LowestF(self.OPEN)

 def LowestF(self, Nodes):
	lowestF = -1
	nodeWithLowestF = None
	for node in Nodes:
		if(node.f > lowestF):
			lowestF = node.f
			nodeWithLowestF = node
	return nodeWithLowestF
	
 def init_grid(self):
	walls = ((1,1),(2,3),(4,2),(2,9),(6,2),(8,3))
	for x in range(self.grid_W):
		for y in range(self.grid_H):
			if (x, y) in walls:
				reachable = False
				n = Node(x,y, False)
			else:
				reachable = True
				n = Node(x,y,True)
			self.nodes.append(n)
	self.start = self.get_node(0,0)
	self.start.IsStart = True	
	self.goal.IsGoal = True
		
 def current(self, x, y):
    return self.node[x*self.grid_height + y]
	
 def GScore(self, node1, node2):
	if (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 6) or (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 1):
		return 10
	if (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 7) or (abs(self.nodes.index(node1) - self.nodes.index(node2)) == 5):
		return 14
	
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
		neighbor.g = self.GScore(node, neighbor)
		neighbor.h = self.diagonal(neighbor)
		neighbor.f = neighbor.h + neighbor.g
		neighbor.parent = node
		
 def draw_path(self, screen):
	n = self.goal
	while n.parent != None:
		gfx.draw.line(screen, purple, n.center, n.parent.center, 5)
		n = n.parent