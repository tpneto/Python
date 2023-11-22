import random
from time import sleep

pc_count = 0
player_count = 0
running  = True

while running:
    print('\033[1;31m=-=\033[m'*11)
    print('\033[1;32m*HOW ABOUT A GAME OF ROCK-PAPER-SCISSORS?*\033[m')
    print('\033[1;31m=-=\033[m'*11)

    player = str(input('Rock, Paper, or Scissors? Or (Exit) to close the app.\n')).capitalize().strip()


    if player.lower() == 'exit':
        print('Good Bye!')
        running = False
    else:        
        rock = 'Rock'
        paper = 'Paper'
        scissors = 'Scissors'
        rps = [rock, paper, scissors,]
        computer = random.choice(rps)
        if player in rps:
            if player == rock and computer == paper:
                print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
                print('Computer: \033[1;35m{}\033[m\nPlayer: \033[1;34m{}\033[m\n\033[1;41mYOU LOST!\033[m'.format(computer, player))
                pc_count += 1
                print(f'Score - Player: {player_count}, PC: {pc_count}')
            elif player == rock and computer == scissors:
                print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
                print('Computer: \033[1;35m{}\033[m\nPlayer: \033[1;34m{}\033[m\n\033[1;42mYOU WON!\033[m'.format(computer, player))
                player_count += 1
                print(f'Score - Player: {player_count}, PC: {pc_count}')
            elif player == paper and computer == scissors:
                print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
                print('Computer: \033[1;35m{}\033[m\nPlayer: \033[1;34m{}\033[m\n\033[1;41mYOU LOST!\033[m'.format(computer, player))
                pc_count +=1 
                print(f'Score - Player: {player_count}, PC: {pc_count}')
            elif player == paper and computer == rock:
                print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
                print('Computer: \033[1;35m{}\033[m\nPlayer: \033[1;34m{}\033[m\n\033[1;42mYOU WON!\033[m'.format(computer, player))
                player_count += 1
                print(f'Score - Player: {player_count}, PC: {pc_count}')
            elif player == scissors and computer == rock:
                print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
                print('Computer: \033[1;35m{}\033[m\nPlayer: \033[1;34m{}\033[m\n\033[1;41mYOU LOST!\033[m'.format(computer, player))
                pc_count += 1
                print(f'Score - Player: {player_count}, PC: {pc_count}')
            elif player == scissors and computer == paper:
                print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
                print('Computer: \033[1;35m{}\033[m\nPlayer: \033[1;34m{}\033[m\n\033[1;42mYOU WON!\033[m'.format(computer, player))
                pc_count += 1
                print(f'Score - Player: {player_count}, PC: {pc_count}')
            else:
                print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
                print('Computer: \033[1;35m{}\033[m\nPlayer: \033[1;34m{}\033[m\n\033[1;43mIT\'S A TIE!\033[m'.format(computer, player))
                print(f'Score - Player: {player_count}, PC: {pc_count}')
        else:
            print('\nInvalid option, try again.\n')
