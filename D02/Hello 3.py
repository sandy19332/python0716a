#資料的轉換
x = input('請輸入一個數字x :')
y = input('請輸入一個數字y :')
print(x,y)
sum = x + y
print(sum)
#觀察x y的資料型態
print(x,type(x),y,type(y))
#x跟y都是str字串
#所以要透過int來把數字轉為字串
sum = int(x) + int(y)
print(sum)