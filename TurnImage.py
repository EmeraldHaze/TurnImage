import pygame
size = [600, 600]
colors = {\
'white': 0xFFFFFF,
'red': 0xFF0000,
'green': 0x00FF00,
'blue': 0x0000FF,
'black': 0x000,
}

rules = {\
    colors['black']:('set red' ,'turn -1', 'forward 1'),
    colors['red']:('set black' ,'turn 1', 'forward 1'),
    #colors['black']:('turn 2', 'forward 1', 'set red', 'turn -4', 'forward 1', "turn -2", "forward 1", "turn 2"),
    #colors['red']:('turn 2', 'forward 1', 'set red', 'turn -4', 'forward 1', 'turn 2', 'forward 1'),
    }
    
class Head:
    dirs = [(0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1)]
    #Each index is how to move in that direction
    def __init__(self, x, y, direct):
        self.x = x
        self.y = y
        self.direct = direct
        
    def getcords(self):
        return self.x, self.y
        
    def turn(self, value):
        self.direct = (self.direct+value)%8
    
    def forward(self, value):
        change = self.dirs[self.direct]
        change = change[0]*value,change[1]*value
        self._change(change)

    def _change(self, cords):
        self.y += cords[1]
        self.x += cords[0]
        
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drawer")
    
sarr = pygame.surfarray.pixels2d(screen)

head = Head(301, 301, 0)

#Start value
sarr[299:302, 299:302] = colors["red"]
while 1:
    color = sarr[head.getcords()]
    print head.getcords(), head.direct, hex(color)
    does = rules[color]
    for do in does:
        cmd, value = do.split()
        if cmd == 'forward':
            head.forward(int(value))
            print "Forward", value, "Newps:", head.getcords()
            
        elif cmd == 'turn':
            head.turn(int(value))
            print "Turn",value, "newdirect:",head.direct
            
        elif cmd == 'set':
            sarr[head.getcords()] = colors[value]
            print 'color ', value
            pygame.display.flip()
        else:
            raise Exception, "Invalid do"
        
            
    
        
        
# -------- Wait loop-----------
print "Running"
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.flip()
            print "Quit."
            pygame.quit ()
            break

exit()
