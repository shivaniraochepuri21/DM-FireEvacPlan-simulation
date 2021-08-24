import pygame
import time
import random

x = int(input())

if(x == 1):
	print("Exit 3 might be blocked!")
	print("Exit 1 for people in 1,2,5 blocks")
	print("Exit 2 for people in 6,7 blocks")
	print("Exit 4 for people in 3,4,8 blocks")

if(x == 2):
	print("Main Exit/Exit 1 might be blocked!")
	print("Exit 2 for people in 6,7 blocks")
	print("Exit 3 for people in 1,2,5 blocks")
	print("Exit 4 for people in 3,4,8 blocks")

if(x == 3):
	print("Fire on the first floor - All exits are possible")
	print("Exit 1 for people in 2,3 blocks")
	print("Exit 2 for people in 6,7 blocks")
	print("Exit 3 for people in 1,5 blocks")
	print("Exit 4 for people in 4,8 blocks")
	
pygame.init()

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Fire Emergency Evacuation Plan')
#clock.tick(100)

background_colour = (100,100,255)
white = (255,255,255)
green = (0,255,0)
black = (0,0,90)

point1 = (200,120)
point2 = (400,120)
point3 = (400,50)

point4 = (200,200)
point5 = (400,200)
point6 = (400,120)
point7 = (400,300)
point8 = (100,300)


point9 = (200, 500)
point10 = (400, 500)
point11 = (400, 540)

point12 = (600, 200)
point13 = (500, 200)
point14 = (500, 300)
point15 = (700, 300)

point16 = (600, 400)
point17 = (500, 400)

point18 = (600, 500)

point19 = (600, 120)

point20 = (200, 450)
point21 = (400,450)

line_width = 10

screen.fill(background_colour)
pygame.display.flip()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	pygame.draw.rect(screen, white, [40,30,150,100])
	pygame.draw.rect(screen, white, [40,150,150,100])
	pygame.draw.rect(screen, green, [40,260,50,100])
		
	pygame.draw.rect(screen, green, [350,10,100,50])
	pygame.draw.rect(screen, green, [350,540,100,50])

	pygame.draw.rect(screen, white, [40,370,150,100])
	pygame.draw.rect(screen, white, [40,480,150,100])
			
	pygame.draw.rect(screen, white, [620,30,150,100])	
	pygame.draw.rect(screen, white, [620,150,150,100])

	pygame.draw.rect(screen, green, [720,260,50,100])	
	pygame.draw.rect(screen, white, [620,370,150,100])
	pygame.draw.rect(screen, white, [620,480,150,100])

	textsurface = myfont.render('RoomsBlock 1', True, (0, 0, 0))
	screen.blit(textsurface,(40,30))

	textsurface = myfont.render('RoomsBlock 2', True, (0, 0, 0))
	screen.blit(textsurface,(40,150))

	textsurface = myfont.render('RoomsBlock 3', True, (0, 0, 0))
	screen.blit(textsurface,(40,370))

	textsurface = myfont.render('RoomsBlock 4', True, (0, 0, 0))
	screen.blit(textsurface,(40,480))

	textsurface = myfont.render('RoomsBlock 5', True, (0, 0, 0))
	screen.blit(textsurface,(620,30))

	textsurface = myfont.render('& Washrooms', True, (0, 0, 0))
	screen.blit(textsurface,(620,50))
		
	textsurface = myfont.render('RoomsBlock 6', True, (0, 0, 0))
	screen.blit(textsurface,(620,150))

	textsurface = myfont.render('RoomsBlock 7', True, (0, 0, 0))
	screen.blit(textsurface,(620,370))

	textsurface = myfont.render('RoomsBlock 8', True, (0, 0, 0))
	screen.blit(textsurface,(620,480))

	textsurface = myfont.render('EXIT 1', True, (255, 0, 0))
	screen.blit(textsurface,(40,300))

	textsurface = myfont.render('EXIT 2', True, (255, 0, 0))
	screen.blit(textsurface,(720,300))

	textsurface = myfont.render('EXIT 3', True, (255, 0, 0))
	screen.blit(textsurface,(370,10))

	textsurface = myfont.render('EXIT 4', True, (255, 0, 0))
	screen.blit(textsurface,(370,540))

	textsurface = myfont.render('FirePoint 1', True, (255, 0, 0))
	screen.blit(textsurface,(500,30))

	textsurface = myfont.render('FirePoint 2 & 3', True, (255, 0, 0))
	screen.blit(textsurface,(200,370))

	textsurface = myfont.render('(1st floor)', True, (255, 0, 0))
	screen.blit(textsurface,(200,390))

	######4#####
	pygame.draw.line(screen, black, point9, point10, line_width)
	pygame.draw.line(screen, black, point10, point11, line_width)
	######4#####

	######8#####
	pygame.draw.line(screen, black, point18, point10, line_width)
	######8#####

	######6#####
	pygame.draw.line(screen, black, point12, point13, line_width)
	pygame.draw.line(screen, black, point13, point14, line_width)
	pygame.draw.line(screen, black, point14, point15, line_width)
	######6#####

	######7#####
	pygame.draw.line(screen, black, point16, point17, line_width)
	pygame.draw.line(screen, black, point14, point17, line_width)
	######7#####
	pygame.display.update()

	

	if (x == 1):
		#####1######
		pygame.draw.line(screen, black, point4, point5, line_width)
		pygame.draw.line(screen, black, point5, point7, line_width)
		pygame.draw.line(screen, black, point7, point8, line_width)
		#####1######

		#####2#####
		pygame.draw.line(screen, black, point1, point2, line_width)
		pygame.draw.line(screen, black, point5, point6, line_width)
		#####2#####

		#####5#####
		pygame.draw.line(screen, black, point19, point2, line_width)
		#####5######

		####3#####
		pygame.draw.line(screen, black, point20, point21, line_width)
		pygame.draw.line(screen, black, point21, point10, line_width)
		####3####

	if (x == 2):
		#####1#####
		pygame.draw.line(screen, black, point1, point2, line_width)
		pygame.draw.line(screen, black, point2, point3, line_width)
		#####1#####

		#####2#####
		pygame.draw.line(screen, black, point4, point5, line_width)
		pygame.draw.line(screen, black, point5, point6, line_width)
		#####2#####

		#####5#####
		pygame.draw.line(screen, black, point19, point2, line_width)
		#####5#####

		####3#####
		pygame.draw.line(screen, black, point20, point21, line_width)
		pygame.draw.line(screen, black, point21, point10, line_width)
		####3####
	
	if(x == 3):
		#####1#####
		pygame.draw.line(screen, black, point1, point2, line_width)
		pygame.draw.line(screen, black, point2, point3, line_width)
		#####1#####

		#####2#####
		pygame.draw.line(screen, black, point4, point5, line_width)
		pygame.draw.line(screen, black, point5, point7, line_width)
		pygame.draw.line(screen, black, point7, point8, line_width)
		#####2#####

		#####5#####
		pygame.draw.line(screen, black, point19, point2, line_width)
		#####5#####

		####3#####
		pygame.draw.line(screen, black, point20, point21, line_width)
		pygame.draw.line(screen, black, point21, point7, line_width)
		####3####
