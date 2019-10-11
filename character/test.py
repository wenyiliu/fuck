# -*- coding: utf-8 -*-

"""
  @date  2019-10-08 
  @author  liuwenyi
  
"""
from pygame import mixer  # Load the required library

mixer.init()
mixer.music.load('/Users/liuwenyi/PycharmProjects/fuck/character/auido.mp3')
mixer.music.play()
