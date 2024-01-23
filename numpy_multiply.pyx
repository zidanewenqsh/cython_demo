import numpy as np
cimport numpy as np
# 定义一个函数，它接收一个 NumPy 数组和一个乘数，然后将数组的每个元素乘以这个乘数
def multiply_by_constant(np.ndarray[np.int32_t, ndim=1] arr, int constant):
    cdef int i
    cdef int size = arr.size
    # 创建一个新的 NumPy 数组用于存储结果
    cdef np.ndarray[np.int32_t, ndim=1] result = np.empty(size, dtype=np.int32)

    for i in range(size):
        result[i] = arr[i] * constant

    return result
    
def multiply_arrays(np.ndarray[np.float64_t, ndim=1] arr1, np.ndarray[np.float64_t, ndim=1] arr2):
    cdef int n = arr1.shape[0]
    cdef int m = arr2.shape[0]

    # 检查数组长度是否相等
    if n != m:
        raise ValueError("Input arrays must have the same length")

    cdef np.ndarray[np.float64_t, ndim=1] result = np.empty(n, dtype=np.float64)
    cdef int i
    for i in range(n):
        result[i] = arr1[i] * arr2[i]
    return result
