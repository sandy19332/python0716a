#質數判斷 13157 是否為質數

n = int(input('請輸入一數字:'))
bool = True #假設是質數
for i in range (2, n//2+1):  #begin(含) end(不含)
    if n % i == 0:
      bool = False
      break
print(n, '是質數' if bool else '不是質數')