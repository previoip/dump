from turtle import Turtle, mainloop, Screen

block = \
"""
#####  #####  #####  
#   #     ##  ##   
# # #   #        #
#   #  #          #
#   #  #          #
#####  #####  #####

#####  #####  #####  
#   #     ##  ##   
# # #   #        #
#   #  #          #
#   #  #          #
#####  #####  #####

"""

block = block.strip()

class TurtleBloc(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.screen = Screen()
        self.screen.tracer(False)
        self.speed(0)
        self.size = 10
        self.pu()
        self.degrees()
        self.fillcolor('green')

    def drawbox(self, fill=False):
        self.pd()
        if fill:
            self.begin_fill()
        for _ in range(4):
            self.forward(self.size)
            self.left(90)
        if fill:
            self.end_fill()
        self.pu()

    def parseblocq(self, blockstr):
        blockstr = blockstr.split('\n')
        for row in blockstr:
            for char in row:
                if char == '#':
                    self.drawbox()
                    self.forward(self.size)
                else:
                    self.forward(self.size)
            self.right(180)
            self.forward(len(row)*self.size)
            self.left(90)
            self.forward(self.size)
            self.left(90)
            

if __name__ == '__main__':
    t = TurtleBloc()
    t.size = 20
    t.setheading(5)
    t.parseblocq(block)
    mainloop()
