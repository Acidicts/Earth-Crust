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
            if self.offset < 800:
                self.offset -= self.vel
                print(self.offset)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.offset > 0:
                self.offset += self.vel



    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.size)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size-2)

class layer:
    def __init__(self, thickness, color, pos=0):
        self.thickness = (thickness*1)
        self.color = color
        self.y = pos
        self.offset = 0

    def draw(self, screen, offset):
        self.offset = offset
        pygame.draw.rect(screen, self.color, (0, self.y+self.offset, 600, 10000))

def main():
    layers.append(layer(100, (255, 0, 0)))
    layers.append(layer(500, (100, 0, 0), 100))
    layers.append(layer(200, (0, 0, 255), 600))
    layers.append(layer(150, (0, 0, 100), 800))

    l_thick = 0
    x = 0

    w = False

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
            l.draw(win, player.offset)

        if player.offset < -300:
            player.offset = 0
            pygame.font.init()
            font = pygame.font.SysFont("comicsans", 100)
            w = True


        player.draw(win)

        if w:
            print("You Win!")
            text = font.render("You Win!", True, (255,255,255))
            target_x = HEIGHT // 2 - text.get_height() // 2

            if x < target_x:
                x += 1

            win.blit(text, (WIDTH//2 - text.get_width()//2, x))

        pygame.display.update()

if __name__ == "__main__":
    main()
