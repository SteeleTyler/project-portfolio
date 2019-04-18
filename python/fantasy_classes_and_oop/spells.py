#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:07:41 2019

@author: Tyler Steele

Spell Classes
"""

from magic import Magic


"""
  *** Sleep ***

  Sleep spell that sets the targets condition to 'Sleep' (cannot attack), does
  no damage, costs 15 mana, and has a power_level that cannot be changed. 
      
"""

class Sleep(Magic):
  def __init__(self, *args, **kwargs):
    super(Sleep, self).__init__(*args, **kwargs)
    self.condition = 'Sleep'
    self.power_level_max = 1
    self.mana_use = 15
    
    
"""
  *** Heal ***

  Heal spell that sets the targets condition to 'Well' (no effect), does
  negative damage (heals target), costs 10 mana, and power_level max is 10. 
      
"""

class Heal(Magic):
  def __init__(self, *args, **kwargs):
    super(Heal, self).__init__(*args, **kwargs)
    self.damage = -5
    self.condition = 'Well'
    self.mana_use = 10
    
    
"""
  *** Invisibility ***

  Invisibility spell that sets the targets condition to 'Invisible' (next 
  attack does double damage), does no damage, costs 10 mana, and has a 
  power_level that cannot be changed.
      
"""


class Invisibility(Magic):
  def __init__(self, *args, **kwargs):
    super(Invisibility, self).__init__(*args, **kwargs)
    self.condition = 'Invisible'
    self.power_level_max = 1
    self.mana_use = 10
    
    
"""
  *** Missile ***

  Missile spell that does not cause any condition, does damage, costs 5 mana, 
  and has a power_level_max of 10.
      
"""

class Missile(Magic):
  def __init__(self, *args, **kwargs):
    super(Missile, self).__init__(*args, **kwargs)
    self.condition = 'None'
    self.mana_use = 5
    self.damage = 5
    
    
"""
  *** Recover ***

  Recover spell that does not cause any condition, does no damage, costs 
  negative mana (restores mana), and has a power_level_max of 10.
      
"""

class Recover(Magic):
  def __init__(self, *args, **kwargs):
    super(Recover, self).__init__(*args, **kwargs)
    self.condition = 'None'
    self.mana_use = -5 * self.power_level
