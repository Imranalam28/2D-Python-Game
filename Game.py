import pygame
from pygame.locals import *
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("D:\SkillBoard\Player.png")
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100
        self.velocity = pygame.math.Vector2(0,-200)
        self.acc = pygame.math.Vector2(0,5)

    

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("D:\SkillBoard\walls.png")
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y


class UpperPlatform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'D:\SkillBoard\wall2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coins(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'D:\SkillBoard\Coins.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class FullHealth(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'D:\SkillBoard\heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class PowerUp(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'D:\SkillBoard\Powerup.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'D:\SkillBoard\enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MovingPlatform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'D:\SkillBoard\movingp.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class MainGame:



    def __init__(self):
        self.run = True
        pygame.init()
        pygame.font.init()

        self.width = 640
        self.height = 480

        self.screen = pygame.display.set_mode((self.width,self.height))
        self.font = pygame.font.SysFont('Comic Sans MS',32)
        self.rect = self.screen.get_rect()
        self.bg = pygame.image.load(r'D:\SkillBoard\bg.jpg')
        self.rect_background = self.bg.get_rect()
        self.jump = False
        self.highestscore = 0
        self.camerax = 0
        self.cameray = 0
        self.score = 0
        self.distance = 0
        self.dir = 1
        self.health = 3
        self.health_image = pygame.image.load(r'D:\SkillBoard\heart.png')
        self.powerup_image = pygame.image.load(r'D:\SkillBoard\poweruplayer.png')
        self.jumpsound = pygame.mixer.Sound('D:\SkillBoard\JumpMusic.mp3')
        self.powerupsound = pygame.mixer.Sound('D:\SkillBoard\Powerupsound.mp3')
        self.power = False
        self.clock = pygame.time.Clock()
        self.check = 0
        self.p_dir = 1
        self.platformdistance = 0



        

        


    def newobject(self):

        # Sprite groups
        self.sprite_group = pygame.sprite.Group()
        self.platform = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.powerup1 = pygame.sprite.Group()
        self.powerup2 = pygame.sprite.Group()
        self.moving = pygame.sprite.Group()
        
        # Player
        self.player = Player()
        self.sprite_group.add(self.player)
        
        # Platform Addition
        self.platform1 = Platform(0,416)
        self.platform2 = Platform(64,416)
        self.platform3 = Platform(128,416)
        self.platform4 = Platform(192,416)
        self.platform5 = Platform(384,416)
        self.platform6 = Platform(448,416)
        self.platform7 = Platform(512,416)
        self.platform8 = Platform(576,416)

        #Platforms

        self.sprite_group.add(self.platform1)
        self.platform.add(self.platform1)
        self.sprite_group.add(self.platform2)
        self.platform.add(self.platform2)
        self.sprite_group.add(self.platform3)
        self.platform.add(self.platform3)
        self.sprite_group.add(self.platform4)
        self.platform.add(self.platform4)
        self.sprite_group.add(self.platform5)
        self.platform.add(self.platform5)
        self.sprite_group.add(self.platform6)
        self.platform.add(self.platform6)
        self.sprite_group.add(self.platform7)
        self.platform.add(self.platform7)
        self.sprite_group.add(self.platform8)
        self.platform.add(self.platform8)

        # UpperPlatform
        self.upper1 = UpperPlatform(128,300)
        self.upper2 = UpperPlatform(300,300)

        # UpperPlatform groups
        self.platform.add(self.upper1)
        self.sprite_group.add(self.upper1)
        self.platform.add(self.upper2)
        self.sprite_group.add(self.upper2)


        # create coins
        self.coin1 = Coins(128,180)
        self.coin2 = Coins(300,180) 
        self.coin3 = Coins(700,370) 

        # coin group
        self.coins.add(self.coin1)
        self.sprite_group.add(self.coin1)
        self.coins.add(self.coin2)
        self.sprite_group.add(self.coin2)
        self.coins.add(self.coin3)
        self.sprite_group.add(self.coin3)

        # Enemy
        self.enemy1 = Enemy(410,380)
        self.enemy2 = Enemy(135,380)

        # Enemy Group
        self.enemy.add(self.enemy1)
        self.sprite_group.add(self.enemy1)
        self.enemy.add(self.enemy2)
        self.sprite_group.add(self.enemy2)

        # HealthIncrease
        self.health1 = FullHealth(580,370)

        # Health Group
        self.powerup1.add(self.health1)
        self.sprite_group.add(self.health1)

        # PowerUp
        self.p1 = PowerUp(128,260)

        #PGROUP

        self.powerup2.add(self.p1)
        self.sprite_group.add(self.p1)

        #Moving Platform
        self.m1 = MovingPlatform(450,200)

        # MGroup
        self.sprite_group.add(self.m1)
        self.moving.add(self.m1)
        

        self.rungame()

    def rungame(self):
        
        self.running = True
        while self.running:
            self.events()
            self.updateScreen()
            self.setscreen()

    def updateScreen(self):
        
        self.sprite_group.update()
        collide = pygame.sprite.spritecollide(self.player,self.platform,False)

        if collide:
            self.player.rect.y = collide[0].rect.top - 60

        if self.score == 30:
            self.LevelCompleted()

        
        coin_collide = pygame.sprite.spritecollide(self.player,self.coins,False)

        if coin_collide:
            self.score += 10
            coin_collide[0].kill()

        enemy_collide = pygame.sprite.spritecollide(self.player,self.enemy,False)
        if enemy_collide and self.power == False:
            self.health -= 1
            self.score = 0

            if self.health == 0:
                self.run = False
                self.checkhighscore()
                self.Endscreen()
            self.newobject()

        elif enemy_collide and self.power:
            enemy_collide[0].kill()

        health_collide = pygame.sprite.spritecollide(self.player,self.powerup1,False)
        if health_collide:
            if self.health < 3:
                self.health += 1
            health_collide[0].kill()

        movingp_collide = pygame.sprite.spritecollide(self.player,self.moving,False)
        if movingp_collide:
            self.score = 0
            self.health -= 1

            if self.health == 0:
                self.run = False
                self.checkhighscore()
                self.Endscreen()
            self.newobject()

            

        if self.player.rect.x >= self.rect.x + 240:
            self.camerax += 5
            self.rect.x += 10
        
        elif self.player.rect.x < self.rect.x + 200:
            self.camerax -= 5
            self.rect.x -= 10
            

        if self.player.rect.y > 500:
            self.checkhighscore()
            self.Endscreen()

            self.run = False
            pygame.quit()
            sys.exit()

        enemy_velocity = 2
        for enemy in self.enemy:
            enemy.rect.x += enemy_velocity * self.dir
        self.distance += 1

        if self.distance >= 24:
            self.distance = 0
            self.dir *= -1

        powerup_collide = pygame.sprite.spritecollide(self.player,self.powerup2,False)
        if powerup_collide:
            self.power = True
            pygame.mixer.Sound.play(self.powerupsound)
            print("Powerup++")
            powerup_collide[0].kill()

        time = self.clock.tick()
        if self.power:
            self.check += time
            if self.check >= 6000:
                print("Powerup--")
                self.check = 0
                self.power = False

        platform_velocity = 2
        for platform in self.moving:
            platform.rect.x += platform_velocity * self.p_dir

        self.platformdistance +=1

        if self.platformdistance >= 120:
            self.platformdistance = 0
            self.p_dir *= -1


        



        


        
           

        
            

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL:
                        print("Score :- ",self.score)
                        if self.running:
                            self.running = False
                        self.run = False
                        pygame.quit()
                        sys.exit()
        

                

                if event.key == pygame.K_LEFT:
                    self.player.acc.x = -1.4
                    print("left")

                if event.key == pygame.K_RIGHT:
                    self.player.acc.x = 1.4
                    print("right")

                if event.key == pygame.K_SPACE:
                    jump_collide = pygame.sprite.spritecollide(self.player,self.platform,False)
                    if jump_collide:
                        self.jump = True
                        pygame.mixer.Sound.play(self.jumpsound)
                        

            if event.type == pygame.KEYUP:
  
                if event.key == pygame.K_LEFT:
                    self.player.acc.x = 0

                if event.key == pygame.K_RIGHT:
                    self.player.acc.x = 0
                
                if event.key == pygame.K_SPACE:
                    self.player.acc.y = 3

        self.player.velocity.x += self.player.acc.x
        self.player.rect.x = self.player.velocity.x + 0.5 * self.player.acc.x
        self.player.rect.y += self.player.acc.y
        if self.jump:
            
            self.player.rect.y += self.player.velocity.y
            self.jump = False

    def setscreen(self):
        self.screen.blit(self.bg,(0,0))
        if self.power:
            self.screen.blit(self.powerup_image,(self.player.rect.x - self.camerax - 2,self.player.rect.y - self.cameray))
        self.healthText()
        for sprite in self.sprite_group:
            self.screen.blit(sprite.image,(sprite.rect.x - self.camerax, sprite.rect.y - self.cameray))

        self.Score_display()
        pygame.display.update()
        self.screen.fill((0,0,0))

    
    def Score_display(self):
        text = self.font.render(('Score:- '+ str(self.score)),False,(255,255,255))
        rect = text.get_rect()
        self.screen.blit(text,(0,0))

    def startingscreen(self):
        self.screen.fill((0,255,255))
        text1 = self.font.render(("Ball Jump"),False,(0,0,0))
        text2 = self.font.render(("Tap any button to play"),False,(0,0,0))
        self.screen.blit(text1,(250,100))
        self.screen.blit(text2,(190,200))
        pygame.display.update()
        self.waiting()

    def Endscreen(self):
        self.screen.fill((0,255,255))
        text1 = self.font.render(("Game Over"),False,(0,0,0))
        text2 = self.font.render(("Your Score :- "+ str(self.score)),False,(0,0,0))
        text3 = self.font.render(("Press rctrl to exit"),False,(0,0,0))
        text4 = self.font.render(("Highest Score:- "+ str(self.highestscore) ),False,(0,0,0))
        self.screen.blit(text1,(250,100))
        self.screen.blit(text2,(190,200))
        self.screen.blit(text4,(180,300))
        self.screen.blit(text3,(230,400))
        pygame.display.update()
        self.waiting()


    def waiting(self):
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RCTRL:
                        self.run = False
                        pygame.quit()
                        sys.exit()
                    wait = False

    def checkhighscore(self):
        score = open('D:\SkillBoard\highscore.txt','r+')
        highscore = score.read()
        highscore_int = int(highscore)
        if self.score > highscore_int:
            print("true")
            score.seek(0)
            score.write(str(self.score))
            highscore_int = self.score
            score.truncate()

        self.highestscore = highscore_int
        score.close()

    def healthText(self):
        text = self.font.render(("Health :- "),False,(255,255,255))
        self.screen.blit(text,(200,0))
        start = 340
        for i in range(0,self.health):
            self.screen.blit(self.health_image,(start,0))
            start += 50

    def LevelCompleted(self):
        self.screen.fill((0,255,255))
        text1 = self.font.render(("Level 1 Completed"),False,(0,0,0))
        text2 = self.font.render(("Your Score :- "+ str(self.score)),False,(0,0,0))
        self.screen.blit(text1,(250,100))
        self.screen.blit(text2,(190,200))
        pygame.display.update()
        self.waiting()
                    



    



      



game = MainGame()
game.startingscreen()
while game.run:
    game.newobject()
   
