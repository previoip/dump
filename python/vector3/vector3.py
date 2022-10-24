from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float

class Vector(Point):

    def __add__(self, o):
        self.x += o.x
        self.y += o.y
        self.z += o.z



if __name__ == "__main__":
    a = Vector(1,2)
    print(a)