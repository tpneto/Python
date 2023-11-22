# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

# ------------------------------------------------------------------------------------------ >>RESPONDIDO CORRETAMENTE<<
import random
from time import sleep
print('\033[1;31m=-=\033[m'*11)
print('\033[1;32m*QUE TAL UMA PARTIDA DE JOKENPÔ?*\033[m')
print('\033[1;31m=-=\033[m'*11)

jogador = str(input('Pedra, Papel ou Tesoura? ')).capitalize().strip()
pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'
jkp = [pedra, papel, tesoura]
pc = random.choice(jkp)
if jogador == pedra and pc == papel:
    print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
    print('Computador: \033[1;35m{}\033[m\nJogador: \033[1;34m{}\033[m\n\033[1;41mVOCÊ PERDEU!\033[m'.format(pc, jogador))
elif jogador == pedra and pc == tesoura:
    print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
    print('Computador: \033[1;35m{}\033[m\nJogador: \033[1;34m{}\033[m\n\033[1;42mVOCÊ GANHOUR!\033[m'.format(pc, jogador))
elif jogador == papel and pc == tesoura:
    print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
    print('Computador: \033[1;35m{}\033[m\nJogador: \033[1;34m{}\033[m\n\033[1;41mVOCÊ PERDEU!\033[m'.format(pc, jogador))
elif jogador == papel and pc == pedra:
    print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
    print('Computador: \033[1;35m{}\033[m\nJogador: \033[1;34m{}\033[m\n\033[1;42mVOCÊ GANHOUR!\033[m'.format(pc, jogador))
elif jogador == tesoura and pc == pedra:
    print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
    print('Computador: \033[1;35m{}\033[m\nJogador: \033[1;34m{}\033[m\n\033[1;41mVOCÊ PERDEU!\033[m'.format(pc, jogador))
elif jogador == tesoura and pc == papel:
    print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
    print('Computador: \033[1;35m{}\033[m\nJogador: \033[1;34m{}\033[m\n\033[1;42mVOCÊ GANHOUR!\033[m'.format(pc, jogador))

else:
    print('.'), sleep(0.6), print('..'), sleep(0.6), print('...'), sleep(0.6)
    print('Computador: \033[1;35m{}\033[m\nJogador: \033[1;34m{}\033[m\n\033[1;43mEMPATE!\033[m'.format(pc, jogador))
