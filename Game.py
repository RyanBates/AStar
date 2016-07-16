import pygame, sys
import pygame as gfx
import AStar
from AStar import *

def main():

 #create the search space to look through
 searchSpace = []
 for x in range(10):
	for y in range(10):
		for Start in (0, 0):
			for Goal in (8,5):
				n = Astar(searchSpace, Start, Goal, x, y)
				unwalkable = ((1,1),(0,2),(2,3),(3,1),(4,2),(2,9),(6,2),(4,5),(8,3),(5,5),(3,3),(3,4),(9,6),(7,8),(8,8),(2,7))
				beginning = (0,0)
				end = (9, 9)
				if (x, y) in unwalkable:
					unwalkable = True
				else:
					unwalkable = False
				if ((x,y) == (0,0)):
					beginning = True
				else:
					beginning = False
				if ((x,y) == (9,9)):
					end = True
				else:
					end = False
				n.setWalk(unwalkable == False)
				n.setStart(beginning == True)
				n.setGoal(end == True)
				searchSpace.append(n)
				
 # Initialize pygame
 pygame.init()

 # Set the HEIGHT and WIDTH of the screen
 WINDOW_SIZE = [255,255]
 screen = pygame.display.set_mode(WINDOW_SIZE)

 # Set title of screen
 pygame.display.set_caption("Astar")

 # Loop until the user clicks the close button.
 done = False
 
 # Used to manage how fast the screen updates
 clock = pygame.time.Clock()

# -------- Main Program Loop -----------
 while not done:
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True	 # Flag that we are done so we exit this loop

	# Set the screen background
	screen.fill((0,0,0))

	for i in searchSpace:
		i.draw(screen, (255,255,255))
		
	line = Astar(searchSpace, Start, Goal, x, y)
	line.Run(screen)
	

	# Limit to 60 frames per second
	clock.tick(60)

	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

 # Be IDLE friendly. If you forget this line, the program will 'hang'
 # on exit.
 pygame.quit()

main()