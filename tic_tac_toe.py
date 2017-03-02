# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:54:15 2017

@author: dhru4670
"""
from random import randrange
import sys

d=10*[' ']
count_x=0
count_o=0

def print_board():
    global d1
    print('_{0}_|_{1}_|_{2}_'.format(d[1],d[2],d[3]))
    print('_{0}_|_{1}_|_{2}_'.format(d[4],d[5],d[6]))
    print('{0}  | {1} | {2}'.format(d[7],d[8],d[9]))

    
def computer():
    global d
    o=randrange(1,10)
    if d[o] == ' ':
        d[o]='o'
        print_board()
        return
    else:
        computer()

        
def user():
    global d
    x=int(input('Enter the pos 1 to 9 : '))
    if d[x] == ' ':
        d[x] = 'x'
        print_board()
        return
    else:
        print('Wrong position entered')
        user()

def check(v):
    global d
    if d[1] == v and d[2] == v and d[3] == v:
        print('Match found for {}'.format(v))
        print('{} Wins !!!'.format(v))
        return True
    elif d[4] == v and d[5] == v and d[6] == v:
        print('Match found for {}'.format(v))
        print('{} Wins !!!'.format(v))
        return True                
    elif d[7] == v and d[8] == v and d[9] == v:
        print('Match found for {}'.format(v))
        print('{} Wins !!!'.format(v))
        return True
    elif d[1] == v and d[4] == v and d[7] == v:
        print('Match found for {}'.format(v))
        print('{} Wins !!!'.format(v))
        return True
    elif d[2] == v and d[5] == v and d[8] == v:
        print('Match found for {}'.format(v))
        print('{} Wins !!!'.format(v))
        return True
    elif d[3] == v and d[6] == v and d[9] == v:
        print('Match found for {}'.format(v))   
        print('{} Wins !!!'.format(v))
        return True
    elif d[1] == v and d[5] == v and d[9] == v:
        print('Match found for {}'.format(v))   
        print('{} Wins !!!'.format(v))
        return True
    elif d[3] == v and d[5] == v and d[7] == v:
        print('Match found for {}'.format(v))   
        print('{} Wins !!!'.format(v))
        return True      
    else:
        pass
    
    
def play():
    global d
    global count_x
    global count_o
    for i in range(9):
        if i%2 == 0:
            user()
            if check('x'):
                count_x+=1
                print('')
                d=10*[' ']
                break
        else:
            computer()
            if check('o'):
                count_o+=1
                print('')
                d=10*[' ']
                break
    else:
        print('Nobody Wins\n')


def main():
    while True:
        play()
        print('Here is Total score so far User:{} Computer:{}'.format(count_x,count_o))
        resp=input("Do you still want to play ? Enter 'Y' or 'N': ")
        if resp == 'N' or resp == 'n':
            print('Here is the Final score so far User:{} Computer:{} \nThanks for playing'.format(count_x,count_o))
            break
        else:
            continue
            
        
if __name__=='__main__':
    main()
