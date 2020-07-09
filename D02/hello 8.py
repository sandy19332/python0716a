print('BMI系統')
name = input('請輸入姓名')
x =float(input('請輸入身高(cm)'))
y =float(input('請輸入體重(kg)'))
BMI = y/((x/100)**2)
result = '正常' if 18< BMI<=23 else '過高' if BMI>18 else '過輕'
print('%s的身高是%5.1f cm 體重是 %5.1f kg BMI計算結果為%5.2f(%s)'
      %(name,x,y,BMI,result))