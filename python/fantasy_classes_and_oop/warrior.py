#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:52:08 2019

@author: Tyler Steele

Warrior Class
"""

from hero import Hero

    
"""
  *** Warrior ***

  Warrior archetype with medium health and high physical damage.
  
  Methods:
    reckless_strike(
        target: Hero object to be affected)
    
    If self.condition is not 'Dead' or 'Sleep' and target is not 'Dead', attack 
    target for 3 times the physical_damage. If self.condition is 
    'Invisibile', attack again. Attack self for physical_damage. Gain 
    experience if target is killed. Die if self is killed.
      
"""

class Warrior(Hero):
  def __init__(self, *args, **kwargs):
    super(Warrior, self).__init__(*args, **kwargs)
    self.base_health = 40
    self.health = 40
    self.max_health = 40
    self.physical_damage = 5
    
  def reckless_strike(self, target):
    attack_valid = self.condition != 'Dead' and self.condition != 'Sleep' and target.condition != 'Dead'
    if attack_valid:
      target.damage(self.physical_damage * 3)
      if self.condition == 'Invisible':
        target.damage(self.physical_damage * 3)
        self.condition = 'Well'
      self.damage(self.physical_damage)
      if target.condition == 'Dead':
         self.gain_experience(target.level * 4)
    else:
      print(f'{self.name} cannot attack!')


