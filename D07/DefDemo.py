def calc(x=1, y=2):
    return x+y

def calc2(x=None, y=None):
    if x == None:
        print('使用者沒帶入x值')
        return 0
    if y == None:
        print('使用者沒帶入y值')
        return 0
    return x+y

if __name__ =='__main__':
    sum = calc (10, 20)
    print(sum)
    sum = calc(7)
    print(sum)
    sum = calc(y=7)
    print(sum)

    sum = calc2(6)
    print(sum)