#!/usr/bin/env

import pygame, pygame.font
import pygame.event, pygame.draw
import string as s
from pygame.locals import *

#Creating and displaying question
def prompt(surface, question, wdt, hgt, lng, pwdt, phgt):
  inp = []
  pygame.font.init()
  draw_prompt_rect(surface, question + ": " + s.join(inp, ""), wdt, hgt,lng, pwdt, phgt)
  while 1:
    evt = pygame.event.poll()
    if evt.type == KEYDOWN: pressed = evt.key
    else: pressed = None
    if pressed == K_BACKSPACE: inp = inp[0:-1]
    if pressed == K_RETURN: break
    if len(inp) < 12 and pressed <= 127 and pressed != None: inp.append(chr(pressed))
    draw_prompt_rect(surface, question + ": " + s.join(inp, ""), wdt, hgt, lng, pwdt, phgt)
  return s.join(inp, "")

#Drawing box for question
def draw_prompt_rect(surface, question, wdt, hgt, lng, pwdt, phgt):
  fnt = pygame.font.SysFont("Arial",26)
  if len(question) > 0: surface.blit(fnt.render(question, 1, (0, 0, 0)), (pwdt, phgt))
  pygame.display.update()
