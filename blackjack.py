#!/usr/bin/env python

from __future__ import print_function
from random import randint
import sys

class player(object):
  def __init__(self,amount=100,bet=10):
    self.amount=amount
    self.bet=bet

  def __str__(self):
    return 'Object of class player'

  def win(self):
    self.amount+=self.bet

  def loose(self):
    self.amount-=self.bet

  def balances(self,other):
    print('Balance: Player: {0} Computer: {1}\n'.format(self.amount, other.amount))

  def bet(self,bet):
    self.bet=bet

class deck(object):

  def __init__(self):
    self.count=randint(1,11)

  def draw(self):
    self.count+=randint(1,11)

  def printtotal(self,other):
    print('{0} {1}'.format(self.count,other.count))

  def compare(self,other):
    return self.count > other.count

  def reset(self,other):
    self.count=randint(1,11)
    other.count=randint(1,11)
    print('Initial value: {}'.format(self.count))

def play():
  while True:
    ans=raw_input("Do you want to draw or stand ? Enter 'D' to draw and 'S' to stand. Enter N to exit: ")
    if ans == 'D' or ans == 'd':
      dp.draw()
      print('Here is your current value: {}'.format(dp.count))
      if dp.count == 21:
        print('Players count is 21. Player wins !!!')
        p1.win()
        c1.loose()
        p1.balances(c1)
        dp.reset(dc)
      if dp.count > 21:
        print('Sorry you lost. Total is grater than 21')
        p1.loose()
        c1.win()
        p1.balances(c1)
        dp.reset(dc)
      continue
    elif ans == 'S' or ans == 's':
        while True:
            print('Computer Continuing')
            if deck.compare(dc,dp):
              print('Computer wins. Here are total of both players: ')
              deck.printtotal(dc,dp)
              c1.win()
              p1.loose()
              p1.balances(c1)
              dp.reset(dc)
              break
            else:
              dc.draw()
              print("Here is computer's count: {0}".format(dc.count))
              if dc.count > 21:
                print('Computer Bursts !!! Player wins')
                c1.loose()
                p1.win()
                p1.balances(c1)
                dp.reset(dc)
                break
              continue
    elif ans == 'N' or ans == 'n':
      print('\nThank you for playing. Here are final score: ')
      p1.balances(c1)
      sys.exit(1)
    else:
        print("Wrong value entered. Please enter 'D' to draw and 'S' to stand: ")
        continue

p1=player()
c1=player()
dp=deck()
dc=deck()
play()

