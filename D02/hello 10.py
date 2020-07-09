import math
x0,y0=10,2
x1,y1=4,20
d = math.sqrt(math.pow(x0-x1,2) + math.pow(y0-y1,2))
result = 'a點座標({0},{1})b點座標({2},{3})直線距離{4:.2f}'.format(x0,y0,x1,y1,d)
print(result)