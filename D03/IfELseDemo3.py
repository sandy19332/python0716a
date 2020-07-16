#撰寫一格bmi計算系統
def  calcBMI():
    h = float(input('您的身高(cm):'))
    w = float(input('您的體重(kg):'))
    bmi = w / ((h/100)**2)
    result = "過重" if (bmi >23)   else "過輕" if (bmi< 18) else "正常"
    print("身高: %.1f 體重: %.1f BMI:%.2f(%s)" % (h, w, bmi, result))
def menu():
    print("BMI計算系統")
    print("----------")
    print("1.開始系統")
    print("2.離開系統")
    id = int(input('請選擇:'))
    if id == 1:
        print("您選擇的是1")
        calcBMI()
        input('請按任意鍵繼續...')
        menu()
    elif id == 2:
        print("您選擇的是2")
        print("Thanks for using.")
    else:
        print("選擇錯誤")
        print("不要給我亂輸入阿笨蛋 就說是1跟2你想輸入啥")
menu()