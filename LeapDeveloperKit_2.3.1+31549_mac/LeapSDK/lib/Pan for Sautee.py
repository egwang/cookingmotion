import pygame
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class PygameGame(object):

    def init(self):
        self.controller = Leap.Controller()
        self.win = pygame.display.set_mode((500,500))
        self.controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)  
        self.openHand = pygame.image.load("openHand.png") 
        self.handPan = pygame.image.load("panfull.png") 
        self.panfull = pygame.image.load("panflip.png")
        self.smallMeat = pygame.image.load("smallMeat.png")
        self.fistKnife = pygame.image.load("fistknife.png")
        self.background = pygame.image.load("background.png")
        self.stove = pygame.image.load("stove.png")
        self.backgroundDim = 100
        pygame.transform.scale(self.background,(self.backgroundDim,self.backgroundDim))
        self.knifeX = 50
        self.knifeY = 250  
        self.steakX = 100
        self.steakY = 150  
        self.panFlipped = False
        self.isClosed = False
        

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass
    

    def timerFired(self, dt):
        frame = self.controller.frame()
        
        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                print("swipe")
                
        for hand in frame.hands:
            normalized = frame.interaction_box.normalize_point(hand.palm_position, True)
            currentX = int(normalized[0]*500)
            currentY = int(500-normalized[1]*500)
            currentZ = normalized[2]*0.5 + 0.5
            if hand.grab_strength > 0.5:
                smallImg = pygame.transform.rotozoom(self.handPan, 0,currentZ)

                if hand.palm_velocity[1] > 200:
                    self.swipe = True
                    self.panFlipped = True
                    smallImg = pygame.transform.rotozoom(self.panfull, 0,currentZ)
                
                if hand.palm_velocity[1] < 0:
                    self.swipe = False
                    self.panFlipped = False
                    smallImg = pygame.transform.rotozoom(self.handPan, 0,currentZ)

            else:
                self.panFlipped = False
                knife = pygame.transform.scale(self.smallMeat,(150,150))
                self.knifeX=50
                self.knifeY=250
                self.win.blit(knife,(self.knifeX,self.knifeY))
                smallImg = pygame.transform.rotozoom(self.openHand,0,currentZ)
            if self.panFlipped == True and self.steakX<self.knifeX<self.steakX+self.steakDim:
                pygame.draw.line(self.win, (0,0,0),(self.knifeX,250), (self.knifeX,500))
            
        #yeet
            self.win.blit(smallImg,(int(normalized[0]*500),500-int(normalized[1]*500)))


            print(normalized)

            pygame.display.update()
        
        
            
    def redrawAll(self, screen):
        self.win.blit(self.background, (0,0))
        self.win.blit(self.stove, (125,200))


    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()