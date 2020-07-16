#加法
def add(x,y):
    print("執行到add()方法",x,y)
    result = x + y
    return result

#訊息說明方法
def info():
    print("執行到info()方法")
    print("本程式是由 Python所撰寫")

#判斷性別
# A155556666
#[1]就是抓維度1的地方(第二個位置)
#M156487942
#0123456789 <-維度(ex.[3]會得到6)(len(id)會得到10)
def checkSex(id):
    sex = id[1]
    if sex == '1':
        print ("男性")
        return
     if sex == '2':
        print("女性")
        return
#主程式
sum = add(10,20)
print(sum)
info()
checkSex(G222406890)
