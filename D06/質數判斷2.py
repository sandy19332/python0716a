#質數判斷 13157 是否為質數

def isPrime(n):
    bool = True #假設是質數
    for i in range (2, n//2+1):  #begin(含) end(不含)
        if n % i == 0:
         bool = False
         break
    return bool

if '__main__' ==__name__: #python的主程式
    for n in range(2,101):
        if isPrime(n):
            print(n)

#__xx__python內含方法