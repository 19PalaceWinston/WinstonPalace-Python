import pygame, random

pygame.init()
width = 700
height = 1000
screen = pygame.display.set_mode([width, height])
screen.fill((0,0,155))
running = True

class Player(object):
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('chrome.png'),(80,80))
        self.x = 350
        self.y = 0
        self.hitBox = (self.x + 50, self.y + 11, 29, 52)

    def collision(self):
        print("Hi")

    def handle_keys(self):
        key = pygame.key.get_pressed()
        distance = 5
        self.y += .5
        if key[pygame.K_RIGHT]:
            self.x += distance
        elif key[pygame.K_LEFT]:
            self.x -= distance

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.hitBox = (self.x, self.y, 80, 80)
        #pygame.draw.rect(screen, (255,0,0), self.hitBox,2)

class Platform(object):
    def __init__(self,xPos,yPos):
        self.image = pygame.transform.scale(pygame.image.load('Platform.png'),(200,20))
        self.x = xPos
        self.y = yPos
        self.hitBox = (self.x, self.y, 200, 22)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.hitBox = (self.x, self.y, 200, 20)
        #pygame.draw.rect(screen, (255,0,0), self.hitBox,2)

class Enemy(object):
    def __init__(self,xPos,yPos):
        self.image = pygame.transform.scale(pygame.image.load('InternetExplorer.png'),(80,80))
        self.x = xPos
        self.y = yPos
        self.hitBox = (self.x, self.y, 80, 80)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.hitBox = (self.x, self.y, 80, 80)
        #pygame.draw.rect(screen, (255,0,0), self.hitBox,2)

def update(running):
    r = 0
    b = 0
    g = 0
    rc = True
    bc = True
    rg =  True
    score = 0
    temp = []
    platforms = []
    enemies = []
    for i in range(5):
        platforms.append(Platform(random.randint(0,700),random.randint(0,700)))
    for a in range(5):
        enemies.append(Enemy(random.randint(0,700),random.randint(0,700)))
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill((0,0,155))
        #if player.y == plat.y-79.5 and player.x < plat.x + 150 and player.x > plat.x - 100:
         #   player.y = plat.y-80
        player.handle_keys()
        player.draw(screen)
        scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
        screen.blit(scoretext, (5, 10))
        for s in range(len(temp)):
            enemies.pop(temp[s])
        temp = []
        for x in range(len(platforms)):
            if player.y == platforms[x].y-79.5 and player.x < platforms[x].x + 150 and player.x > platforms[x].x - 100:
                player.y = platforms[x].y-80
            platforms[x].draw(screen)
        for z in range(len(enemies)):
            if player.y == enemies[z].y-79.5 and player.x < enemies[z].x + 150 and player.x > enemies[z].x - 100:
                temp.append(z)
                score += 1
            enemies[z].draw(screen)
        pygame.display.update()

player = Player()
myfont = pygame.font.SysFont("monospace", 16)
update(running)
pygame.quit()
