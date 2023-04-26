import pygame
import random

# Oyun ekranı boyutları
WIDTH = 800
HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Rakipler
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 75]) # Rakip boyutu
        self.image.fill(WHITE) # Rakip rengi beyaz
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > HEIGHT - 75:
            self.rect.y = HEIGHT - 75

# Top
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10]) # Top boyutu
        self.image.fill(WHITE) # Top rengi beyaz
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speed = [random.randint(2, 4), random.randint(-8, 8)] # Topun hızını rastgele belirler

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.y < 0 or self.rect.y > HEIGHT - 10:
            self.speed[1] = -self.speed[1] # Topun yönünü değiştirir

        if self.rect.x > WIDTH:
            self.reset() # Topun başlangıç konumuna geri döndürür

# Oyun başlangıcı
pygame.init() # Pygame başlatılır
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # Ekran boyutları ayarlanır
pygame.display.set_caption('Pong') # Oyun başlığı belirlenir

paddle1 = Paddle(25, 250) # İlk rakibin konumu
paddle2 = Paddle(765, 250) # İkinci rakibin konumu
ball = Ball() # Top oluşturulur

all_sprites = pygame.sprite.Group() # Tüm sprite'ları tutacak bir grup oluşturulur
all_sprites.add(paddle1) # Rakip 1 gruba eklenir
all_sprites.add(paddle2) # Rakip 2 gruba eklenir
all_sprites.add(ball) # Top gruba eklenir

running = True # Oyun başlatılır
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Oyun kapatma düğmesine basılırsa, oyun durdurulur
            running = False

    keys = pygame.key.get_pressed() # Kullanıcının klavyedeki tuşlara basıp basmadığı kontrol edilir
    if keys[pygame.K_w]:  # 'w' tuşuna basılırsa
        paddle1.move_up(5)

    if keys[pygame.K_s]:  # 's' tuşuna basılırsa
        paddle1.move_down(5)
    if keys[pygame.K_UP]:  # YUKARI yön tuşuna basılırsa
        paddle2.move_up(5)
    if keys[pygame.K_DOWN]:  # AŞAĞI yön tuşuna basılırsa
        paddle2.move_down(5)

    all_sprites.update()  # Tüm sprite'ların güncellenmesi

    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.speed[0] = -ball.speed[0]  # Topun yönünü değiştirir

    if ball.rect.x < 0:
        running = False  # Oyunu durdurur

    screen.fill(BLACK)  # Ekranı siyah renkle doldurur
    all_sprites.draw(screen)  # Tüm sprite'ları ekrana çizer
    pygame.display.flip()  # Ekranı günceller
    clock.tick(60)  # Oyun hızını ayarlar
pygame.quit()