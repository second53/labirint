from pygame import *

win_x = 700
win_y = 500
windows = display.set_mode((win_x, win_y))

display.set_caption("Лабиринт")

bg = transform.scale(image.load("background.jpg"), (win_x, win_y))

clock = time.Clock()
FPS = 60
game = True

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
mixer.music.set_volume(0.2)

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_x - 65:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_y - 65:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_x - 65:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_y - 65:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = "left"

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
        if self.rect.x <= 420:
            self.direction = "right"
        if self.rect.x >= 620:
            self.direction = "left"





class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))



color = (99, 201, 119)

wall1 = Wall(200, 100, 400, 15, color)
wall2 = Wall(200, 100, 15, 400, color)
wall3 = Wall(600, 100, 15, 115, color)
wall4 = Wall(395, 200, 205, 15, color)
wall5 = Wall(395, 200, 15, 115, color)
wall6 = Wall(400, 400, 300, 15, color)
player = Player("hero.png", 70, 435, 5)
player2 = Player2("sprite2.png", 0, 435, 5)
enemy = Enemy("cyborg.png", 635, 300, 5)
gold = GameSprite("treasure.png", 625, 425, 0)


font.init()
font_win = font.SysFont("Arial", 70)
win = font_win.render("YOU WIN", True, (255, 215, 0))




finish = True








while game:
    windows.blit(bg, (0, 0))

    clock.tick(FPS)
    if finish == False:
        windows.blit(win, (100, 250))
    if finish == True:

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        player.reset()
        player2.reset()
        enemy.reset()
        gold.reset()
        player.update()
        player2.update()
        enemy.update()

        if sprite.collide_rect(player, enemy):
            kick.play()
            win = font_win.render("YOU LOSE!", True, (255, 215, 0))
            finish = False

        if sprite.collide_rect(player2, enemy):
            kick.play()
            win = font_win.render("YOU LOSE!", True, (255, 215, 0))
            finish = False
            
        if sprite.collide_rect(player, gold):
            money.play()
            win = font_win.render("YOU WIN, PLAYER1!", True, (255, 215, 0))
            finish = False
            
        if sprite.collide_rect(player2, gold):
            money.play()
            win = font_win.render("YOU WIN, PLAYER2!", True, (255, 215, 0))
            finish = False

        
        if sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6):
            kick.play()
            player.rect.x = 70
            player.rect.y = 435
        
        if sprite.collide_rect(player2, wall1) or sprite.collide_rect(player2, wall2) or sprite.collide_rect(player2, wall3) or sprite.collide_rect(player2, wall4) or sprite.collide_rect(player2, wall5) or sprite.collide_rect(player2, wall6):
            kick.play()
            player2.rect.x = 0
            player2.rect.y = 435




    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                finish = True
                player.rect.x = 70
                player.rect.y = 435
                player2.rect.x = 0
                player2.rect.y = 435

    display.update()