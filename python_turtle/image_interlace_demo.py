from turtle import Turtle, mainloop, Screen
from PIL import ImageFile, Image

class Hashing(Turtle):
    def __init__(self, width, height):
        Turtle.__init__(self)
        self.counter = 1
        self.pu()
        self.degrees()
        self.screen_width = width
        self.screen_height = height
        self.reset_pos()
        # self.setpos(width/2, height/2)
        self.speed(0)
        self.pensize(.3)
    def reset_pos(self):
        self.pu()
        self.setpos(0,0)


    def draw_instruction(self, instr):
        for row in instr:
            for i in row:
                if i[0] == 0:
                    self.pu()
                else: 
                    self.pd()
                self.forward(i[1]*3)
            self.pu()
            self.setx(0)
            self.left(90)
            self.forward(3)
            self.right(90)
        self.reset_pos()
        self.left(90)
        self.forward(self.counter)
        self.right(90)
        self.counter += 1

            
def convert_to_chunks(l: list, maxw: int):
    return [l[i:i+maxw] for i in range(0, len(l), maxw)]

def get_turtle_instr(data, maxw):
    chunk = convert_to_chunks(data, maxw)
    instrs = []
    for row in chunk:
        # print(row)
        instr = []
        count = 1
        curr_val = row[0]
        for val in row[1:]:
            if val == curr_val:
                count += 1
            else:
                instr.append((curr_val, count))
                curr_val = val
                count = 1
        instr.append((curr_val, count))
        # print(instr)
        # print()
        instrs.append(instr)
    return instrs

if __name__ == '__main__':
    fname = 'logo.jpg'

    with Image.open(f'src/imgs/{fname}') as img:
        img_buff = img.copy()
    img_p_bbox = img_buff.getbbox()
    img_p_size = tuple(i[1] - i[0] for i in (img_p_bbox[::2], img_p_bbox[1::2]))
    img_p_ratio = img_p_size[1] / img_p_size[0]
    targetheight = 100
    targetwidth = int(img_p_ratio * targetheight)
    print(img_p_size, img_p_ratio, targetheight, targetwidth)
    img_buff = img_buff.resize((targetheight, targetwidth), resample=Image.Resampling.HAMMING)
    img_buff = img_buff.rotate(180, expand=1)
    # img_buff.show()
    img_buff = img_buff.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    img_p_extrema = img_buff.getextrema()    
    img_p_extrema = [[i[0], i[0] - i[1]] for i in img_p_extrema]

    img_d_channel = [list(i) for i in [img_buff.getdata(band=ch) for ch in range(3)]]
    img_d_channel = [[round(j/(img_p_extrema[ch][1]*0.6)) for j in i] for ch, i in enumerate(img_d_channel)]
    img_d_channel_R, img_d_channel_G, img_d_channel_B = img_d_channel
    
    instructions_R = get_turtle_instr(img_d_channel_R, targetheight)
    instructions_G = get_turtle_instr(img_d_channel_G, targetheight)
    instructions_B = get_turtle_instr(img_d_channel_B, targetheight)
    
    screen = Screen()
    screen.bgcolor('black')
    screen.screensize(canvwidth=targetwidth, canvheight=targetheight)
    screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
    screen.tracer(False)

    t = Hashing(targetheight, targetwidth)
    # t.color('yellow')
    t.color('red')
    t.draw_instruction(instructions_R)
    # t.color('magenta')
    t.color('green')
    t.draw_instruction(instructions_G)
    # t.color('cyan')
    t.color('blue')
    t.draw_instruction(instructions_B)

    mainloop()