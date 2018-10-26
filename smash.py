import pygame;
from pygame.locals import *
pygame.init();

#SCREEN variables
screen_w = 800;
screen_h = 480;
window = pygame.display.set_mode((screen_w,screen_h)); #window size
pygame.display.set_caption("X-Smash"); #game name

background = pygame.image.load('data/background/background1.jpg').convert()
bgX = 0;
bgX2 = background.get_width();

clock = pygame.time.Clock()

#SOUND variables
hitSound = pygame.mixer.Sound('data/sound/hit.wav');
bulletSound = pygame.mixer.Sound('data/sound/bullet.wav');
music = pygame.mixer.music.load('data/sound/music.wav');
pygame.mixer.music.play(-1);

class player1(object):
    #slide = [pygame.image.load(os.path.join('data', 'S1.png')),pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S3.png')), pygame.image.load(os.path.join('data', 'S4.png')), pygame.image.load(os.path.join('data', 'S5.png'))]
    jump = pygame.image.load('data/char/standing.png');
    walkRight = [pygame.image.load('data/char/R1.png'),pygame.image.load('data/char/R2.png'),pygame.image.load('data/char/R3.png'),pygame.image.load('data/char/R4.png'),pygame.image.load('data/char/R5.png'),pygame.image.load('data/char/R6.png'),pygame.image.load('data/char/R7.png'),pygame.image.load('data/char/R8.png'),pygame.image.load('data/char/R9.png')];
    walkLeft = [pygame.image.load('data/char/L1.png'),pygame.image.load('data/char/L2.png'),pygame.image.load('data/char/L3.png'),pygame.image.load('data/char/L4.png'),pygame.image.load('data/char/L5.png'),pygame.image.load('data/char/L6.png'),pygame.image.load('data/char/L7.png'),pygame.image.load('data/char/L8.png'),pygame.image.load('data/char/L9.png')]
    char = pygame.image.load('data/char/standing.png')

    def __init__(self, x, y, w, h):
        '''player'''
        self.x = x;
        self.y = y;
        self.w = w; #width
        self.h = h; #height

        self.vel = 5;
        self.isJump = False; #jumping
        self.isSlide = False; #sliding
        self.jumpCount = 10;
        self.runCount = 0;
        self.slideUp = 0;
        self.left = False;
        self.right = False;
        self.standing = True;
        self.move = True;

    def draw(self, window):
        if self.runCount + 1 >= 27:
            self.runCount = 0;
        if not (self.standing):
            if self.left:
                window.blit(self.walkLeft[self.runCount//3], (self.x,self.y))
                self.runCount += 1;
            elif self.right:
                window.blit(self.walkRight[self.runCount//3], (self.x,self.y))
                self.runCount +=1
        else:
            if self.right:
                window.blit(self.walkRight[0], (self.x,self.y));
            else:
                window.blit(self.walkLeft[0], (self.x,self.y));

        #pygame.draw.rect(window,(255,0,0), self.hitbox,2);
        self.hitbox = (self.x +17, self.y +11, 29, 52);

    def hit(self):
        self.isJump = False;
        self.jumpCount = 10;
        self.runCount = 0;
        font1 = pygame.font.SysFont('comicsans', 100);
        text = font1.render('-5',1,(255,0,0));
        window.blit(text, (250-(text.get_width()/2), 200));
        pygame.display.update();
        i = 0;
        while i < 200:
            i += 1;
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201;
                    pygame.quit()

    def collision(self,tx,ty,tw,th):
        self.isJump = False;
        self.jumpCount = 10;

        if self.y > ty:
            self.y = 410;
        if not(tx-th/2< self.x < tx+th/2) :
            self.y = 410
        

        self.runCount = 0;
        pygame.display.update();

class projectile(object):
    '''Bullet'''
    bullet_right = pygame.image.load('data/bullet/bulletR.png')
    bullet_left = pygame.image.load('data/bullet/bulletL.png')

    def __init__(self,x,y,radius,color,facing,player):
        self.x = x;
        self.y = y;
        self.radius = radius;
        self.color = color;
        self.facing = facing;
        self.vel = 8 * facing;
        self.player = player
    def draw(self,window,player):
        #pygame.draw.circle(window, self.color, (self.x, self.y), self.radius);
        if player.left:
            window.blit(self.bullet_left, (self.x-50, self.y-25))
        else:
            window.blit(self.bullet_right, (self.x, self.y-25))
            
    def collision(self,what):
        if self.y - self.radius < what.hitbox[1] + what.hitbox[3] and self.y + self.radius > what.hitbox[1]:
                if self.x + self.radius > what.hitbox[0] and self.x - self.radius < what.hitbox[0] + what.hitbox[2]:
                    return True
        else:
            return False

class player2(object):
    #slide = [pygame.image.load(os.path.join('data', 'S1.png')),pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S3.png')), pygame.image.load(os.path.join('data', 'S4.png')), pygame.image.load(os.path.join('data', 'S5.png'))]
    jump = pygame.image.load('data/char/standing.png');
    walkRight = [pygame.image.load('data/char/R1.png'),pygame.image.load('data/char/R2.png'),pygame.image.load('data/char/R3.png'),pygame.image.load('data/char/R4.png'),pygame.image.load('data/char/R5.png'),pygame.image.load('data/char/R6.png'),pygame.image.load('data/char/R7.png'),pygame.image.load('data/char/R8.png'),pygame.image.load('data/char/R9.png')];
    walkLeft = [pygame.image.load('data/char/L1.png'),pygame.image.load('data/char/L2.png'),pygame.image.load('data/char/L3.png'),pygame.image.load('data/char/L4.png'),pygame.image.load('data/char/L5.png'),pygame.image.load('data/char/L6.png'),pygame.image.load('data/char/L7.png'),pygame.image.load('data/char/L8.png'),pygame.image.load('data/char/L9.png')]
    char = pygame.image.load('data/char/standing.png')

    def __init__(self, x, y, w, h):
        '''enemy'''
        self.x = x;
        self.y = y;
        self.w = w; #width
        self.h = h; #height

        self.vel = 5;
        self.isJump = False; #jumping
        self.isSlide = False; #sliding
        self.jumpCount = 10;
        self.runCount = 0;
        self.slideUp = 0;
        self.left = False;
        self.right = False;
        self.standing = True;
        self.move = True;

    def draw(self, window):
        if self.runCount + 1 >= 27:
            self.runCount = 0;
        if not (self.standing):
            if self.left:
                window.blit(self.walkLeft[self.runCount//3], (self.x,self.y))
                self.runCount += 1;
            elif self.right:
                window.blit(self.walkRight[self.runCount//3], (self.x,self.y))
                self.runCount +=1
        else:
            if self.right:
                window.blit(self.walkRight[0], (self.x,self.y));
            else:
                window.blit(self.walkLeft[0], (self.x,self.y));

        #pygame.draw.rect(window,(255,0,0), self.hitbox,2);
        self.hitbox = (self.x +17, self.y +11, 29, 52);

    def hit(self):
        self.isJump = False;
        self.jumpCount = 10;
        #self.x = 60;
        #self.y = 410;
        self.runCount = 0;
        font1 = pygame.font.SysFont('comicsans', 100);
        text = font1.render('-5',1,(255,0,0));
        window.blit(text, (250-(text.get_width()/2), 200));
        pygame.display.update();
        i = 0;
        while i < 200:
            i += 1;
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201;
                    pygame.quit()

    def collision(self,tx,ty,tw,th):
        self.isJump = False;
        self.jumpCount = 10;

        if self.y > ty:
            self.y = 410;
        if not(tx-th/2< self.x < tx+th/2) :
            self.y = 410
        

        self.runCount = 0;
        pygame.display.update();

class terrain(object):
    block = pygame.image.load('data/terrain/block1.png')

    def __init__(self,x,y,w,h):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
    
    def draw(self,window):
        self.hitbox = (self.x + 8, self.y + 6, 50, 66);
        window.blit(self.block,(self.x,self.y));
        #pygame.draw.rect(window,(255,0,0), self.hitbox,2);
        #pygame.draw.rect(window,(255,0,0), self.hitbox,2);

    def collision(self,what):
        if what.hitbox[1] < self.hitbox[1] + self.hitbox[3] and what.hitbox[1] + what.hitbox[3] > self.hitbox[1]:
            if what.hitbox[0] + what.hitbox[2] > self.hitbox[0] and what.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                return True
        else:
            return False

def jumpFunction(keys):
    if not (player.isJump):
        if keys[pygame.K_w]:
            player.isJump = True;
            player.right = False;
            player.left = False;
            player.runCount = 0;
    else:
        if player.jumpCount >= -10:
            neg = 1;
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg;
            player.jumpCount -= 1;

        else:
            player.isJump = False;
            player.jumpCount = 10; 

def jumpFunction2(keys):
    if not (enemy.isJump):
        if keys[pygame.K_UP]:
            enemy.isJump = True;
            enemy.right = False;
            enemy.left = False;
            enemy.runCount = 0;
    else:
        if enemy.jumpCount >= -10:
            neg = 1;
            if enemy.jumpCount < 0:
                neg = -1
            enemy.y -= (enemy.jumpCount ** 2) * 0.5 * neg;
            enemy.jumpCount -= 1;

        else:
            enemy.isJump = False;
            enemy.jumpCount = 10; 


def events(distance, what):

    if distance == 500:
        if what == 'enemy':
            return True;
    else:
        return False

def redrawGame():
    ''' Draws the game '''
    window.blit(background, (bgX,0))
    window.blit(background, (bgX2,0))
    p1.draw(window);
    p2.draw(window)
    for b in blocks:
        b.draw(window);
    for bullet in bullets1:
        bullet.draw(window,p1);
    for bullet in bullets2:
        bullet.draw(window,p2)
    
    pygame.display.update();
    
def GAME(player,blocks,bullets,enemy,isPlayer1):
    '''gameplay'''
    
    shootLoop = 0;
    #BULLET COOLDOWN:
    if shootLoop > 0:
        shootLoop += 1;
    if shootLoop > 3:
        shootLoop = 0;
    #BULLETS:
    for bullet in bullets:
        for b in blocks:
            if bullet.collision(b) == True:
                hitSound.play();
                bullets.pop(bullets.index(bullet));

        #collision enemy bullet
        if bullet.collision(enemy) == True:
                hitSound.play();
                enemy.hit();
                bullets.pop(bullets.index(bullet));

        if bullet.x < screen_w and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet));
            
        for b in blocks:
            #COLLISION blocks player1
            if b.collision(player):
                player.collision(b.x,b.y,b.w,b.h)
                jumpFunction(keys)
                jumpFunction2(keys)

    #COLLISION player2 player1  #hitbox within x and y = collision
    if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
            player.hit();
            enemy.hit();

    #EVENTS quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False;
            pygame.quit()
            quit()


    #KEYS press:
    keys = pygame.key.get_pressed();
    
    if isPlayer1 == True:
        #space
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if player.left :
                facing = -1
            else:
                facing = 1

            if len(bullets) < 3 :
                bulletSound.play();
                bullets.append(projectile(round(player.x + player.w //2), round(player.y+player.h//2), 6, (0,94,255), facing,player))
            shootLoop = 1;
    
        #left
        if keys[pygame.K_a] and player.x > player.vel:
            player.left = True;
            player.x -= player.vel;
            player.right = False;
            player.standing = False;
        
        #right
        elif keys[pygame.K_d]:
            player.left = False;
            if player.move == True:
                player.x += player.vel;
            player.right = True;
            player.standing = False;
        else:
            player.standing = True;
            player.runCount = 0
        
        #up
        if not (player.isJump):
            if keys[pygame.K_w]:
                player.isJump = True;
                player.right = False;
                player.left = False;
                player.runCount = 0;
        else:
            if player.jumpCount >= -10:
                neg = 1;
                if player.jumpCount < 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) * 0.5 * neg;
                player.jumpCount -= 1;

            else:
                player.isJump = False;
                player.jumpCount = 10;

        #down
        if keys[pygame.K_s]:
            if not (player.isSlide):
                player.isSlide = True
    else:
        #enter
        if keys[pygame.K_KP_ENTER] and shootLoop == 0:
            if player.left :
                facing = -1
            else:
                facing = 1

            if len(bullets) < 3 :
                bulletSound.play();
                bullets.append(projectile(round(player.x + player.w //2), round(player.y+player.h//2), 6, (0,94,255), facing,p2))
            shootLoop = 1;
    
        #left
        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.left = True;
            player.x -= player.vel;
            player.right = False;
            player.standing = False;
        
        #right
        elif keys[pygame.K_RIGHT]:
            player.left = False;
            if player.move == True:
                player.x += player.vel;
            player.right = True;
            player.standing = False;
        else:
            player.standing = True;
            player.runCount = 0
        
        #up
        if not (player.isJump):
            if keys[pygame.K_UP]:
                player.isJump = True;
                player.right = False;
                player.left = False;
                player.runCount = 0;
        else:
            if player.jumpCount >= -10:
                neg = 1;
                if player.jumpCount < 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) * 0.5 * neg;
                player.jumpCount -= 1;

            else:
                player.isJump = False;
                player.jumpCount = 10;

        #down
        if keys[pygame.K_DOWN]:
            if not (player.isSlide):
                player.isSlide = True
    

    #END GAME:



#GAME variables
font = pygame.font.SysFont('comicsans',30,True);
bullets1 = [];
bullets2 = [];
fps = 30
shootLoop = 0;
shootLoop2 = 0;
blocks = []

p1 = player1(200,410,64,64);
p2 = player2(screen_w-128,410,64,64)

use_space = []
notes = []

blocks.append(terrain(300,300,64,64))
blocks.append(terrain(screen_w-200,100,64,64))

game = True;
space_event = True;

while game:
    redrawGame();
    GAME(p1,blocks,bullets1,p2,True);
    GAME(p2,blocks,bullets2,p1,False)
    clock.tick(fps);