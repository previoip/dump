import traceback
from inspect import getframeinfo, currentframe
from dataclasses import dataclass
from math import sqrt


"""
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
"""


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
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method with type {type(o)}')
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
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method with type {type(o)}')
        return self

    def __mul__(self, o):
        if isinstance(o, self.__class__):
            self.x *= o.x
            self.y *= o.y
            self.z *= o.z
        elif isinstance(o, (int, float)):
            self.x *= o
            self.y *= o
            self.z *= o
        else:
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method with type {type(o)}')
        return self

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
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method with type {type(o)}')
        return self

    
    def __matmul__(self, o):
        if isinstance(o, self.__class__):
            return self.x * o.x + self.y * o.y + self.z * o.z
        else:
            raise TypeError(f'unsupported operand {getframeinfo(currentframe()).function} method with type {type(o)}')

    def __pos__(self):
        return self

    def __neg__(self):
        self.x = -1 * abs(self.x)
        self.y = -1 * abs(self.y)
        self.z = -1 * abs(self.z)
        return self

    def __invert__(self):
        self.x *= -1
        self.y *= -1
        self.z *= -1
        return self


class Vector3(Point):

    def __abs__(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)


if __name__ == "__main__":
    a = Point(1,'2', 3.0)
    b = Point(a)
    print(b)