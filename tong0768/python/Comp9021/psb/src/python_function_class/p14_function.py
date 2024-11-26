"""函数"""


def my_print(*param, num=2):
    """打印"""
    for i in range(num):
        print(param)
    """打印2"""
    return 0


my_print('huang', 'yi', 'tong', num=3)


print(my_print.__doc__)
print(my_print.__annotations__)
print(my_print.__class__)
print(my_print.__code__)
print(my_print.__module__)


def sum(a, b):
    return a + b


print(sum(10, 20))


def inc(a):
    a += 1
    return a


a = 10
print(inc(a))
print(a)


def change_list(l):
    l[0] = 10


def multi(a, b):
    return a * b


def calc(a, b, op):
    print(op(a, b))


calc(3, 5, sum)
calc(4, 7, multi)


print("before main")


if __name__ == '__main__':
    print("inside main")


print("after main")


