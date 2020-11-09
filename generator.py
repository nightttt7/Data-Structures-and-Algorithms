# get all prime number using generator
def _odd_iter():  # Odd numbers starting from 3
    n = 1
    while True:  # Infinite loop
        n = n + 2
        yield n   # it's a generator


def _not_divisible(n):  # whether x is divisible by n
    return lambda x: x % n > 0


# 思路:
# 第一个素数2
# it=所有奇数
# 第二个素数3
# it=it中不能被3整除的
# it中3的下一个数是5
# 第三个素数5
# it=it中不能被5整除的
# it中5的下一个数是7
# 第四个素数7
# it=it中不能被7整除的
# it中7的下一个数是11
# 第五个素数11
# ...
# 得出包含所有素数的迭代

# Idea:
# The first prime number 2
# it=All odd numbers
# The second prime number 3
# it=it is not divisible by 3
# The next number of 3 in it is 5
# The third prime number 5
# it=it is not divisible by 5
# The next number of 5 in it is 7
# The fourth prime number 7
# it=it is not divisible by 7
# The next number of 7 in it is 11
# The fifth prime number 11
# ...
# Get an iteration containing all prime numbers

def primes():  # All prime numbers
    yield 2  # The first prime number 2
    it = _odd_iter()  # Initial sequence
    while True:  # Infinite loop
        n = next(it)  # Next _odd_iter
        yield n  # Join primes
        it = filter(_not_divisible(n), it)  
        # Filter out odd numbers that are not divisible by n


# Print prime numbers within 1000:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break  # primes() is infinite, so it must break

# ---
# easy implementation of the iterator protocol
# Example of depth-first search using a generator


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# Example
root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
for ch in root.depth_first():
    print(ch)
# Outputs: Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
