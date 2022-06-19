# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:38:40 2022

@author: legen
"""
### Question

    # Create a Python project of a Magic 8 Ball which is a toy used for fortune-telling or seeking advice.
    
    #   Allow the user to input their question.
    #   Show an in progress message.
    #   Create 10/20 responses, and show a random response.
    #   Allow the user to ask another question/advice or quit the game.

from random import randint
from tqdm import tqdm
import time

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')

def magic_8_ball():
    response = ['Give libeamlak 100 RMB', 'Ask libeamlak he is best adviser ever', 'shut up and study', 
            'If you can’t make a mistake…You can’t make anything', 'How could you ask this quesion, are you dumb!', 
            'Concentrate and ask again.', 'Cannot predict now.', 'Better not tell you now.', 
            'Ask again later.', 'Reply hazy, try again.', 'Signs point to yes.', 'Yes.', 
            'Outlook good.', 'Most likely.', 'As I see it, yes.', 'You may rely on it.', 
            'Yes definitely.', 'Without a doubt', 'It is decidedly so.', 'It is certain.', "Don't count on it.", 
            'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
    value = randint(0, 24)
    return response[value]

print('Do you want to play?')

answer = input("Enter 'Y' to play or anyother key to quit: ")
answer = answer.lower()

while answer=='y':
    question = input('Please Submit your question: ')
    
    for i in tqdm(range(100),desc='Processing ...'):
        time.sleep(0.03)
        pass
    
    print(magic_8_ball())
    
    answer = input("Enter 'Y' to play, Enter any other key to quit: ")
    






    



