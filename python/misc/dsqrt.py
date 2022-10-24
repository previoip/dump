test = [
    1,
    5,
    58,
    234,
    1994,
    4275
]
import time



def solve(n):

    hash_n_romans = {
        1000:   'M', 
        900:    'CM', 
        500:    'D',
        400:    'CD',
        100:    'C', 
        90:     'XC', 
        50:     'L',
        40:     'XL',
        10:     'X', 
        9:      'IX', 
        5:      'V',
        4:      'IV',
        1:      'I',
    }

    romans = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I',]
    nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]


    res = ''
    for v, s in hash_n_romans.items():
        while True:
            if n < v or n == 0:
                break
            n -= v
            res += s
    return res

if __name__ == '__main__':
    for n in test:
        print(f'solving {n}')
        print(solve(n))

