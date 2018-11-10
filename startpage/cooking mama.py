import pygame

from pygamegame import PygameGame
from Start import Start

#run game
class Game(PygameGame):
    def init(self):
        data.time = 0
        #start page
        self.startpage = True
        Start.init()
        start = Start(self.width / 2, self.height / 2)
        self.start = pygame.sprite.GroupSingle(start)
        # #import each page here
        # self.tenderise = import the funct
        # self.chop = import the funct
        # self.saute = import the funct
        self.tenderisePage = False:
        self.chopPage = False:
        self.sautePage = False:
    def keyPressed(self, code, mod):
        pass
        
    def mousePressed(self, posx, posy):
        #if within parameters of start button
        if (120 < posx < 400) and (580 < posy < 655) and (self.startpage == True):
            self.startpage = False
            self.tenderisePage = True


    def timerFired(self, dt):
        if self.startpage == True:
            pass
        else:
            #change each page every 10 seconds
            data.time += 1
            if data.time < 1000:
                self.tenderisePage = True
            elif 1000 < data.time < 2000:
                self.tenderisePage = False
                self.chopPage = True
            elif 2000 < data.time < 3000:
                self.chopPage = False
                self.sautePage = True
            else:
                self.sautePage = False
                self.end = True

    def redrawAll(self, screen):
        #draw each page
        if self.startpage == True:
            self.start.draw(screen)
        elif self.tenderisePage == True:
            pass
        elif self.chopPage == True:
            pass
        elif self.sautePage == True:
            pass
        else:
            #draw final page if we have

Game(520, 786).run()