import random

while True :
    n = random.randint(1,100)
    if n % 3 == 0:
       print(n)
    #若n等於11的倍數就停止(break)
    if n % 11 == 0:
        break