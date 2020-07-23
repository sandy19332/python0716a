data = '170,60 & 160,40'
#算出這兩筆Bmi各是多少

#二次分割的方法
for row in data.split("&"):
    print(row , type(row))
    r = row.split(",")
    bmi = "%.2f" % (float(r[1])/(float(r[0])/100)**2)
    print(bmi)

