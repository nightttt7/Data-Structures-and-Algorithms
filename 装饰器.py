def now():
    print('2015-3-25')

f = now
f()

now.__name__

f.__name__

# 增强now()函数的功能
# 动态增加功能的方式，称之为“装饰器”(Decorator)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 接受一个函数作为参数，并返回一个函数
# func: 被装饰的函数
# wrapper: 增加的功能

@log
def now():
    print('2015-3-25')

# 相当于执行了语句
# now = log(now)

now()