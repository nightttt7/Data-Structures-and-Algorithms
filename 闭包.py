def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 2, 3)

# f是一个函数,保存了参数和变量
f

# 调用f时,才会返回函数结果
f()

# f这种函数结构被称作闭包


# 返回闭包时牢记一点
# 返回函数不要引用任何循环变量
# 或者后续会发生变化的变量

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
f1()
f2()
f3()
# 调用f1f2f3的时候才执行函数,此时i=3
# 因此答案全部是9
