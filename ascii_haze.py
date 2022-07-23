import random

LENGTH = 10000

def genfill():
    fff = random.randrange(2,16)
    def rr(l):
        fills = '░▒▓█'
        x = int(l/2)
        y = int(l/3)
        z = int(l/4)
        return fills[0]*z + fills[1]*y + fills[2]*x + fills[3]*l + fills[2]*x + fills[1]*y + fills[0]*z
    return rr(fff)

random.seed('foobar')
state = '11'
for i in range(LENGTH):
    i = random.randrange(len(state))
    st = state[i]
    if st == '0':
        print(' ', end='')
    else:
        print(genfill(), end='')
