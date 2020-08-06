class Account:
    __money = 0 #物件屬性/變數/資產
    # 加兩個底線表示私有屬性

    def __init__(self, x) -> None:
        self.__money = x   #開戶時所存的第一筆金額

    def transfer(self, accountName, x):
        print("轉帳給:"+ accountName + "，金額:$"+str(x))
        if x <=0:
            print("轉帳金額必須大於零")
            return 
        if x > self.__money:
            print('轉帳金額過大，餘額不足拉~~~~')
            return
        self.__money = self.__money - x

    def save(self, x):
        print("存款: $" + str(x))
        if x <=0:
            print('存款必須 > 0')
            return
        self.__money = self.__money + x

    def withdraw(self, x): #x表示要提款的金額
        print("提款: $" + str(x))
        if x <=0:
            print('金額必須 > 0')
            return
        if x > self.__money:
            print('提款金額過大，餘額不足拉~~~~')
            return
        self.__money = self.__money - x

    def __str__(self) -> str:
        return "帳戶餘額: $" +str(self.__money)

if __name__ == '__main__':
    account1 = Account(30000)   #建立一個物件
    print(account1)
    account1.withdraw(6000)
    print(account1)
    account1.save(10000)
    print(account1)
    account1.transfer('Mary', 16000)
    print(account1)