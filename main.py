import pygame

visited = []
layers = []
layer = 0

WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))


class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = 50
        self.vel = 5
        self.color = (255,0,0)
        self.offset = HEIGHT//2

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.offset -= self.vel
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.offset += self.vel



    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.size)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size-2)

class layer:
    def __init__(self, thickness, color, pos=0):
        self.thickness = (thickness*1)
        self.color = color
        self.y = pos

    def draw(self, screen, offset):
        pygame.draw.rect(screen, self.color, (0, self.y+offset, WIDTH, self.thickness+offset))

def main():
    layers.append(layer(100, (255, 0, 0)))
    layers.append(layer(5000, (100, 0, 0), 0))
    layers.append(layer(2000, (0, 0, 255), 0))
    layers.append(layer(500, (0, 0, 100), 0))

    l_thick = 0

    for i in range(len(layers)):
        if i > 0:
            layers[i].y += l_thick
        l_thick += layers[i].thickness
        print(layers[i].y)
    player = Player()

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            player.move()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break

        win.fill((180, 180, 250))

        for l in layers:
            offset = player.offset
            l.draw(win, offset)

        player.draw(win)

        pygame.display.update()

if __name__ == "__main__":
    main()
