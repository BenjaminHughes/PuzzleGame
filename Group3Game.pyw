#!/usr/bin/env

import pygame
from pygame.locals import *
import math
import random
import sys, os
sys.path.append( os.getcwd() )
import pginput

class GameClass(object):
    def __init__(self):     

        # Defines - DJH
        self.DISPLAY_WIDTH = 640
        self.DISPLAY_HEIGHT = 480
        self.BOAT_L = 160
        self.BOAT_R = 270
        self.BOAT_Y = 245
        self.OBJVANISH_X = -200
        self.OBJVANISH_Y = -200
        self.WOLF_XL = 5
        self.WOLF_XR = 455
        self.WOLF_Y = 220
        self.SHEEP_XL = 88
        self.SHEEP_XR = 550
        self.SHEEP_Y = 220
        self.CABBAGE_XL = 73
        self.CABBAGE_XR = 525
        self.CABBAGE_Y = 260
        self.SND_BACKGROUND_VOL = 0.7
        self.start()

    # Initial set up code
    def setup(self):

        self.water_size = ( 274, 190 )
        self.wave_size = ( 267, 17 )
        self.sndMute = False
        self.sndBackgroundM = False
        self.sndBackgroundG = False
        self.themeSun = False
        self.themeNight = False
        self.themeHallow = True
        self.cloud_anim = 0
        self.cloud_anim_change = 50
        self.boatObj = ""
        self.boatItem = False
        self.m_snowflakes = []
        for i in range( 20 ):
            self.m_snowflakes.append( ( random.random() * self.DISPLAY_WIDTH, random.random() * self.DISPLAY_HEIGHT ) )
        # DJH - image loads
        self.i_Back = pygame.image.load("img\\menu-back.png").convert_alpha()
        self.background1 = pygame.image.load("img\\background.png").convert()
        self.background2 = pygame.image.load("img\\background2.png").convert()
        self.i_water1 = pygame.image.load( 'img\\river.png' ).convert_alpha()
        self.i_water2 = pygame.image.load( 'img\\river-dark.png' ).convert_alpha()
        self.s_waterSurface = pygame.Surface( self.water_size, pygame.SRCALPHA )
        self.i_CloudOne1 = pygame.image.load("img\\cloud-one.png").convert_alpha()
        self.i_CloudTwo1 = pygame.image.load("img\\cloud-two.png").convert_alpha()
        self.i_CloudOne2 = pygame.image.load("img\\cloud-one-dark.png").convert_alpha()
        self.i_CloudTwo2 = pygame.image.load("img\\cloud-two-dark.png").convert_alpha()
        self.i_BankL1 = pygame.image.load("img\\bank_l.png").convert_alpha()
        self.i_Bankr1 = pygame.image.load("img\\bank_r.png").convert_alpha()
        self.i_BankL2 = pygame.image.load("img\\bank_l2.png").convert_alpha()
        self.i_Bankr2 = pygame.image.load("img\\bank_r2.png").convert_alpha()
        self.i_Wolf1 = pygame.image.load("img\\game-wolf.png").convert_alpha()
        self.i_WolfE1_1 = pygame.image.load("img\\game-wolf-eat-one.png").convert_alpha()
        self.i_WolfE2_1 = pygame.image.load("img\\game-wolf-eat-two.png").convert_alpha()
        self.i_Sheep1 = pygame.image.load("img\\game-sheep.png").convert_alpha()
        self.i_SheepE1_1 = pygame.image.load("img\\game-sheep-eat-one.png").convert_alpha()
        self.i_SheepE2_1 = pygame.image.load("img\\game-sheep-eat-two.png").convert_alpha()
        self.i_Cabbage1 = pygame.image.load("img\\game-cabbage.png").convert_alpha()
        self.i_Wave1 = pygame.image.load("img\\game-wave.png").convert_alpha()
        self.s_waveSurface = pygame.Surface( self.wave_size, pygame.SRCALPHA )
        self.i_menuS = pygame.image.load("img\\menu-start.png").convert_alpha()
        self.i_menuR = pygame.image.load("img\\menu-rules.png").convert_alpha()
        self.i_menuH = pygame.image.load("img\\menu-highscore.png").convert_alpha()
        self.i_menuC = pygame.image.load("img\\menu-credits.png").convert_alpha()
        self.i_gameOl = pygame.image.load("img\\gameover-lose.png").convert_alpha()
        self.i_gameBl = pygame.image.load("img\\gameover-back.png").convert_alpha()
        self.i_gameOw = pygame.image.load("img\\gameover-win.png").convert_alpha()
        self.i_gameBw = pygame.image.load("img\\gameover-back.png").convert_alpha()
        self.i_Boatb1 = pygame.image.load("img\\game-boat.png").convert_alpha()
        self.i_Boatw1 = pygame.image.load("img\\game-boat-wolf.png").convert_alpha()
        self.i_Boats1 = pygame.image.load("img\\game-boat-sheep.png").convert_alpha()
        self.i_Boatc1 = pygame.image.load("img\\game-boat-cabbage.png").convert_alpha()
        self.i_menuToggle = pygame.image.load("img\\menu-toggle.png").convert_alpha()
        self.i_sndOn = pygame.image.load("img\\menu-sound-on.png").convert_alpha()
        self.i_sndOff = pygame.image.load("img\\menu-sound-off.png").convert_alpha()
        self.i_snowflake = pygame.image.load("img\\snowflake.png").convert_alpha()
        self.i_snowflake = pygame.transform.scale( self.i_snowflake, ( 20, 20 ) )
        
        # Third theme image loads
        self.background3 = pygame.image.load("img\\background3.png").convert_alpha()
        self.i_water3 = pygame.image.load("img\\river3.png").convert_alpha()
        self.i_CloudOne3 = pygame.image.load("img\\cloud-bat-one.png").convert_alpha()
        self.i_CloudOneAnim3 = pygame.image.load("img\\cloud-bat-two.png").convert_alpha()
        self.i_CloudTwo3 = pygame.image.load("img\\cloud-ghost-one.png").convert_alpha()
        self.i_CloudTwoAnim3 = pygame.image.load("img\\cloud-ghost-two.png").convert_alpha()
        self.i_BankL3 = pygame.image.load("img\\bank_l3.png").convert_alpha()
        self.i_Bankr3 = pygame.image.load("img\\bank_r3.png").convert_alpha()
        self.i_Wolf3 = pygame.image.load("img\\game-werewolf.png").convert_alpha()
        self.i_WolfE1_3 = pygame.image.load("img\\game-werewolf-eat-one.png").convert_alpha()
        self.i_WolfE2_3 = pygame.image.load("img\\game-werewolf-eat-two.png").convert_alpha()
        self.i_Sheep3 = pygame.image.load("img\\game-sheep.png").convert_alpha()
        self.i_SheepE1_3 = pygame.image.load("img\\game-sheep-eat-one.png").convert_alpha()
        self.i_SheepE2_3 = pygame.image.load("img\\game-sheep-eat-two.png").convert_alpha()
        self.i_Cabbage3 = pygame.image.load("img\\game-pumpkin.png").convert_alpha()
        self.i_Wave3 = pygame.image.load("img\\game-wave-halloween.png").convert_alpha()
        self.i_Boatb3 = pygame.image.load("img\\game-boat-halloween.png").convert_alpha()
        self.i_Boatw3 = pygame.image.load("img\\game-boat-werewolf.png").convert_alpha()
        self.i_Boats3 = pygame.image.load("img\\game-boat-sheep-halloween.png").convert_alpha()
        self.i_Boatc3 = pygame.image.load("img\\game-boat-pumpkin.png").convert_alpha()

        # DJH - sound loads
        self.sndWin = pygame.mixer.Sound( "snd\\win.wav" )
        self.sndLose = pygame.mixer.Sound( "snd\\lose.wav" )
        self.sndCabbage = pygame.mixer.Sound( "snd\\cabbage.wav" )
        self.sndSheep = pygame.mixer.Sound( "snd\\sheep.wav" )
        self.sndWolf = pygame.mixer.Sound( "snd\\wolf.wav" )
        self.sndWavesM = pygame.mixer.Sound( "snd\\waves.wav" )
        self.sndWavesG = pygame.mixer.Sound( "snd\\waves_crisp.wav" )
        self.sndWavesM.set_volume( self.SND_BACKGROUND_VOL )
        self.sndWavesG.set_volume( self.SND_BACKGROUND_VOL )

        # set theme
        self.change_Theme()

    #Variable Declaration
    def reset_Var(self):
        # Variables to be reset on the start of a new game.
        self.running = True
        self.gameover = False
        self.counter = 0
        self.clicks = 0
        self.highscore_timer = 0
        self.gamefail = False
        self.screenVis = "menu"
        self.LEFT = 1
        self.item = False
        self.wolfPos = ( self.WOLF_XR, self.WOLF_Y )
        self.sheepPos = ( self.SHEEP_XR, self.SHEEP_Y )
        self.cabbagePos = ( self.CABBAGE_XR, self.CABBAGE_Y )
        self.boatPos = ( self.BOAT_R, self.BOAT_Y )
        self.cloudPosOne = (70, 30)
        self.cloudPosTwo = (450, 110)
        self.cLeft = 0
        self.boatObj = ""
        self.boatItem = False
        self.change_Boat()
        self.scroll_water = 0
        self.scroll_wave = self.wave_size[0]
        self.scroll_water_direction = 1
        self.scroll_wave_direction = -1

        # Check if highscore file is present. If not, make one.
        try:
            fHIGHSCORE = open("highscore.txt", "r")
        except Exception, e:
            fHIGHSCORE = open("highscore.txt", "w")
            fHIGHSCORE.write("1000 1000 1000")
            fHIGHSCORE.close()
            fHIGHSCORE = open("highscore.txt", "r")

        # Split text file data to list.
        self.fSCORES = fHIGHSCORE.read().split(" ")
        fHIGHSCORE.close()

    # Saving highscore to text file.
    def save_Highscore(self, name, htime, clicks):
        fHIGHSCORES = open("highscore.txt", "w")
        htime = int(htime)
        fHIGHSCORES.write("%s %s %s" % (name, htime, self.clicks))
        fHIGHSCORES.close()
        self.reset_Var()
        self.blit_Menu()

    # Blit Highscore menu to self.screen.
    def blit_Highscore(self):

        # Draw self.background
        self.blit_Background()

        #Animated waves on menu
        self.blit_Water()
        self.blit_Waves()

        #Draw transparent rect
        self.trans_Rect(250,240,30)
        
        #Drawing text and buttons
        t_Highscore = self.screen.blit(self.i_menuH, (self.DISPLAY_WIDTH/2 - 101, 50))
        self.b_Back = self.screen.blit(self.i_Back, (self.DISPLAY_WIDTH/2 - 52.5, 210))

        #Check if high score has been set.
        if self.fSCORES[0] == "1000" and self.fSCORES[1] == "1000":
            nameVar, clickVar, timeVar = "Name: None Set", "Clicks: None Set", "Timer: None Set"
        else:
            nameVar = "Name: %s" % self.fSCORES[0]
            clickVar = "Clicks: %s" % self.fSCORES[2]
            timeVar = "Timer: %s" % self.fSCORES[1]

        #Draw highscore text to self.screen.
        t_Highscore = [nameVar, clickVar, timeVar]
        for i in range(len(t_Highscore)):
            htext = self.largefont.render(t_Highscore[i], True, (0,0,0))
            rHighscore = self.screen.blit(htext, (self.DISPLAY_WIDTH/2-80, 100 + i*30))
            
        pygame.display.flip()
        
    # Changing the display self.background.
    def blit_Background(self):

        # Calculate cloud position.
        self.calc_Clouds()

        # Draw self.background image.
        self.screen.blit(self.background, ( 0, 0 ) )

        # Calculate which image should be used to animate the first cloud
        if self.counter % self.cloud_anim_change == 0:
            if self.cloud_anim == 0:
                self.cloud_anim = 1
                self.i_CloudOne = self.i_CloudOneAnimA
            else:
                self.cloud_anim = 0
                self.i_CloudOne = self.i_CloudOneAnimB

        # Draw clouds on self.background.
        self.c_CloudOne = self.screen.blit( self.i_CloudOne, self.cloudPosOne )
        self.c_CloudTwo = self.screen.blit( self.i_CloudTwo, self.cloudPosTwo )


    #Loading Menu Images
    def blit_Menu(self):

        # Draw the self.background
        self.blit_Background()

        # Draw transparent rect.
        self.trans_Rect(250, 260, 20)

        # Draw transparent rect off centre.
        self.screen_t = pygame.Surface((45, 39), pygame.SRCALPHA)
        self.screen_t.fill((255,255,255,128))
        self.screen.blit(self.screen_t, (10, 10))
        self.screen.blit(self.screen_t, (10, 60))

        #Loading menu items
        self.b_StartGame = self.screen.blit(self.i_menuS, (self.DISPLAY_WIDTH/2 - 101, 40))
        self.b_Rules = self.screen.blit(self.i_menuR, (self.DISPLAY_WIDTH/2 - 101, 100))
        self.b_Highscore = self.screen.blit(self.i_menuH, (self.DISPLAY_WIDTH/2 - 101, 160))
        self.b_Credits = self.screen.blit(self.i_menuC, (self.DISPLAY_WIDTH/2 - 101, 220))
        self.b_Toggle = self.screen.blit(self.i_menuToggle, (10, 10))

        # Toggle mute button.
        if not self.sndMute:
            self.b_Mute = self.screen.blit(self.i_sndOn, (10, 60))
        else:
            self.b_Mute = self.screen.blit(self.i_sndOff, (10, 60))

        # Draw water animation.
        self.blit_Water()
        self.blit_Waves()

        # Refresh the display
        pygame.display.flip()

    # On self.gameover:
    def blit_GameOver(self):

        #Draw a transparent rect if the theme is dark.
        if self.themeSun == False:
            self.trans_Rect(450, 200, 45)

        #Drawing game over images.
        if self.gameover == True and self.gamefail == True:
            t_gameO = self.screen.blit(self.i_gameOl, (self.DISPLAY_WIDTH/2 - 215, 75))
            self.b_gameB = self.screen.blit(self.i_gameBl, (self.DISPLAY_WIDTH/2 - 121, 190))
            pygame.display.flip()
        elif self.gameover == True and self.gamefail == False:
            t_gameO = self.screen.blit(self.i_gameOw, (self.DISPLAY_WIDTH/2 - 162, 55))
            self.b_gameB = self.screen.blit(self.i_gameBw, (self.DISPLAY_WIDTH/2 - 121, 190))


            # Check if new highscore to be set.
            if int(self.clicks) == int(self.fSCORES[2]):

                if int(self.highscore_timer) < int(self.fSCORES[1]):
                    nHigh = self.largefont.render("NEW HIGHSCORE!", True, (0,0,0))
                    rHigh = self.screen.blit(nHigh, (self.DISPLAY_WIDTH/2-80, 120))                
                    usrName = pginput.prompt(self.screen, "Name", 100, 20, 200, self.DISPLAY_WIDTH/2 - 100, 150)
                    self.save_Highscore(usrName, self.highscore_timer, self.clicks)

            elif int(self.clicks) < int(self.fSCORES[2]):
                nHigh = self.largefont.render("NEW HIGHSCORE!", True, (0,0,0))
                rHigh = self.screen.blit(nHigh, (self.DISPLAY_WIDTH/2-80, 120))                
                usrName = pginput.prompt(self.screen, "Name", 100, 20, 200, self.DISPLAY_WIDTH/2 - 100, 150)
                self.save_Highscore(usrName, self.highscore_timer, self.clicks)
            
            # Refresh the display
            pygame.display.flip()

    # Calculate and blit snowflakes
    def blit_Snowflakes(self):

        # Snowflakes
        for f in range( len( self.m_snowflakes ) ):
            flake_x = self.m_snowflakes[ f ][0] 
            flake_y = self.m_snowflakes[ f ][1] + 1
            if flake_y > self.DISPLAY_HEIGHT:
                flake_x = random.random() * self.DISPLAY_WIDTH
                flake_y = -10
            self.m_snowflakes[ f ] = ( flake_x, flake_y )
        for flake in self.m_snowflakes:
            self.screen.blit( self.i_snowflake, ( flake[0], flake[1] ) )

    # Calculate and blit water
    def blit_Water(self):

        self.scroll_water += self.scroll_water_direction * ( math.sin( math.radians( self.counter ) ) * 2 )

        if self.scroll_water > self.water_size[0]:
            self.scroll_water_direction = -1
        elif self.scroll_water < 0:
            self.scroll_water_direction = 1
        
        self.s_waterSurface.fill( 0x000000 )

        # Blit snowflakes first
        if self.themeNight:
            self.blit_Snowflakes()

        # Blit water
        self.s_waterSurface.blit( self.i_water, ( self.scroll_water, 0 ) )
        self.s_waterSurface.blit( self.i_water, ( self.scroll_water - self.water_size[0], 0 ) )
          
        self.screen.blit( self.s_waterSurface, ( 171, 293 ) )

    # Draw a centred transparent rect.
    def trans_Rect(self, bwidth, bheight, top):
        self.screen_t = pygame.Surface((bwidth, bheight), pygame.SRCALPHA)
        self.screen_t.fill((255,255,255,128))
        self.screen.blit(self.screen_t, (( self.DISPLAY_WIDTH/2) - (bwidth/2), top))    

    # Draw waves to self.screen.
    def blit_Waves(self):

        self.scroll_wave += self.scroll_wave_direction  * ( math.sin( math.radians( self.counter ) ) * 2 )

        if self.scroll_wave > self.water_size[0]:
            self.scroll_wave_direction = -1
        elif self.scroll_wave < 0:
            self.scroll_wave_direction = 1

        # Blit waves
        self.s_waveSurface.fill( 0x000000 )
        self.s_waveSurface.blit( self.i_Wave, ( self.scroll_wave, 0 ) )
        self.s_waveSurface.blit( self.i_Wave, ( self.scroll_wave - self.wave_size[0], 0 ) )
        self.screen.blit( self.s_waveSurface, ( 171, 323 ) )

        # Blit banks
        self.screen.blit( self.i_BankL, ( 0, 290 ) )
        self.screen.blit( self.i_Bankr, ( 433, 290 ) )

    # Calculate cloud position.
    def calc_Clouds(self):

        # Placing clouds back on the self.screen when they exit.
        if self.cloudPosOne[0] > 770:
            self.cloudPosOne = (-130, self.cloudPosOne[1])
        if self.cloudPosTwo[0] > 770:
            self.cloudPosTwo = (-130, self.cloudPosTwo[1])
        else:
            self.cloudPosOne, self.cloudPosTwo = (self.cloudPosOne[0] + 1, self.cloudPosOne[1]), (self.cloudPosTwo[0] + 0.5, self.cloudPosTwo[1])

    # Blit the game images
    def blit_Game( self, wImg = 0, sImg = 0 ):

        # Re-draw self.background
        self.blit_Background()

        # Animate water
        self.blit_Water()
        
        # Game images and buttons
        self.g_Boat = self.screen.blit(self.i_Boat, self.boatPos)
        self.blit_Waves()

        # Check to see if item is in boat before drawing it.
        if self.boatObj != "cabbage":
            self.g_Cabbage = self.screen.blit( self.i_Cabbage, self.cabbagePos )
        if self.boatObj != "sheep":
            if sImg == 0:
                self.g_Sheep = self.screen.blit( self.i_Sheep, self.sheepPos )
            elif sImg == 1:
                self.g_Sheep = self.screen.blit( self.i_SheepE1, self.sheepPos )
            elif sImg == 2:
                self.g_Sheep = self.screen.blit( self.i_SheepE2, self.sheepPos )
        if self.boatObj != "wolf":
            if wImg == 0:
                self.g_Wolf = self.screen.blit( self.i_Wolf, self.wolfPos )
            elif wImg == 1:
                self.g_Wolf = self.screen.blit( self.i_WolfE1, self.wolfPos )
            elif wImg == 2:
                self.g_Wolf = self.screen.blit( self.i_WolfE2, self.wolfPos )

        # Draw transparent rect.
        self.trans_Rect(220, 30, 10)

        # Display self.clicks self.counter.
        self.clicksStr = "Clicks: %s" % self.clicks
        self.t_clicks = self.largefont.render(self.clicksStr, True, (0,0,0))
        self.rClicks = self.screen.blit(self.t_clicks, (self.DISPLAY_WIDTH/2 - 80, 10))

        # Display timer.
        self.timerStr = "Timer: %d" % int(self.highscore_timer)
        self.t_timer = self.largefont.render(self.timerStr, True, (0,0,0))
        self.rTimer = self.screen.blit(self.t_timer, (self.DISPLAY_WIDTH/2 + 20, 10))   

        # Draw transparent rect off centre.
        self.screen_t = pygame.Surface((45, 39), pygame.SRCALPHA)
        self.screen_t.fill((255,255,255,128))
        self.screen.blit(self.screen_t, (10, 10))
        self.screen.blit(self.screen_t, (10, 60))

        # Draw toggle button.
        self.b_Toggle = self.screen.blit(self.i_menuToggle, (10, 10))

        # Toggle mute button.
        if not self.sndMute:
            self.b_Mute = self.screen.blit(self.i_sndOn, (10, 60))
        else:
            self.b_Mute = self.screen.blit(self.i_sndOff, (10, 60))

        # Refresh the display
        pygame.display.flip()


    #Boat left/right animation
    def move_Boat(self, bm ):

        # If boat is moving from right to left
        if bm == -1:
            if self.boatPos[0] > self.BOAT_L:
                self.boatPos = ( self.boatPos[0] - 5, self.boatPos[1] )
            else:
                bm = 0

        # If boat is moving from left to right
        if bm == 1:
            if self.boatPos[0] < self.BOAT_R:
                self.boatPos = ( self.boatPos[0] + 5, self.boatPos[1] )
            else:
                bm = 0

        return bm


    #Change boat image depending on object stored
    def change_Boat(self):
        # Empty boat.
        if self.boatObj == "":
            self.i_Boat = self.i_Boatb
            self.boatItem = False

        # Play sound and set image depending on item in boat.   
        if self.boatObj == "wolf":
                self.i_Boat = self.i_Boatw
                if self.boatItem == False:
                    if not self.sndMute:
                        self.sndWolf.play()
                    self.boatItem = True
                    
        if self.boatObj == "sheep":
                self.i_Boat = self.i_Boats
                if self.boatItem == False:
                    if not self.sndMute:
                        self.sndSheep.play()
                    self.boatItem = True
                    
        if self.boatObj == "cabbage":
                self.i_Boat = self.i_Boatc
                if self.boatItem == False:
                    if not self.sndMute:
                        self.sndCabbage.play()
                    self.boatItem = True

    # Check to see if the game should end
    def check_Status(self):

        # Animation self.counters.
        anim_repeats = 9
        anim_period = 180
        anim_change = ( anim_period / anim_repeats ) / 2.0

        # Game ending conditions
        if self.gameover == False:
            if     self.boatPos[0] == self.BOAT_L and self.wolfPos[0] == self.WOLF_XR and self.sheepPos[0] == self.SHEEP_XR \
                or self.boatPos[0] == self.BOAT_R and self.wolfPos[0] == self.WOLF_XL and self.sheepPos[0] == self.SHEEP_XL:
                if not self.sndMute:
                    pygame.mixer.fadeout(500)
                    self.sndWolf.play()
                    self.sndLose.play()
                c = 2
                for i in range( anim_period ):
                    if i % anim_change == 0:
                        if c == 1:
                            c = 2
                        else:
                            c = 1
                    self.blit_Game( c, 0 )
                    self.counter += 1
                    self.clock.tick( 60 )
                self.gamefail = True
                self.gameover = True
                self.blit_GameOver()
                
            elif   self.boatPos[0] == self.BOAT_L and self.cabbagePos[0] == self.CABBAGE_XR and self.sheepPos[0] == self.SHEEP_XR \
                or self.boatPos[0] == self.BOAT_R and self.cabbagePos[0] == self.CABBAGE_XL and self.sheepPos[0] == self.SHEEP_XL:
                if not self.sndMute:
                    pygame.mixer.fadeout(500)
                    self.sndSheep.play()
                    self.sndLose.play()
                self.sheepPos = ( self.sheepPos[0], self.sheepPos[1] + 10 ) #map(sum,zip(self.sheepPos,(0,10)))
                c = 2
                for i in range( anim_period ):
                    if i % anim_change == 0:
                        if c == 1:
                            c = 2
                        else:
                            c = 1
                    self.blit_Game( 0, c )
                    self.counter += 1
                    self.clock.tick( 60 )
                self.gamefail = True
                self.gameover = True
                self.blit_GameOver()
                
            # All objects on left together \
            elif self.wolfPos[0] == self.WOLF_XL and self.sheepPos[0] == self.SHEEP_XL and self.cabbagePos[0] == self.CABBAGE_XL:
                # then WIN!!
                if not self.sndMute:
                    self.sndWin.play()
                self.gamefail = False
                self.gameover = True
                self.blit_GameOver()

            if self.gameover == True:
                self.sndWavesG.fadeout(500)
                self.sndBackgroundG = False
                if not self.sndMute:
                    self.sndWavesM.play( -1 )
                    self.sndBackgroundM = True

    # Loading Credits self.screen
    def blit_Credits(self):
        
        # Re-draw self.background.
        self.blit_Background()

        # Draw water.
        self.blit_Water()
        self.blit_Waves()

        # Animate credits.
        self.scroll_Credits()

        # Draw transparent rect.
        self.screen_t = pygame.Surface((105, 39), pygame.SRCALPHA)
        self.screen_t.fill((255,255,255,128))
        self.screen.blit(self.screen_t, (self.DISPLAY_WIDTH/2 - 250, 230))
        
        # Draw back button to self.screen.
        self.b_Back = self.screen.blit(self.i_Back, (self.DISPLAY_WIDTH/2 - 250, 230))
        
        # Refresh the display
        pygame.display.flip()

    # Animating credits.
    def scroll_Credits(self):

        # Increase self.counter
        self.j += 1
        self.tHEIGHT = 2*20 - self.j
        
        # Credit text
        self.t_cred = ["David Humphreys", "Benjamin Hughes", "Natalie Machin",
                  "Edward Haswell", "Sebastian Gaetani", "Adeeb Rashid",
                  "Adam Bullock", "William Evans"]
        
        # Move text down if it exits self.screen.
        if self.tHEIGHT < -800:
            self.j = -500

        # Draw text to self.screen.
        for i in range(len(self.t_cred)):
            self.shadcreds = self.vlargefont.render(self.t_cred[i], True, (255,255,255))
            self.creds = self.vlargefont.render(self.t_cred[i], True, (0,0,0))
            self.rShadCreds = self.screen.blit(self.shadcreds, (self.DISPLAY_WIDTH/2-50-(len(self.t_cred[i])*5)+1.5, i*100 - self.j+1.5))
            self.rCreds = self.screen.blit(self.creds, (self.DISPLAY_WIDTH/2-50-(len(self.t_cred[i])*5), i*100 - self.j))
        
    # Loading Rules self.screen
    def blit_Rules(self):
        
        # Re-draw self.background
        self.blit_Background()

        # Draw water.
        self.blit_Water()
        self.blit_Waves()

        # Draw transparent rect.
        self.trans_Rect(260, 260, 20)

        # Drawing text and buttons.
        self.t_Rules = self.screen.blit(self.i_menuR, (self.DISPLAY_WIDTH/2 - 101, 30))
        self.b_Back = self.screen.blit(self.i_Back, (self.DISPLAY_WIDTH/2 - 52.5, 230))

        # Rules text.
        self.t_rules = ["Move the wolf, the sheep, and the",
                   "cabbage to the opposite side by", "moving only one item at a time.",
                   "", "Be careful! If the farmer is not", "around, the wolf will eat the sheep",
                   "and the sheep will eat the cabbage."]

        #Draw self.rules to self.screen.
        for i in range(len(self.t_rules)):
            self.rules = self.medfont.render(self.t_rules[i], True, (0,0,0))
            self.rRules = self.screen.blit(self.rules, (215, 80 + i*20))
            
        # Refresh the display
        pygame.display.flip()

    def change_Theme(self):

        # Theme toggle.
        if self.themeSun == True:
            self.themeSun = False
            self.themeNight = True
        elif self.themeNight == True:
            self.themeNight = False
            self.themeHallow = True
        elif self.themeHallow == True:
            self.themeHallow = False
            self.themeSun = True

        # Set images depending on theme.
        if self.themeSun:
            self.background = self.background1
            self.i_CloudOneAnimA = self.i_CloudOne1
            self.i_CloudOneAnimB = self.i_CloudOne1
            self.i_CloudTwo = self.i_CloudTwo1
            self.i_water = self.i_water1
            self.i_BankL = self.i_BankL1
            self.i_Bankr = self.i_Bankr1
            self.i_Boatb = self.i_Boatb1
            self.i_Boatw = self.i_Boatw1
            self.i_Boats = self.i_Boats1
            self.i_Boatc = self.i_Boatc1
            self.i_Wolf = self.i_Wolf1
            self.i_WolfE1 = self.i_WolfE1_1
            self.i_WolfE2 = self.i_WolfE2_1
            self.i_Sheep = self.i_Sheep1
            self.i_SheepE1 = self.i_SheepE1_1
            self.i_SheepE2 = self.i_SheepE2_1
            self.i_Cabbage = self.i_Cabbage1
            self.i_Wave = self.i_Wave1
        if self.themeNight:
            self.background = self.background2
            self.i_CloudOneAnimA = self.i_CloudOne2
            self.i_CloudOneAnimB = self.i_CloudOne2
            self.i_CloudTwo = self.i_CloudTwo2
            self.i_water = self.i_water2
            self.i_BankL = self.i_BankL2
            self.i_Bankr = self.i_Bankr2
            self.i_Boatb = self.i_Boatb1 #
            self.i_Boatw = self.i_Boatw1 #
            self.i_Boats = self.i_Boats1 #
            self.i_Boatc = self.i_Boatc1 #
            self.i_Wolf = self.i_Wolf1 #
            self.i_WolfE1 = self.i_WolfE1_1 #
            self.i_WolfE2 = self.i_WolfE2_1 #
            self.i_Sheep = self.i_Sheep1 #
            self.i_SheepE1 = self.i_SheepE1_1 #
            self.i_SheepE2 = self.i_SheepE2_1 #
            self.i_Cabbage = self.i_Cabbage1 #
            self.i_Wave = self.i_Wave1 #
        if self.themeHallow:
            self.background = self.background3
            self.i_CloudOneAnimA = self.i_CloudOne3
            self.i_CloudOneAnimB = self.i_CloudOneAnim3
            self.i_CloudTwo = self.i_CloudTwo3
            self.i_water = self.i_water3
            self.i_BankL = self.i_BankL3
            self.i_Bankr = self.i_Bankr3
            self.i_Boatb = self.i_Boatb3
            self.i_Boatw = self.i_Boatw3
            self.i_Boats = self.i_Boats3
            self.i_Boatc = self.i_Boatc3
            self.i_Wolf = self.i_Wolf3
            self.i_WolfE1 = self.i_WolfE1_3
            self.i_WolfE2 = self.i_WolfE2_3
            self.i_Sheep = self.i_Sheep3
            self.i_SheepE1 = self.i_SheepE1_3
            self.i_SheepE2 = self.i_SheepE2_3
            self.i_Cabbage = self.i_Cabbage3
            self.i_Wave = self.i_Wave3

        self.i_CloudOne = self.i_CloudOneAnimA
        self.change_Boat()


    # MAIN ENTRY POINT
    def start(self):
        # Setting up display
        pygame.display.init()
        self.screen = pygame.display.set_mode( ( self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT ), pygame.HWSURFACE | pygame.DOUBLEBUF, 32 )

        # Initialise mixer
        pygame.mixer.init()

        #Initiate font module
        pygame.font.init()
        self.medfont = pygame.font.SysFont("Arial", 17)
        self.largefont = pygame.font.SysFont("Arial", 22)
        self.vlargefont = pygame.font.SysFont("Arial", 36)

        #Change window options
        pygame.display.set_caption('Group 3 Game')

        # Some basic setup
        self.setup()
        self.reset_Var()

        # Setup pygame timer and variables for main loop
        self.clock = pygame.time.Clock()
        self.j = -500
        self.boat_move = 0

        # Draw the menu
        self.blit_Menu()

        #Begin main Loop
        while self.running:

            #Counter for animation.
            self.counter += 1

            # Increase game timer.
            if self.gameover == False and self.screenVis == "game":
                self.highscore_timer += 0.015
                
            # Loop through events
            for event in pygame.event.get():

                # If left mouse button pressed down
                if event.type == MOUSEBUTTONDOWN and event.button == self.LEFT and self.gameover == False:

                    # Check if menu is open
                    if self.screenVis=="menu":
                        # Start Game Menu Button
                        if self.b_StartGame.collidepoint(pygame.mouse.get_pos()):
                            self.screenVis = "game"
                            self.sndWavesM.fadeout(500)
                            if not self.sndMute:
                                self.sndWavesG.play( -1 )
                                self.sndBackgroundG = True
                            self.blit_Game()
                            
                        # Rules Menu Button
                        if self.b_Rules.collidepoint(pygame.mouse.get_pos()):
                            self.screenVis = "subMenu"
                            
                        # Highscore Menu Button
                        if self.b_Highscore.collidepoint(pygame.mouse.get_pos()):
                            self.screenVis = "subMenuH"

                        # Credits Menu Button
                        if self.b_Credits.collidepoint(pygame.mouse.get_pos()):
                            self.screenVis = "subMenuC"
                     
                        # Toggle Day/Night/Halloween
                        if self.b_Toggle.collidepoint(pygame.mouse.get_pos()):
                            self.change_Theme()

                        # Toggle mute.
                        if self.b_Mute.collidepoint(pygame.mouse.get_pos()):
                            if not self.sndMute:
                                pygame.mixer.fadeout(500)
                                self.sndMute = True
                            else:
                                self.sndMute = False
                                self.sndWavesM.play( -1 )
                            
                    #Check if a sub menu is open
                    elif self.screenVis == "subMenu" or self.screenVis == "subMenuH" or self.screenVis == "subMenuC":

                        #Back Button
                        if self.b_Back.collidepoint(pygame.mouse.get_pos()):
                            self.screenVis = "menu"

                    #Check if game is playing        
                    if self.screenVis == "game":
                        
                        if self.g_Boat.collidepoint(pygame.mouse.get_pos()) or self.g_Wolf.collidepoint(pygame.mouse.get_pos()) or self.g_Sheep.collidepoint(pygame.mouse.get_pos()) or self.g_Cabbage.collidepoint(pygame.mouse.get_pos()):
                            self.clicks += 1
                        
                        #If empty boat is clicked.
                        if self.g_Boat.collidepoint(pygame.mouse.get_pos()) and self.boatObj == "":
                            # If boat is on left, set to move right
                            if self.boatPos[0] == self.BOAT_L:
                                self.boat_move = 1
                            # If boat is on right, set to move left
                            if self.boatPos[0] == self.BOAT_R:
                                self.boat_move = -1

                        #If boat containing wolf is clicked on left side.
                        elif self.g_Boat.collidepoint(pygame.mouse.get_pos()) and self.boatObj == "wolf" and self.boatPos[0] == self.BOAT_L:
                            if self.wolfPos == ( self.OBJVANISH_X, self.OBJVANISH_Y ):
                                self.wolfPos = ( self.WOLF_XL, self.WOLF_Y )
                            self.boatObj = ""
                            item = False
                            self.change_Boat()
                        #If boat containing wolf is clicked on right side.
                        elif self.g_Boat.collidepoint(pygame.mouse.get_pos()) and self.boatObj == "wolf" and self.boatPos[0] == self.BOAT_R:
                            if self.wolfPos == ( self.OBJVANISH_X, self.OBJVANISH_Y ):
                                self.wolfPos = ( self.WOLF_XR, self.WOLF_Y )
                            self.boatObj = ""
                            item = False
                            self.change_Boat()

                        #If boat containing sheep is clicked on left side.
                        elif self.g_Boat.collidepoint(pygame.mouse.get_pos()) and self.boatObj == "sheep" and self.boatPos[0] == self.BOAT_L:
                            if self.sheepPos == ( self.OBJVANISH_X, self.OBJVANISH_Y ):
                                self.sheepPos = ( self.SHEEP_XL, self.SHEEP_Y )
                            self.boatObj = ""
                            item = False
                            self.change_Boat()
                        #If boat containing sheep is clicked on right side.
                        elif self.g_Boat.collidepoint(pygame.mouse.get_pos()) and self.boatObj == "sheep" and self.boatPos[0] == self.BOAT_R:
                            if self.sheepPos == ( self.OBJVANISH_X, self.OBJVANISH_Y ):
                                self.sheepPos = ( self.SHEEP_XR, self.SHEEP_Y )
                            self.boatObj = ""
                            item = False
                            self.change_Boat()

                        #If boat containing cabbage is clicked on left side.
                        elif self.g_Boat.collidepoint(pygame.mouse.get_pos()) and self.boatObj == "cabbage" and self.boatPos[0] == self.BOAT_L:
                            if self.cabbagePos == ( self.OBJVANISH_X, self.OBJVANISH_Y ):
                                self.cabbagePos = ( self.CABBAGE_XL, self.CABBAGE_Y )
                            self.boatObj = ""
                            item = False
                            self.change_Boat()
                        #If boat containing cabbage is clicked on right side.
                        elif self.g_Boat.collidepoint(pygame.mouse.get_pos()) and self.boatObj == "cabbage" and self.boatPos[0] == self.BOAT_R:
                            if self.cabbagePos == ( self.OBJVANISH_X, self.OBJVANISH_Y ):
                                self.cabbagePos = ( self.CABBAGE_XR, self.CABBAGE_Y )
                            self.boatObj = ""
                            item = False
                            self.change_Boat()

                        #Loading wolf on to boat on right side.
                        if self.g_Wolf.collidepoint(pygame.mouse.get_pos()) and self.boatObj != "wolf" and self.boatPos[0] == self.BOAT_R and self.wolfPos[0] == self.WOLF_XR:
                            self.boatObj = "wolf"
                            self.wolfPos = ( self.OBJVANISH_X, self.OBJVANISH_Y )
                            self.change_Boat()
                            self.boat_move = -1
                        #Loading wolf on to boat on left side.
                        elif self.g_Wolf.collidepoint(pygame.mouse.get_pos()) and self.boatObj != "wolf" and self.boatPos[0] == self.BOAT_L and self.wolfPos[0] == self.WOLF_XL:
                            self.boatObj = "wolf"
                            self.wolfPos = ( self.OBJVANISH_X, self.OBJVANISH_Y )
                            self.change_Boat()
                            self.boat_move = 1

                        #Loading sheep on to boat on right side.
                        elif self.g_Sheep.collidepoint(pygame.mouse.get_pos()) and self.boatObj != "sheep" and self.boatPos[0] == self.BOAT_R and self.sheepPos[0] == self.SHEEP_XR:
                            self.boatObj = "sheep"
                            self.sheepPos = ( self.OBJVANISH_X, self.OBJVANISH_Y )
                            self.change_Boat()
                            self.boat_move = -1
                        #Loading sheep on to boat on left side.
                        elif self.g_Sheep.collidepoint(pygame.mouse.get_pos()) and self.boatObj != "sheep" and self.boatPos[0] == self.BOAT_L and self.sheepPos[0] == self.SHEEP_XL:
                            self.boatObj = "sheep"
                            self.sheepPos = ( self.OBJVANISH_X, self.OBJVANISH_Y )
                            self.change_Boat()
                            self.boat_move = 1

                        #Loading cabbage on to boat on right side.
                        elif self.g_Cabbage.collidepoint(pygame.mouse.get_pos()) and self.boatObj != "cabbage" and self.boatPos[0] == self.BOAT_R and self.cabbagePos[0] == self.CABBAGE_XR:
                            self.boatObj = "cabbage"
                            self.cabbagePos = ( self.OBJVANISH_X, self.OBJVANISH_Y )
                            self.change_Boat()
                            self.boat_move = -1
                        #Loading cabbage on to boat on left side.
                        elif self.g_Cabbage.collidepoint(pygame.mouse.get_pos()) and self.boatObj != "cabbage" and self.boatPos[0] == self.BOAT_L and self.cabbagePos[0] == self.CABBAGE_XL:
                            self.boatObj = "cabbage"
                            self.cabbagePos = ( self.OBJVANISH_X, self.OBJVANISH_Y )
                            self.change_Boat()
                            self.boat_move = 1
                            
                        #Toggle Day/Night
                        if self.b_Toggle.collidepoint(pygame.mouse.get_pos()):
                            self.change_Theme()


                        #Toggle Mute on/off
                        if self.b_Mute.collidepoint(pygame.mouse.get_pos()):
                            if not self.sndMute:
                                pygame.mixer.fadeout(500)
                                self.sndMute = True
                            else:
                                self.sndMute = False
                                self.sndWavesG.play( -1 )

                            
                #If left mouse button pressed down when game over self.screen is visible
                if event.type == MOUSEBUTTONDOWN and event.button == self.LEFT and self.gameover == True:

                    #Back to Menu Button
                    if self.b_gameB.collidepoint(pygame.mouse.get_pos()):
                        self.reset_Var()

            #Exit if closed otherwise
            if event.type == pygame.QUIT:
                self.running = False
                pygame.mixer.stop()
                pygame.quit() #IDLE FRIENDLY EXIT

            # If the game is self.running...
            if self.screenVis == "game":
                # Update the boat
                self.boat_move = self.move_Boat( self.boat_move )
                # BLIT!
                if self.gameover == False:
                    self.blit_Game()
                # Check the game status
                self.check_Status()
                # Play the in-game sound
                if not self.sndMute and not self.sndBackgroundG:
                    self.sndWavesG.play( -1 )
                    self.sndBackgroundG = True
            # Else if it isn't, play the non in-game sound
            else:
                if not self.sndMute and not self.sndBackgroundM:
                    self.sndWavesM.play( -1 )
                    self.sndBackgroundM = True

            # Draw menu depending on selection.
            if self.screenVis == "menu":
                self.blit_Menu()
            if self.screenVis == "subMenu":
                self.blit_Rules()
            if self.screenVis == "subMenuH":
                self.blit_Highscore()
            if self.screenVis == "subMenuC":
                self.blit_Credits()

            # Force 60 FPS
            self.clock.tick( 60 )

if __name__ == "__main__":
    GameClass()
