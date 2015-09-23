import pygame
import time
import random
from pygame import *
from time import sleep
pygame.init()
pygame.time.set_timer(USEREVENT + 1,5000)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)	
length=1000
width=600
block_size=10
FPS=20
lifes=3
gamedisplay=pygame.display.set_mode((length,width))
#floors=[]
#pygame.display.update()

pygame.display.set_caption('DonkeyKing')

exit=False

lead_x=0
lead_y=width
lead_x_change=0
lead_y_change=0
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,25)
gaps=[]
ladders=[]
floors=[]
sudoplayer=pygame.image.load("mario.png")
sudodevil=pygame.image.load("devi.jpeg")
sudoladder=pygame.image.load("ladder.jpeg")
sudoqueen=pygame.image.load("queen.png")
sudocoin=pygame.image.load("coin.png")
sudofire_ball=pygame.image.load("fire_ball.png")
queen=pygame.transform.scale(sudoqueen,(30,30))
fire_ball=pygame.transform.scale(sudofire_ball,(10,20))
coin=pygame.transform.scale(sudocoin,(20,20))
lad=pygame.transform.scale(sudoladder,(20,100))
player=pygame.transform.scale(sudoplayer,(10,10))
devil=pygame.transform.scale(sudodevil,(20,30))
balls=[]
class fireball():
	ball_speed=10
	def create(self,dev):
		balls.append([pygame.Rect(dev,70,block_size,block_size),1])
	def update(self):
		for ball in balls:
			if ball[1]==0:
				ball[0].x +=self.ball_speed
			else:
				ball[0].x -=self.ball_speed
			if ball[0].x <=10:
				ball[0].x=10
				ball[1]=0
			elif ball[0].x>=length-20:
				ball[0].x=length-20
				ball[1]=1
			gamedisplay.blit(fire_ball,[ball[0].x,ball[0].y,10,10])
#			pygame.display.update()
f=fireball()
def ladder():
	gamedisplay.blit(lad,[(length/2)-40,490])
	gamedisplay.blit(lad,[(3*(length/4))+20,490])
	gamedisplay.blit(lad,[80,390])
	gamedisplay.blit(lad,[length-80,390])
	gamedisplay.blit(lad,[length-30,290])
	gamedisplay.blit(lad,[length/2,290])
	gamedisplay.blit(lad,[40,190])
	gamedisplay.blit(lad,[length-180,90])
	gamedisplay.blit(lad,[180,90])
	gamedisplay.blit(lad,[3*(length/4)-20,190])

ladders.append([(length/2)-40,490])
ladders.append([(3*(length/4))+20,490])
ladders.append([80,390])
ladders.append([length-80,390])
ladders.append([length-30,290])
ladders.append([length/2,290])
ladders.append([40,190])
ladders.append([length-180,90])
ladders.append([180,90])
ladders.append([3*(length/4)-20,190])
def floor():
	pygame.draw.rect(gamedisplay,black,[0,490,length/2,block_size])
	pygame.draw.rect(gamedisplay,black,[3*(length/4),490,length/4,block_size])
	pygame.draw.rect(gamedisplay,black,[0,390,length/4,block_size])
	pygame.draw.rect(gamedisplay,black,[length/4+20,390,3*(length/4),block_size])
	pygame.draw.rect(gamedisplay,black,[0,290,3*(length/4)+40,block_size])
	pygame.draw.rect(gamedisplay,black,[length-60,290,60,block_size])
	pygame.draw.rect(gamedisplay,black,[0,190,length/4,block_size])
	pygame.draw.rect(gamedisplay,black,[3*(length/4)-40,190,length/4+40,block_size])
	pygame.draw.rect(gamedisplay,black,[0,90,length-80,block_size])
gaps.append([length/2,3*(length/4),490])
gaps.append([3*(length/4)+40,length-60,290])
gaps.append([length/4,3*(length/4)-40,190])
gaps.append([length-80,length,90])
gaps.append([length/4,length/4+20,390])
possible=[580,480,380,280,180,80]	
def heroin():
	gamedisplay.blit(queen,[10,60])
def kong(dev):
	gamedisplay.blit(devil,[dev,60])
def walls():
	pygame.draw.rect(gamedisplay,black,[0,0,length,block_size])
	pygame.draw.rect(gamedisplay,black,[0,0,block_size,width])
	pygame.draw.rect(gamedisplay,black,[0,width-10,length,block_size])
	pygame.draw.rect(gamedisplay,black,[length-10,0,block_size,width])
def hero(lead_x,lead_y,block_size):
	gamedisplay.blit(player,[lead_x,lead_y])
def message_to_screen(msg,color,x_co,y_co):
	screen_text = font.render(msg,True,color)
	gamedisplay.blit(screen_text,[x_co,y_co])
def message(msg,x,y):
	text=font.render(msg,True,red)
	gamedisplay.blit(text,[x,y])
