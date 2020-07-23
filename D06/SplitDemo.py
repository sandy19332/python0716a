data = '170,60'

#分割字串
list = data.split(",")
print(list[0],type(list))
print(list[1],type(list))
h = float(list[0])
w = float(list[1])
bmi = "%.2f" %(w/(h/100)**2)
print(bmi)