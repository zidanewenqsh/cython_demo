cdef struct Point:
    double x
    double y

def create_point(double x, double y):
    cdef Point p
    p.x = x
    p.y = y
    return p.x, p.y
