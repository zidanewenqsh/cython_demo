# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(name="example_cython", sources=["example_cython.pyx"]),
    Extension(name="average", sources=["average.pyx"]),
    Extension(name="libexample", sources=["libexample.pyx"], language="c++"),
    Extension(name="cstruct", sources=["cstruct.pyx"]),
    Extension(name="numpy_multiply", sources=["numpy_multiply.pyx"]),
    # Extension(name="multiply_c`ython", sources=["multiply_cython.pyx"]),
    # 添加其他扩展...
]

setup(
    name='Cython Examples',
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level': "3"} # 这行代码指定了 language_level 编译指令，其值为 "3"。这个指令告诉 Cython 编译器使用 Python 3 的语法和语义来编译 .pyx 文件。
        ),
    include_dirs=[numpy.get_include()]
)



# from setuptools import setup
# from Cython.Build import cythonize
# import numpy

# extensions = [
#     # 列出所有的 Cython 模块及其源文件
#     ('example_cython', 'example_cython.pyx'),
#     ('average', 'average.pyx'),
#     ('libexample', 'libexample.pyx'),
#     ('cstruct', 'cstruct.pyx'),
#     ('parallel_sum', 'parallel_sum.pyx'),
#     ('numpy_multiply', 'numpy_multiply.pyx'),
# ]

# setup(
#     name='Cython Examples',
#     ext_modules=cythonize([extension[1] for extension in extensions]),
#     include_dirs=[numpy.get_include()]
# )

# setup(
#     name='Cython App',
#     ext_modules=cythonize(
#         ["example_cython.pyx"], 
#         compiler_directives={'language_level': "3"} # 这行代码指定了 language_level 编译指令，其值为 "3"。这个指令告诉 Cython 编译器使用 Python 3 的语法和语义来编译 .pyx 文件。
#     ),
#     include_dirs=[numpy.get_include()]
# )

# python setup.py build_ext --inplace