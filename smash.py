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
        '''p1'''
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

    def __init__(self,x,y,radius,color,facing):
        self.x = x;
        self.y = y;
        self.radius = radius;
        self.color = color;
        self.facing = facing;
        self.vel = 8 * facing;
    def draw(self,window):
        #pygame.draw.circle(window, self.color, (self.x, self.y), self.radius);
        if p1.left:
            window.blit(self.bullet_left, (self.x-50, self.y-25))
        else:
            window.blit(self.bullet_right, (self.x, self.y-25))
    def collision(self,what):
        if bullet.y - bullet.radius < what.hitbox[1] + what.hitbox[3] and bullet.y + bullet.radius > what.hitbox[1]:
                if bullet.x + bullet.radius > what.hitbox[0] and bullet.x - bullet.radius < what.hitbox[0] + what.hitbox[2]:
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
        '''p2'''
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
    if not (p1.isJump):
        if keys[pygame.K_w]:
            p1.isJump = True;
            p1.right = False;
            p1.left = False;
            p1.runCount = 0;
    else:
        if p1.jumpCount >= -10:
            neg = 1;
            if p1.jumpCount < 0:
                neg = -1
            p1.y -= (p1.jumpCount ** 2) * 0.5 * neg;
            p1.jumpCount -= 1;

        else:
            p1.isJump = False;
            p1.jumpCount = 10; 

def jumpFunction2(keys):
    if not (p2.isJump):
        if keys[pygame.K_UP]:
            p2.isJump = True;
            p2.right = False;
            p2.left = False;
            p2.runCount = 0;
    else:
        if p2.jumpCount >= -10:
            neg = 1;
            if p2.jumpCount < 0:
                neg = -1
            p2.y -= (p2.jumpCount ** 2) * 0.5 * neg;
            p2.jumpCount -= 1;

        else:
            p2.isJump = False;
            p2.jumpCount = 10; 

class messages(object):
    #MESSAGES variables
    message01 = pygame.image.load('data/messages/01.png')
    def __init__(self,message,x,y,w,h):
        self.message = message
        self.x = x
        self.y = y
        self.w = w;
        self.h = h;
        self.text = ''

    def draw(self,window):
        if self.message == '01':
            window.blit(self.message01,(self.x,self.y));

def events(distance, what):
    if distance == 200:
        if what == 'blocks':
            return True;
    if distance == 1000:
        if what == 'fps':
            return True;
    if distance == 500:
        if what == 'p2':
            return True;
    if distance == 0:
        if what == 'space_use':
            return True;
    else:
        return False

def redrawGame():
    ''' Draws the game '''
    window.blit(background, (bgX,0))
    window.blit(background, (bgX2,0))
    p1.draw(window);
    p2.draw(window)
    text = font.render("Score: %s"%score,1,(255,255,255))
    window.blit(text, (370,10));
    if distance < 1000:
        counter = font.render(" %sm"%(distance),1,(255,255,255))
    else:
        counter = font.render(" %skm"%(distance/1000),1,(255,255,255))
    window.blit(counter, (0,10));

    for b in blocks:
        b.draw(window);
    for bullet in bullets:
        bullet.draw(window);
    #MESSAGES:
    for n in notes:
        n.draw(window)
    
    pygame.display.update();
    
    

#GAME variables
distance_unit = 'm'
distance = 0;
font = pygame.font.SysFont('comicsans',30,True);
bullets = [];
fps = 30
shootLoop = 0;
score = 0 
blocks = []

p1 = player1(200,410,64,64);
p2 = player2(screen_w-128,410,64,64)
players = [p1,p2];

use_space = []
notes = []

blocks.append(terrain(300,300,64,64))
blocks.append(terrain(screen_w-200,100,64,64))

notes.append(messages('01',100,50,64,64))

