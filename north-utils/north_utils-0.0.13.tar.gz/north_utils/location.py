from typing import Optional, Union

try:
    from PyQt5.QtGui import QVector3D as Vector3

except ImportError:
    class Vector3:
        # use a, b, c instead of x, y, z to be close to API-compatible with QVector3D (which doesn't support x, y, z kwargs)
        def __init__(self, a: Union[float, 'Vector3'], b: Optional[float]=None, c: Optional[float]=None):
            if isinstance(a, Vector3):
                if b is not None or c is not None:
                    raise TypeError(f'__init__(self, Vector3) takes 2 positional arguments')

                self.a = a.x()
                self.b = a.y()
                self.c = a.z()
            else:
                if a is None or b is None or c is None:
                    raise TypeError(f'__init__(self, float, float, float) takes 4 positional arguments')
                self.a = a
                self.b = b
                self.c = c

        def x(self) -> float:
            return self.a

        def y(self) -> float:
            return self.b

        def z(self) -> float:
            return self.c