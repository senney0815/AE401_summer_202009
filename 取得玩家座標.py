# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:24:42 2020

@author: sc24
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
print(mc.player.getTilePos())
print()