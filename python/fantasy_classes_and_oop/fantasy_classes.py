#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Classes and Inheritance in python

Created on Tue Apr  2 14:53:55 2019
2
@author: Tyler Steele
"""     

from warrior import Warrior
from knight import Knight
from sorceress import Sorceress
    
"""
  Example Scenario
"""
    
# Create 3 characters
player = Warrior('Tyler')
ally = Knight('Lancelot')
enemy = Sorceress('Witch')

# Display beginning stats
player.display_stats()
enemy.display_stats()
ally.display_stats()

player.reckless_strike(enemy)
ally.critical_strike(enemy)

# Display stats after physical attacks
player.display_stats()
enemy.display_stats()
ally.display_stats()

# Test several spells
enemy.cast(enemy, enemy.spells['heal'])
enemy.cast(enemy, enemy.spells['invisible'])
enemy.cast(player, enemy.spells['missile'])
enemy.cast(player, enemy.spells['missile'])
enemy.cast(player, enemy.spells['missile'])
enemy.cast(player, enemy.spells['recover'])
enemy.spells['recover'].change_power(5)
enemy.spells['missile'].change_power(100)
enemy.cast(player, enemy.spells['recover'])

# Display stats after magic attacks
player.display_stats()
enemy.display_stats()
ally.display_stats()

enemy.cast(ally, enemy.spells['missile'])
enemy.cast(ally, enemy.spells['missile'])
enemy.cast(ally, enemy.spells['missile'])
enemy.cast(ally, enemy.spells['missile'])
player.reckless_strike(enemy)

# Display stats after dramatic conclusion
player.display_stats()
enemy.display_stats()
ally.display_stats()

print(f'{player.name}: \"Rest in peace, Sir {ally.name}. I have avenged you!\"\n')