game = True;
space_event = True;
while game:

    if distance >= 1000:
        distance_unit = 'km'
    redrawGame();

    #NOTES / MESSAGES:
    
    
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

        #collision p2 bullet
        if bullet.collision(p2) == True:
                hitSound.play();
                p2.hit();
                score += 1;
                bullets.pop(bullets.index(bullet));

        if bullet.x < screen_w and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet));
            
        for b in blocks:
            #COLLISION blocks player1
            if b.collision(p1):
                p1.collision(b.x,b.y,b.w,b.h)
                jumpFunction(keys)
                jumpFunction2(keys)

            #collision p1 bullet
            if bullet.collision(p1) == True:
                    hitSound.play();
                    p1.hit();
                    score += 1;
                    bullets.pop(bullets.index(bullet));
            

        if bullet.x < screen_w and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet));
                
    for b in blocks:
        #COLLISION blocks player2
        if b.collision(p1):
            p2.collision(b.x,b.y,b.w,b.h)
            jumpFunction(keys)
            jumpFunction2(keys)
        #collision p2 bullet
            if bullet.collision(p2) == True:
                    hitSound.play();
                    p2.hit();
                    score += 1;
                    bullets.pop(bullets.index(bullet));
    #COLLISION player2 player1
    #hitbox within x and y = collision
    if p1.hitbox[1] < p2.hitbox[1] + p2.hitbox[3] and p1.hitbox[1] + p1.hitbox[3] > p2.hitbox[1]:
        if p1.hitbox[0] + p1.hitbox[2] > p2.hitbox[0] and p1.hitbox[0] < p2.hitbox[0] + p2.hitbox[2]:
            p1.hit();
            p2.hit();
            score -= 5;

    #EVENTS quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False;
            pygame.quit()
            quit()


    #EVENTS space
    if events(distance,use_space) == True:
        space_event = True;

    #KEYS press:
    keys = pygame.key.get_pressed();
    #space
    if space_event == True:
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if p1.left :
                facing = -1
            else:
                facing = 1

            if len(bullets) < 3 :
                bulletSound.play();
                bullets.append(projectile(round(p1.x + p1.w //2), round(p1.y+p1.h//2), 6, (0,94,255), facing))
            shootLoop = 1;
    
    #left
    if keys[pygame.K_a] and p1.x > p1.vel:
        p1.left = True;
        p1.x -= p1.vel;
        p1.right = False;
        p1.standing = False;
    
    #right
    elif keys[pygame.K_d]:
        p1.left = False;
        if p1.move == True:
            p1.x += p1.vel;
        p1.right = True;
        p1.standing = False;
    else:
        p1.standing = True;
        p1.runCount = 0
    
    #up
    if not (p1.isJump):
        if keys[pygame.K_w]:
            p1.isJump = True;
            p1.right = False;
            p1.left = False;
            p1.runCount = 0;
    else:
        if p1.jumpCount >= -10:
            neg = 1;
            if p1.jumpCount < 0:
                neg = -1
            p1.y -= (p1.jumpCount ** 2) * 0.5 * neg;
            p1.jumpCount -= 1;

        else:
            p1.isJump = False;
            p1.jumpCount = 10;

    #down
    if keys[pygame.K_s]:
        if not (p1.isSlide):
            p1.isSlide = True
    
    #left2
    if keys[pygame.K_LEFT] :
        p2.left = True;
        p2.x -= p2.vel;
        p2.right = False;
        p2.standing = False;
    
    #right2
    elif keys[pygame.K_RIGHT]:
        p2.left = False;
        if p2.move == True:
            p2.x += p2.vel;
        p2.right = True;
        p2.standing = False;
    else:
        p2.standing = True;
        p2.runCount = 0
    
    #up2
    if not (p2.isJump):
        if keys[pygame.K_UP]:
            p2.isJump = True;
            p2.right = False;
            p2.left = False;
            p2.runCount = 0;
    else:
        if p2.jumpCount >= -10:
            neg = 1;
            if p2.jumpCount < 0:
                neg = -1
            p2.y -= (p2.jumpCount ** 2) * 0.5 * neg;
            p2.jumpCount -= 1;

        else:
            p2.isJump = False;
            p2.jumpCount = 10;

    #down2
    if keys[pygame.K_DOWN]:
        if not (p2.isSlide):
            p2.isSlide = True
            
    clock.tick(fps);

    #END GAME:

