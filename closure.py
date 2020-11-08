# 闭包(Closure)
# Closure example 1


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 2, 3)

# f是一个函数,保存了参数和变量
# f is a function which saved the arguments and varibles
f

# 调用f时,才会返回函数结果
# when f is called, the result return
f()

# f这种函数结构被称作闭包(Closure)
# function with structure like f is called Closure

# ---
# 闭包2
# Closure example 2
from urllib.request import urlopen


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener


# 生成yahoo函数
# generate a function: yahoo
yahoo = urltemplate('https://finance.yahoo.com/quote/{name}/history')
# 调用yahoo函数, 并传入参数 name='AAPL'
# call yahoo with argurment: name='AAPL
for line in yahoo(name='AAPL'):
    print(line.decode('utf-8'))
# 可替代只有单个方法的类
# could inplace class with only one method

# ---
# 返回闭包时牢记一点, 返回函数不要引用任何循环变量, 或者后续会发生变化的变量
# when use Closure, make sure the function returned not use any loop varibales
# or and variable will changed after


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
# when call f1, f2, f3 the function run, and now i=3
# 因此答案全部是9


# ---
# 闭包: 在回调(callback)函数中携带额外的状态
# Closure: carry extra state with callback functions
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def add(x, y):
    return x + y


def make_handler():
    sequence = 0

    def handler(result):
        # nonlocal: declare that the variable is not local
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)


# ---
# access variables defined inside a closure
def sample():
    n = 0

    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


f = sample()
f()

f.set_n(10)
f()

print(f.get_n())
