def add(x):
    return x + 1
def sub(y):
    return y - 1

def calc(func, n):
    result = func(n)
    return result


if __name__ =='__main__':
    print(calc(add, 5))
    print(calc(sub, 7))
