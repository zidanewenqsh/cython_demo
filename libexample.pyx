cdef extern from "libexample.c":
    double square(double x)

def py_square(double x):
    return square(x)
