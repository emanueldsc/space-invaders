import sys
import pygame

def check_events(ship):
	# Responds to events when keyborad press
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_rigth = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_rigth = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False

def update_screen(ia_settings, screen, ship):
	# Update images in screen to new screen
	screen.fill(ia_settings.bg_color)
	ship.blitme()
	pygame.display.flip()