#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:53:33 2019

@author: Tyler Steele

Sorceress Class
"""

from hero import Hero
from spells import Sleep, Invisibility, Heal, Missile, Recover

        
"""
  *** Sorceress ***

  Sorceress archetype with low health and low physical damage, but various 
  powerful spells.
  
  Methods:
    cast(
        target: Hero object to be affected,
        spell: Magic object referenced for spell effects)
    
    If self.condition is not 'Dead' or 'Sleep' and target is not 'Dead', 
    attempt to cast spell. If mana is too low, stop. Damage the target for the 
    spell.damage multiplied by spell.power_level. If self.condition is 
    'Invisibile', damage again. Gain experience if target is killed. If the 
    spell has a condition other than 'None', apply that condition to target.
      
"""

class Sorceress(Hero):
  def __init__(self, *args, **kwargs):
    super(Sorceress, self).__init__(*args, **kwargs)
    self.base_health = 25
    self.max_health = 25
    self.heatlh = 25
    self.mana = 25
    self.max_mana = 25
    self.base_mana = 25
    self.physical_damage = 1
    self.spells = {'sleep': Sleep(), 
                   'invisible': Invisibility(), 
                   'heal': Heal(),
                   'missile': Missile(),
                   'recover': Recover()}
    
  def cast(self, target, spell):
    attack_valid = self.condition != 'Dead' and self.condition != 'Sleep' and target.condition != 'Dead'
    if attack_valid:
      try:
        self.mana -= spell.mana_use
        if self.mana < 0:
          self.mana += spell.mana_use
          raise ValueError
        target.damage(spell.damage * spell.power_level)
        if self.condition == 'Invisible':
          target.damage(spell.damage * spell.power_level)
          self.condition = 'Well'
        if target.condition == 'Dead':
          self.gain_experience(4*target.level)
        if spell.condition != 'None':
          target.condition = spell.condition
      except ValueError:
        print(f'{self.name} does not have enough mana.')


