# test_cython_extensions.py

import numpy as np

# 导入 Cython 扩展模块
import example_cython
import average
import libexample
import cstruct
import numpy_multiply
# import multiply_cython
def main():
    # 测试 example_cython
    print("Testing example_cython...")
    nums = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    result = example_cython.sum_of_squares_cython(nums)  # 假设有一个名为some_function的函数
    print("Result from example_cython:", result)

    # 测试 average
    print("\nTesting average...")
    nums = [1, 2, 3, 4, 5]
    avg = average.compute_average(nums)
    print("Average:", avg)

    # 测试 libexample
    print("\nTesting libexample...")
    sq = libexample.py_square(4)  # 假设 libexample 中有一个名为py_square的函数
    print("Square:", sq)

    # 测试 cstruct
    print("\nTesting cstruct...")
    point = cstruct.create_point(2.0, 3.0)  # 假设 cstruct 中有一个名为create_point的函数
    print("Point:", point)

    # 测试 numpy_multiply
    print("\nTesting numpy_multiply...")
    arr1 = np.array([1, 2, 3], dtype=np.float64)
    arr2 = np.array([4, 5, 6], dtype=np.float64)
    result = numpy_multiply.multiply_arrays(arr1, arr2)
    print("Multiply arrays:", result)
    arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    result = numpy_multiply.multiply_by_constant(arr, 3)
    print("Multiply by constant:", result)



if __name__ == "__main__":
    main()

