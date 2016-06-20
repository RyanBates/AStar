import pygame, sys
import pygame as gfx
import AStar
from AStar import *

def main():

 #create the search space to look through
 searchSpace = []
 for x in range(10):
	for y in range(10):
		for Start in (0, 1):
			for Goal in (8,5):
				n = Astar(searchSpace, Start, Goal, x, y)
				unwalkable = ((1,1),(2,3),(4,2),(2,9),(6,2),(8,3))
				start = (0, 1)
				goal = Goal
				if (x, y) in unwalkable:
					unwalkable = True
				else:
					unwalkable = False
				if (x, y) in start:
					start = True
				else:
					start = False
				n.setWalk(unwalkable == False)
				n.setStart(start == True)
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

	# Limit to 60 frames per second
	clock.tick(60)

	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

 # Be IDLE friendly. If you forget this line, the program will 'hang'
 # on exit.
 pygame.quit()

main()