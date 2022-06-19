# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:57:39 2022

@author: legen
"""
from random import randint

## function for two players
def two_players():
     
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')
    
    #count the max number of inputs, if reaches 9 before the game ends, consider the game as draw
    count = 0
    #List to append player 1 and 2 moves
    player_1_move = []
    player_2_move = []
    while(True):
        
        player_1 = input('Player 1, choose a spot: ')
        #check if the spot that player choose is already taken or not, if yes ask the player to choose another spot
        while(spot_check(player_1_move,player_2_move,player_1) == 'taken'):
            player_1 = input('Spot taken, choose free spot: ')

        player_1_move.append(player_1)
        set_table(player_1,'x')
        for i in range(0,3):
                print(table[i])

        count = count + 1
        if win_check(player_1_move,count) == 'over':
            print('Congrats player 1 you won !!!')
            break
        elif win_check(player_1_move, count) == 'Draw':
            print('Game Ended with Draw')
            break
        
        player_2 = input('Player 2, choose a spot: ')
        while(spot_check(player_1_move,player_2_move,player_2) == 'taken'):
            player_2 = input('Spot taken, choose free spot: ')
            
        player_2_move.append(player_2)
        set_table(player_2,'o')
        for i in range(0,3):
                print(table[i])
                
        count = count + 1
        if win_check(player_2_move,count) == 'over':
            print('Congrats player 2 you won !!!')
            break
        elif win_check(player_2_move, count) == 'Draw':
            print('Game Ended with Draw')
            break

#Play with computer
def single_player():
    
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')
    
    count = 0
    continueing = 1
    player_1_move = []
    player_2_move = []
    while(continueing==1):
        
        player_1 = input('Player 1, choose a spot: ')
        while(spot_check(player_1_move,player_2_move,player_1) == 'taken'):
            player_1 = input('Spot taken, choose free spot: ')

        player_1_move.append(player_1)
        set_table(player_1,'x')
        for i in range(0,3):
                print(table[i])

        count = count + 1
        if win_check(player_1_move,count) == 'over':
            print('Congrats player 1 you won !!!')
            break
        elif win_check(player_1_move, count) == 'Draw':
            print('Game Ended with Draw')
            break
        
        #genrate random number for the computer move
        player_2 = str(randint(1, 9))
        while(spot_check(player_1_move,player_2_move,player_2) == 'taken'):
            player_2 = str(randint(1, 9))
        
        print("Computer's move: "+player_2)
            
        player_2_move.append(player_2)
        set_table(player_2,'o')
        for i in range(0,3):
                print(table[i])
                
        count = count + 1
        if win_check(player_2_move,count) == 'over':
            print('Congrats player 2 you won !!!')
            break
        elif win_check(player_2_move, count) == 'Draw':
            print('Game Ended with Draw')
            break

#check if the spot player choose is free or not
def spot_check(move_1,move_2,spot):
    if spot in(move_1) or spot in(move_2):
        return 'taken'
    else:
        return 'free'
    
#check if the game is over or not
def win_check(move,check_draw):
    
    if '1' in(move) and '2' in(move) and '3' in(move):
        return 'over'
    elif '4' in(move) and '5' in(move) and '6' in(move):
        return 'over'
    elif '7' in(move) and '8' in(move) and '9' in(move):
        return 'over'
    elif '1' in(move) and '4' in(move) and '7' in(move):
        return 'over'
    elif '2' in(move) and '5' in(move) and '8' in(move):
        return 'over'
    elif '3' in(move) and '6' in(move) and '9' in(move):
        return 'over'
    elif '1' in(move) and '5' in(move) and '9' in(move):
        return 'over'
    elif '3' in(move) and '5' in(move) and '7' in(move):
        return 'over'
    elif check_draw == 9:
        return 'Draw'

#show the table of the game
def set_table(num,xando):
    num = int(num)
    if num <= 3:
        num = (num*4)-2
        new_table = table[0]
        table[0] = new_table[:num] + xando + new_table[num+1:]
    elif num <= 6:
        num = ((num-3)*4)-2
        new_table = table[1]
        table[1] = new_table[:num] + xando + new_table[num+1:]
    elif num <= 9:
        num = ((num-6)*4)-2
        new_table = table[2]
        table[2] = new_table[:num] + xando + new_table[num+1:]
    else:
        print('Wrong chooise')


while(True):
    #Initiate the game table
    table = ['|   |   |   |', '|   |   |   |', '|   |   |   |']
    print('')
    print('Do you wanna play tic tac tos?')
    want_to_play = input('Replay yes to play or anyother key to quit: ')
    if want_to_play.lower() == 'yes':
        player = input('To play with computer enter 1, To play with friend enter 2: ')
        
        if player == '1':
            single_player()
        elif player == '2':
            two_players()
        else:
            print('Wrong input')
    else:
        break
    


    







        


