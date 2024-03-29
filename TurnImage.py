import pygame
import logging

class Head:
    dirs = [(0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1)]
    # Each index is how to move in that direction

    def __init__(self, x, y, direct):
        self.x = x
        self.y = y
        self.direct = direct

    def getcords(self):
        return self.x, self.y

    def turn(self, value):
        self.direct = (self.direct + value) % 8

    def forward(self, value):
        change = self.dirs[self.direct]
        change = change[0] * value, change[1] * value
        self._change(change)

    def _change(self, cords):
        self.y += cords[1]
        self.x += cords[0]

# configuration

head = Head(300, 300, 0)

size = [600, 600]

colors = {
    'white': 0xFFFFFF,
    'red': 0xFF0000,
    'green': 0x00FF00,
    'blue': 0x0000FF,
    'black': 0x000,
}

rules = {
    colors['black']: ('set red', 'turn 1', 'forward 2'),
    colors['red']: ('set white', "forward 3", "turn 1"),
    colors['white']: ('set red', 'turn 1', 'forward 3')
}

fps = 60
startcolor = 'black'


pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drawer")
screen.fill(colors[startcolor])

sarr = pygame.surfarray.pixels2d(screen)

print("Running")
fpscount = 0
while True:
    # Main
    color = sarr[head.getcords()]
    logging.info(head.getcords(), head.direct, hex(color))
    does = rules[color]
    for do in does:
        cmd, value = do.split()
        if cmd == 'forward':
            head.forward(int(value))
            logging.info("Forward", value, "newpos:", head.getcords())

        elif cmd == 'turn':
            head.turn(int(value))
            logging.info("Turn", value, "newdirect:", head.direct)

        elif cmd == 'set':
            sarr[head.getcords()] = colors[value]
            logging.info('color ', value)
        else:
            raise Exception("Invalid do")
    if fpscount > fps:
        pygame.display.flip()
        fpscount = 0
    else:
        fpscount += 1
    # Check for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.flip()
            print("Quit.")
            pygame.quit()
            break

exit()
