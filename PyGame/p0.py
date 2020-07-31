import pygame



screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("LEVEL 2 = Find the Correct Square!")

clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (64, 54, 16, 16))
        self.dist = 10

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
        screen.fill((255, 255, 255))
        self.rect = self.rect.move(x*self.dist, y*self.dist); pygame.draw.rect(screen, (0, 0, 128), self.rect)
        pygame.display.update()

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), (64, 54, 16, 16))

pygame.init()

player = Player()
screen.fill((255, 255, 255))
player.draw(screen)
pygame.display.update()

while True:
  player.handle_keys()