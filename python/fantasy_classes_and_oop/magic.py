#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:16:02 2019

@author: Tyler Steele

Magic Class
"""


    
"""
  *** Magic ***

  Base class for all spells
  
  Attributes: 
    power_level: Damage modifier, can be used to increase effectiveness in 
      other ways
    power_level_max: Max value for power_level
    damage: Amount of damage done, can be negative for heal
    mana_use: Amount of mana a Sorceress must use for the spell. Can be 
      negative for mana recovery
    condition: Effect that is applied to the target upon casting the spell
    
  
  Methods:
    change_power()
    
      Change power_level up or down while keeping it within bounds (1, max)
      
"""
    
class Magic():
  def __init__(self):
    self.power_level = 1
    self.power_level_max = 10
    self.damage = 0
    self.mana_use = 0
    self.condition = 'None'
        
  def change_power(self, amount):
    self.power_level += amount
    if self.power_level < 1:
      self.power_level = 1
    if self.power_level > self.power_level_max:
      self.power_level = self.power_level_max
      