def gameloop():
	win=False
	dev_change=10
	dev=500
	edo=0
	exit=False
	gameover=False
	lead_x=20
	lead_y=width-20
	lead_x_change=0
	lead_y_change=0
	jumped=False
	jump_y=0
	coins=[]
	score=[]
	lifes=3
	for i in range(0,10):
		coins.append(0)
		score.append(0)

	coins[0]=round(random.randrange(10,length-20)/10.0)*10.0
	coins[1]=round(random.randrange(10,length-20)/10.0)*10.0
	coins[2]=round(random.randrange(10,length/2)/10.0)*10.0
	coins[3]=round(random.randrange(3*(length/4),length-20)/10.0)*10.0
	coins[4]=round(random.randrange(10,length-20)/10.0)*10.0
	coins[5]=round(random.randrange(10,length-20)/10.0)*10.0
	coins[6]=round(random.randrange(10,3*(length/4))/10.0)*10.0
	coins[7]=round(random.randrange(length-60,length-20)/10.0)*10.0
	coins[8]=round(random.randrange(10,length/4)/10.0)*10.0
	coins[9]=round(random.randrange(3*(length/4),length-20)/10.0)*10.0
	while not exit:
		count=0
		gamedisplay.fill(white)
		while gameover == True:
			message_to_screen("game over, press c to play again or q to quit",red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key ==pygame.QUIT:
						out=1
						gameover=False
					elif event.key == pygame.K_q:
						exit=True
						gameover=False
					elif event.key == pygame.K_c:
						gameloop()
		if dev==0:
		  dev_change=10
		elif dev==length-90:
		  dev_change=-10
		dev+=dev_change
		req=0
		for i in range(0,10):
			if lead_x>=ladders[i][0] and lead_x<=ladders[i][0]+20:
				if not lead_y>=ladders[i][1] or not lead_y<ladders[i][1]+90:
					lead_y_change=0
				if lead_y>=ladders[i][1] and lead_y<ladders[i][1]+90:
					req=1
		if lead_y not in possible and req==0:
		 	lead_y=((lead_y/100)*100)+80
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit=True
				if event.type==USEREVENT + 1:
					f.create(dev)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						lead_x_change= -(block_size)
					elif event.key == pygame.K_RIGHT:
						lead_x_change= block_size
					elif event.key == pygame.K_DOWN:
						do=0
						for i in range(0,10):
							if lead_x>=ladders[i][0] and lead_x<ladders[i][0]+20:
								if lead_y>=ladders[i][1]-10 and lead_y<=ladders[i][1]+100:
									do=1
						if do==1:
						 lead_y_change= block_size
						else:
						 lead_y_change=0
					elif event.key == pygame.K_UP:
					   do=0
					   for i in range(0,10):
						   if lead_x>=ladders[i][0] and lead_x<ladders[i][0]+20:
							   if lead_y>=ladders[i][1] and lead_y<=ladders[i][1]+100:
								   do=1
					   if do==1:
					    lead_y_change= -block_size
					   else:
					    lead_y_change=0
					elif event.key == pygame.K_SPACE:
					    if jumped==False:
					    	jump_y=-60
					    	edo=lead_y
					    	jumped=True

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
						lead_x_change=0
					if event.key==pygame.K_UP or event.key==pygame.K_DOWN :
					   	lead_y_change=0
		if jumped==True:
			jump_y+=10
		lead_y+=jump_y
		if jump_y==0 and jumped==True:
			lead_y=edo
		for i in range(0,5):
			if lead_x>=gaps[i][0] and lead_x<gaps[i][1] and lead_y==gaps[i][2]-10:
					lead_y+=100

		lead_y+=lead_y_change
		lead_x+=lead_x_change
		if lead_y in possible:
		  jumped=False
		  jump_y=0
		if lead_x>length-20:
		  lead_x=length-20  
		if lead_x<10: 
		  lead_x=10
		if lead_y>width-20:
		  lead_y=width-20 
	       	if lead_y<10:
	   	  lead_y=10
		gamedisplay.fill(white)
		walls()
		floor()
		ladder()
		heroin()
		for i in range(0,10):
			if score[i]==0 :
				gamedisplay.blit(coin,[coins[i],570-((i/2)*100)])
		for i in range(0,10):
			if lead_x==coins[i] and lead_y==580-((i/2)*100):
				score[i]=1
			if score[i]==1:
			 	count+=5
		hero(lead_x,lead_y,block_size)
		kong(dev)
		message("score : "+str(count),800,20)
		message("lifes : "+str(lifes),700,20)
		for ball in balls:
			if ball[0].x==10 and ball[0].y == 570:
				balls.remove(ball)
			for i in range(0,5):
				if ball[0].x>gaps[i][0] and ball[0].x<gaps[i][1] and ball[0].y==gaps[i][2]-20:
						ball[0].y+=100
		for ball in balls:
		  	if ball[0].x==lead_x and ball[0].y==lead_y-10:
		  		lifes-=1
		  		count=count-25
		  		sleep(1)
		  	if lead_x==dev and lead_y==80:
		  		lifes=0
		  		sleep(1)

		if lifes==0:
			exit=True
		f.update()
		pygame.display.update()
		if lead_x==20 and lead_y==80:
			exit=True
			win=True
		clock.tick(FPS)
        gamedisplay.fill(white)	
	if win==False:
		message_to_screen("Game Over",red,length/2-20,width/2)
	else:
		count+=50
		message_to_screen("YOU WON",green,length/2-20,width/2)
	message_to_screen("Your score is "+str(count),red,length/2-40,width/2+40)
	pygame.display.update()
	sleep(2)
	pygame.quit()
	quit()
gameloop()
