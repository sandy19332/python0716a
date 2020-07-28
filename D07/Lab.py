def ctof(value) ->float:
    return value *9/5 + 32

def ftoc(value) ->float:
    return(value - 32) * 5/9



num = int(input('欲轉為華氏請按0,轉為攝氏請按1:'))
if num == 0:
    tem = int(input('請輸入攝氏溫度'))
    print(ctof(tem))
elif num == 1:
 tem1 = int(input('請輸入華氏溫度'))
 print(ftoc(tem1))