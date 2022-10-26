import traceback
from inspect import getframeinfo, currentframe
from dataclasses import dataclass
from math import sqrt

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __post_init__(self):
        if isinstance(self.__dict__.get('x'), self.__class__):
            o = self.__dict__.get('x')
            self.__init__(o.x, o.y, o.z)
            return

        for name, field_type in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                try:
                    self.__dict__[name] = field_type(self.__dict__[name])
                except ValueError:
                    traceback.print_exc()
                    exit(1)

    def set(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        self.__post_init__()

    @property
    def len(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    @property
    def ls(self) -> list:
        return [self.x, self.y, self.z]

    def __eq__(self, o):
        if isinstance(o, self.__class__):
            delta = 1e-10
            return all([
                abs(self.x - o.x) < delta,
                abs(self.y - o.y) < delta,
                abs(self.z - o.z) < delta
            ])
        else:
            return False

    def __add__(self, o):
        if isinstance(o, self.__class__):
            self.x += o.x
            self.y += o.y
            self.z += o.z
        elif isinstance(o, (int, float)):
            self.x += o
            self.y += o
            self.z += o
        else:
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method: \'vector3\' and \'{type(o)}\'')
        return self

    def __sub__(self, o):
        if isinstance(o, self.__class__):
            self.x -= o.x
            self.y -= o.y
            self.z -= o.z
        elif isinstance(o, (int, float)):
            self.x -= o
            self.y -= o
            self.z -= o
        else:
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method: \'vector3\' and \'{type(o)}\'')
        return self

    def __mul__(self, o):
        if isinstance(o, self.__class__):
            return self.x * o.x + self.y * o.y + self.z * o.z
        elif isinstance(o, (int, float)):
            self.x *= o
            self.y *= o
            self.z *= o
        else:
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method: \'vector3\' and \'{type(o)}\'')
        return self
    
    def __matmul__(self, o):
        if isinstance(o, self.__class__):
            self.x = (self.y * o.z) - (self.z * o.y)
            self.y = (self.z * o.x) - (self.x * o.z)
            self.z = (self.x * o.y) - (self.y * o.x)
            return self
        else:
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method: \'vector3\' and \'{type(o)}\'')

    def __truediv__(self, o):
        if isinstance(o, self.__class__):
            self.x /= o.x
            self.y /= o.y
            self.z /= o.z
        elif isinstance(o, (int, float)):
            self.x /= o
            self.y /= o
            self.z /= o
        else:
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method: \'vector3\' and \'{type(o)}\'')
        return self

    def __pos__(self):
        return self

    def __neg__(self):
        self.x *= -1
        self.y *= -1
        self.z *= -1
        return self

    def __invert__(self):
        return self.__neg__()


class Vector3(Point):

    def normalize(self):
        self.__truediv__(self.len)
        return self

if __name__ == "__main__":
    a = Vector3(3,4,0)
    print(a)
    print(a.len)
    a.set(3, 2, 1)
    print(a)
    print(a.len)
    print(a.normalize())
    print(a.len)
    a = a*2
    print(a * [1])
