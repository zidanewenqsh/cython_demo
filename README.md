# cython_demo
我练习用使用cython的工程
# Cython 示例
此仓库包含了一系列的 Cython 模块示例，展示了 Cython 的各种功能和特性。Cython 是一种编程语言，它使得为 Python 编写 C 扩展与编写 Python 本身一样简单。它旨在成为 Python 语言的超集，允许为 Python 编写 C 扩展。

# 环境要求
Python 3.x
Cython
NumPy
C/C++ 编译器（如 Linux/Mac 的 GCC 或 Windows 的 MSVC）

# 安装
要安装 Cython 扩展，请在此仓库的根目录下运行以下命令：
```bash
python setup.py build_ext --inplace
```
这将编译 .pyx 文件为共享库文件（.so 或 .pyd 文件，具体取决于您的操作系统），可以直接在 Python 中导入使用。

# 包含的示例
1. example_cython
使用 Cython 加速 Python 函数的简单示例。它包含了一个计算数组平方和的函数。

2. average
此模块展示了如何用 Cython 编写计算列表中数字平均值的函数。它演示了类型内存视图和基本的 Cython 优化的使用。

3. libexample（C++）
一个使用 Cython 接口与 C++ 代码的示例。此模块展示了如何包装 C++ 类和函数。请确保对此模块使用 C++ 编译器。

4. cstruct
此示例演示了如何在 Cython 中操作 C 结构体。包括定义结构体和操作这些结构体的函数。

5. numpy_multiply
展示了如何在 Cython 中与 NumPy 数组进行交互的示例。它包含了一个逐元素乘以两个 NumPy 数组的函数，展示了如何在 Cython 中使用 NumPy 的 C API。

# 使用方法
编译扩展后，您可以像普通的 Python 模块一样在 Python 中导入和使用它们。例如：

```python
import example_cython
result = example_cython.sum_of_squares([1, 2, 3, 4, 5])
print(result)
```
# 注意事项
1. 如果您在不同的 Python 版本之间切换或更改源文件，请记得清理构建产物。您可以通过删除生成的 .so 或 .pyd 文件和任何临时构建目录来清理构建产物。
2. 源文件命名冲突：在编译 Cython 模块（如 libexample.pyx）时，Cython 会生成一个与源文件同名但后缀为 .c 的中间文件（例如 libexample.c）。如果您的项目中已经存在同名的 .c 文件，这可能会导致冲突。为避免此类冲突，请确保您的 Cython 源文件（.pyx）和任何现有的 C/C++ 源文件（.c/.cpp）不具有相同的基本文件名。
3. 手动删除生成的 .c 文件：如果在修改 .pyx 文件后遇到编译问题，尤其是在出现意外的编译错误或运行时行为时，考虑删除由 Cython 自动生成的 .c 文件，并重新编译。这有助于确保所有更改都已正确应用。
4. 为了防止误删，libexample.c在backup目录中提供备份文件。
5. `python setup.py build_ext --inplace`中的--inplace参数允许在 Python 环境中直接导入编译的 Cython 模块，而无需将编译的模块复制到 Python 环境中。

# GitHub
项目源代码可在 GitHub 上找到：[GitHub 项目链接](https://github.com/zidanewenqsh/cython_demo)

# 许可证
该项目采用 MIT 许可证。详情请见 LICENSE 文件。