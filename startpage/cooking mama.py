import pygame

from Mama import Mama
from pygamegame import PygameGame
from Start import Start

#run game
class Game(PygameGame):
    def init(self):
        #start page
        self.startpage = True
        Start.init()
        start = Start(self.width / 2, self.height / 2)
        self.start = pygame.sprite.GroupSingle(start)
        
    def keyPressed(self, code, mod):
        pass
        
    def mousePressed(self, posx, posy):
        #if within parameters of start button
        if (120 < posx < 400) and (580 < posy < 655) and (self.startpage == True):
            self.startpage = False
            print(posx, posy)
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        #draw start page
        if self.startpage == True:
            self.start.draw(screen)

Game(520, 786).run()