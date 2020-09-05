import random

name = input('Enter your name: ')

print(f'Hello, {name}')
namefile = 'rating.txt'
file1 = open(namefile, 'r')
filelist = file1.read().split()
score = 0

if name in filelist:
    indexname = filelist.index(name)
    score = int(filelist[indexname + 1])
    file1.close()
else:
    file1.close()
    file2 = open(namefile, 'a')
    print(f'{name} 0', file=file2)
    file2.close()

option_list = ['scissors', 'paper', 'rock', '!exit', '!rating']
lecit_moves = ["rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"]

gameoptions = input().rsplit(",")
if gameoptions == '':
    pass
else:
    for x in gameoptions:
        if x not in option_list and x in lecit_moves:
            option_list.append(x)

print("Okay, let's start")
option = input()

# game starts
while True:

    # invalid input
    while option not in option_list:
        print('Invalid input')
        option = input()

    ai_move = random.choice(['scissors', 'paper', 'rock'])

# end of the program
    if option == '!exit':
        print('Bye!')
        break

    winning_cases = {
        "water": ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
        "dragon": ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        "devil": ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        "gun": ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        "rock": ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
        "fire": ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        "scissors": ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
        "snake": ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        "human": ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        "tree": ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        "wolf": ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        "sponge": ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        "paper": ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
        "air": ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
        "lightning": ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
    }

    if option == '!rating':
        print(f'Your rating: {score}')

    elif option in winning_cases[ai_move]:
        print(f'Sorry, but computer chose {ai_move}')

    elif ai_move == option:
        print(f'There is a draw ({ai_move})')
        score += 50

    elif option not in winning_cases[ai_move]:
        score += 100
        print(f'Well done. Computer chose {ai_move} and failed')

    option = input()
