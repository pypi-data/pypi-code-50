from .timedelta import TimeDelta
from .settings import Settings


def intersectRect(r1, r2):

    x1 = max(r1[0], r2[0])
    x2 = min(r1[0] + r1[2], r2[0] + r2[2])
    dx = x2 - x1

    if dx < 0:
        return None

    y1 = max(r1[1], r2[1])
    y2 = min(r1[1] + r1[3], r2[1] + r2[3])
    dy = y2 - y1

    if dy < 0:
        return None
    return (x1, y1, dx, dy)


__all__ = ["intersectRect", "TimeDelta", "Settings"]
