import pygame



screen = pygame.display.set_mode((1200, 760))
pygame.display.set_caption("Self Driving")

image = pygame.image.load('/home/damian/Documents/Projects/TensorFlow/PyGame/Images/Shanghai.png')

clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (64, 54, 8, 8))
        self.dist = 2

    def handle_keys(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.KEYDOWN:
                key = e.key
                if key == pygame.K_LEFT:
                    self.draw_rect(-1, 0)
                elif key == pygame.K_RIGHT:
                    self.draw_rect(1, 0)
                elif key == pygame.K_UP:
                    self.draw_rect(0, -1)
                elif key == pygame.K_DOWN:
                    self.draw_rect(0, 1)
                elif key == pygame.K_ESCAPE:
                    pygame.quit(); exit()

    def draw_rect(self,x,y):
        screen.blit(image, (0, 0))
        self.rect = self.rect.move(x*self.dist, y*self.dist); pygame.draw.rect(screen, (0, 0, 128), self.rect)
        pygame.display.update()

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), (64, 54, 8, 8))

pygame.init()
player = Player()
player.draw(screen)
screen.blit(image, (0, 0))

while True:
    player.handle_keys() 
    pygame.display.update()
    