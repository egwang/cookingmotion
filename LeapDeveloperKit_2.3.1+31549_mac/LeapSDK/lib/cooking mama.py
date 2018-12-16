import pygame
<<<<<<< HEAD:startpage/cooking mama.py
from tenderize import *
from knifeInHand import *
from pygamegame import PygameGame
from StarterFile import *
=======
from pygamegame import PygameGame
from Start import Start
from tenderize import Tenderize
>>>>>>> a4fd928a1eeacb14df6910d06323f0e84a13b7d0:LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/cooking mama.py

#run game
class Game(PygameGame):
    def init(self):
<<<<<<< HEAD:startpage/cooking mama.py
        #data.time = 0
=======
        self.time = 0
>>>>>>> a4fd928a1eeacb14df6910d06323f0e84a13b7d0:LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/cooking mama.py
        #start page
        self.startpage = True
        Start.init()
        start = Start(self.width / 2, self.height / 2)
        self.start = pygame.sprite.GroupSingle(tenderize)
        # #import each page here
        # self.tenderise = pygame.sprite.GroupSingle(tenderize)
        # self.chop = import the funct
        # self.saute = import the funct
<<<<<<< HEAD:startpage/cooking mama.py
        self.tenderizePage = False
        self.chopPage = False
        self.sautePage = False
        self.gameMode = 0
        self.time = 0
=======
        self.tenderisePage = False
        self.chopPage = False
        self.sautePage = False
>>>>>>> a4fd928a1eeacb14df6910d06323f0e84a13b7d0:LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/cooking mama.py
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
<<<<<<< HEAD:startpage/cooking mama.py
            self.time += 100
            if self.time < 1000:
                self.tenderizePage = True
            elif 1000 < self.time < 2000:
                self.tenderizePage = False
=======
            self.time += 1
            if self.time < 1000:
                self.tenderisePage = True
            elif 1000 < data.time < 2000:
                self.tenderisePage = False
>>>>>>> a4fd928a1eeacb14df6910d06323f0e84a13b7d0:LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/cooking mama.py
                self.chopPage = True
            elif 2000 < self.time < 3000:
                self.chopPage = False
                self.sautePage = True
            else:
                self.sautePage = False
                self.end = True

    def redrawAll(self, screen):
        #draw each page
        
        if self.startpage == True:
            self.start.draw(screen)
        elif self.tenderizePage == True:
            
            pass
        elif self.chopPage == True:
            pass
        elif self.sautePage == True:
            pass
        else:
            pass
            #draw final page if we have
            pass

Game(520, 786).run()