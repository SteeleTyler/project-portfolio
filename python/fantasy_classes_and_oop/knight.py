#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:50:15 2019

@author: Tyler Steele
"""

from hero import Hero
from spells import Heal


"""
  *** Knight ***

  Knight archetype with high health and medium physical damage.
  
  Methods:
    critical_strike(
        target: Hero object to be affected)
    
    If self.condition is not 'Dead' or 'Sleep' and target is not 'Dead', attack 
    target for 2 times the physical_damage. If self.condition is 
    'Invisibile', attack again. Gain experience if target is killed.
      
"""
   
class Knight(Hero):
  def __init__(self, *args, **kwargs):
    super(Knight, self).__init__(*args, **kwargs)
    self.base_health = 50
    self.max_health = 50
    self.heatlth = 50
    self.physical_damage = 4
    self.spells = {'heal': Heal()}
    
  def critical_strike(self, target):
    attack_valid = self.condition != 'Dead' and self.condition != 'Sleep' and target.condition != 'Dead'
    if attack_valid:
      target.damage(self.physical_damage * 2)
      if self.condition == 'Invisible':
        target.damage(self.physical_damage * 2)
        self.condition = 'Well'
      if target.condition == 'Dead':
         self.gain_experience(target.level * 4)
    else:
      print(f'{self.name} cannot attack!')
    
