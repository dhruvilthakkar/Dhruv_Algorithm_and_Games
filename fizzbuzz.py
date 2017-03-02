#!/usr/bin/env python
from __future__ import print_function

num = input('Enter last number: ')

for x in range(1,num+1):
  if x % 3 == 0 and x % 5 == 0:
    print('FizzBuzz')
  elif x % 3 == 0 :
    print ('Fizz')
  elif x % 5 == 0:
    print('Buzz')
  else:
    print(x)
