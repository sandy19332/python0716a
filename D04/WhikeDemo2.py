import random
def check():
    n = random.randint(1,9)
    print(n)
    return True if n% 2 == 0 else False

while check():    #True就會執行
    print("Python")