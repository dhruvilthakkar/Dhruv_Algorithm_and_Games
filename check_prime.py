#!/usr/bin/env python

from __future__ import print_function

def check_prime(num):
  for i in range(2,num):
    if num % i == 0:
      print('Number is not prime')
      break
  print('Number is prime')

num = input('Enter number to check for: ')

check_prime(num)

