border_chr_range = (9472, 9600)
block_chr_range = (9601, 9636)


class BorderChar:
    direction = ['DIAGONAL', 'HORIZONTAL', 'VERTICAL', 'RIGHT',  'UP', 'LEFT', 'DOWN', 'UPPER', 'LOWER']
    properties = ['LIGHT', 'QUADRUPLE', 'DOUBLE', 'TRIPLE', 'DASH',  'ARC', 'SINGLE', 'CROSS', 'HEAVY']

    def __init__(self, index, attrs):
        self.index = index
        self.property = attrs

    def __repr__(self):
        return f'{self.index} {str(self.properties)}'


if __name__ == '__main__':
    boder_classes = []
    sset = set()

    with open('ascii_table.txt', 'r') as fp:
        lines = fp.readlines()

    for line in lines:
        x = line.split(" b'\\\\N")
        x = [x[0], x[1][1:-3].split(' ')[2:]].copy()
        container = BorderChar(int(x[0]), x[1])
        boder_classes.append(container)

    for borde in boder_classes:
        print(borde)

