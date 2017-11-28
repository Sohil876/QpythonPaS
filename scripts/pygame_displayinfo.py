#!/usr/bin/env python
#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import pygame
from pygame.locals import *

pygame.init()
pygame.display.init()

print "Display info: "
DISPLAYINFO = pygame.display.Info()
print DISPLAYINFO
WINDOWWIDTH = DISPLAYINFO.current_w
WINDOWHEIGHT = DISPLAYINFO.current_h
SIZE = (WINDOWWIDTH, WINDOWHEIGHT)
pygame.display.set_mode(SIZE, 0)

print "Display driver: "
print pygame.display.get_driver()

print "Surface info: "
print pygame.display.get_surface()

print "Bits: "
print pygame.display.get_surface().get_bitsize()

print "Windowing system info: "
print pygame.display.get_wm_info()

print "List of available fullscreen modes: "
print pygame.display.list_modes()

pygame.display.quit()
pygame.quit()

