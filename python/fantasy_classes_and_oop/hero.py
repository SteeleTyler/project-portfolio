#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:38:38 2019

@author: Tyler Steele

Hero Class
"""


"""
  *** Hero ***

  Base class for all characters
  
  Attributes: 
    name: Display name
    health: Amount of damage that can be taken before death
    max_health: Max amount of health
    base_health: Level 1 max_health, used to determine how much max_health 
      increases on level up
    experience: Point representation of progress towards next level
    experience_max: Amount of experience necessary to reach next level
    experience_base: Level 1 experience_max, used to determine how much 
      experience_max increases on level up
    level: Point representation of general power and progress
    max_level: Level cap
    mana: Currency used to cast spells
    max_mana: Max amount of mana 
    base_mana: Level 1 max_mana, used to determine how much max_mana increases 
      on level up
    physical_damage: Amount of damage done in meelee attack
    condition: Temporary status effect
    spells: Collection of spells available for use
  
  Methods:
    level_up()
    
      Change stats to reflect increase in power
    
    gain_experience(
        amount: Number of points gained)
    
      Increase or decrease experience attribute and level_up if appropriate.
      Cap to upper and lower bounds. (0 to experience_max)
      
    damage(
        amount: Number of points damaged, negative for heal)
    
      Increase or Decrease health of self and kill() if appropriate.
      Cap to upper and lower bounds. (0 to max_health)
      
    kill()
    
      Set condition to 'Dead'. Should be used for any future on-death effects.
      
    display_status()
    
      Print relevant attribute values and labels.
      
"""

class Hero():
  def __init__(self, name):
    self.name = name
    self.health = 25
    self.max_health = 25
    self.base_health = 25
    self.experience = 0
    self.experience_max = 100
    self.experience_base = 100
    self.level = 1
    self.max_level = 20
    self.mana = 0
    self.max_mana = 0
    self.base_mana = 0
    self.physical_damage = 1
    self.condition = 'Well'
    self.spells = {}
  
  def level_up(self):
    print(f'{self.name} leveled up!')
    try:
      self.level += 1
      if self.level > self.max_level:
        self.level = self.max_level
        raise ValueError
      self.capacity += self.base_capacity / 5
      self.max_health += self.base_health / 5
      self.heatlh = self.max_health
      self.max_mana+= self.base_mana / 5
      self.mana = self.max_mana
      self.experience -= self.experience_max
      self.experience_max += self.experience_base/5
      self.experience_base += self.experience_base/4
    except ValueError:
      print(f'{self.name} is max level.')
    
  def gain_experience(self, amount):
    self.experience += amount
    if self.experience > self.experience_max:
      self.level_up()
    if self.experience < 0:
      self.experience = 0
      
  def damage(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.kill()
    if self.health > self.max_health:
      self.health = self.max_health

  def kill(self):
    self.condition = 'Dead'
    self.health = 0
    
  def display_stats(self):
    print(f'Stats for {self.name}: \n')
    print(f'Health: {self.health} / {self.max_health}')
    if self.max_mana > 0:
      print(f'Mana: {self.mana} / {self.max_mana}')
    print(f'Condition: {self.condition}')
    print(f'Experience: {self.experience}')
    print(f'Level: {self.level}\n')
      

