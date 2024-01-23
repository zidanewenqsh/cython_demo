# example_cython.pyx

# cimport 用于导入特定于 Cython 的模块或者 C 语言的函数
cimport cython

# 定义一个计算平方和的函数
@cython.boundscheck(False)  # 关闭边界检查以提高性能
@cython.wraparound(False)   # 关闭负索引以提高性能
def sum_of_squares_cython(int[:] nums):
    cdef int total = 0
    cdef int i
    for i in range(len(nums)):
        total += nums[i] * nums[i]
    return total
