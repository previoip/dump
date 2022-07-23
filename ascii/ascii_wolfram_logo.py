from math import floor
logo_string = 'wolfram.'

FILL = 1
BLANK = 0

def fill_options(i: int) -> str:
    chars_len = [(32, 2), (9608, 2), (9619, 2), (9632, 1)]
    if i > len(chars_len):
        i = 1
    return chr(chars_len[i][0])*chars_len[i][1]

def scale_2D_list(arr, scale: int):
    temp = []
    for i in arr:
        row = []
        for j in range(scale):
            row.append(''.join([x*scale for x in i]))
        temp += row
    return temp


if __name__ == '__main__':
    buffer = ''
    for i, c in enumerate(logo_string):
        fill, blank = fill_options(FILL), fill_options(BLANK)
        n = ord(c)
        b = f'{n:08b}'
        s = b[-i:] + b[:-i]
        buffer += s + '\n'
    buffer = buffer.split('\n')
    buffer = scale_2D_list(buffer, 2)
    res = ''
    for s in buffer:
        res += ''.join([fill if i == '1' else blank for i in s])
        res += '\n'
    print(res)
