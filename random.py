import pygame
import random
import numpy as np

class qbSpark:
    def init(self, initx, initv, initVx, initVy, initialColor, lifeTime):
        self.initialColor = initialColor
        self.finalColor = (0,0,0)
        self.lifetime - lifeTime
        self.initX, self.initY = initX,initY
        self.initVx, self.initVy = initVx,initVy

        self.Color = self.initialColor
        self.X = self.initX
        self.Y = self.initY
        self.fX = float(self.X)
        self.fY = float(self.Y)
        self.Vx = self.initVx
        self.Vy =  seld.initVy
        self.frameCounter = 0
        self.Active = True

        (iR,iG,iB) = self.initialColor
        (fR,fG,FB) = self.finalColor
        self.rFade = (iR - fR)/self.lifetime
        self.gFade = (iG - fG)/self.lifetime
        self.bFade = (iB - fB)/self.lifetime

    def Tick(self):
        self.fX += self.Vx
        self.fY += self.Vy
        self.X = int(self.fX)
        self.Y = int(self.fY)

        self.Vy += 0.05
        (newR, newG, newB) = self.Color
        newR = max(0,int(newR - self.rFade))
        newG = max(0,int(newG - self.gFade))
        newB = max(0,int(newB - self.bFade))
        self.Color = (newR, newG, newB)
        if (self.frameCounter >= self.lifetime):
            self.Active = False
        self.frameCounter += 1

    def Draw(self, displaySurface):
        if (self.Active):
            newRect = pygame.draw.rect(displaySuface, self.Color, pygame.Rect(self.X, self.Y, 4,4))
            return newRect
        else:
            return None

class qbFirework:
    def init(self, xLoc, yLoc, startTime, startColor):
        self.initX = xLoc
        slef.initY = yLoc
        self.startTime = startTime
        self.startColor = startColor

        self.numSparks = 100
        self.frameCounter = 0
        self.Active = True
        self.sparks = []

    def Tick(self):
        if (self.frameCounter == self.startTime):
            for i in range(0,self.numSparks):
                randDir = random.uniform(0, np.pl)
                randSpeed = random,uniform(-2,2)
                xV = randSpeed * np.sin(randDir)
                yV = randSpeed * np.cos(randDir)

                lifeTime = random.randint(30,120)

                self.sparks.append(qbSpark(self.initX, self.initY, xV, yV, self.startColor, lifeTime))
        elif(self.frameCounter > self.startTime):
            numActive = 0
            for x in self.sparks:
                x.Tick()
                if x.Active:
                    numActive += 1
                if numActive == 0:
                    self.Active = False
        else:
            pass

            self.framCounter+= 1

    def Draw(self,displaySurface):
        if (self.Active & (self.frameCounter > self.startTime)):
            for x in self.sparks:
                if x.Active:
                    x.Draw(displaySurface)

class Application:
    def init(self):
        self.isRunning = True
        self.displaySurface = None
        self.fpsClock = None
        self.firework = []
        self.size = self.width, self.heigght = 1280, 720
        self.numFireworks = 500
        self.numFrames = 1800
        self.outputCount = 0
        self.outputPath = "..."

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("You Won!")
        self.displaySurface = pygame.display.set_mode(self.size)

        for i in range(0,self.numFireworks):
            startTime = random.randint(1, self.numFrames)
            xLoc = random.randint(0,self.width)
            yLoc = random.randint(0,self.height/2)
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            self.fireworks.append(qbFirework(xLoc, yLoc, startTime,(r,g,b)))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.isRunning = False

    def on_loop(self):
        for x in self.fireworks:
            if x.Active:
                x.Tick()
    def on_render(self):
        self.displaySurface.fill((0,0,0))

        for x in self.fireworks:
            if x.Active:
                x.Draw(self.displaySurface)

        pygame.display.update()

        self.putputCount += 1

    def on_execute(self):
        if self.on_init() == False:
            self.isRunning = False

        while self.isRunning:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
        pygame.quit()
        
        
            
            
        
                    
                    
                
                
        




        

        
        
        
