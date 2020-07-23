data = '170,60 & 160,40'
#算出這兩筆Bmi各是多少

#二次分割的方法
for row in data.split("&"):
    print(row , type(row))
    h,w = row.split(",")
    bmi ="%.2f" % (float(w)/(float(h)/100)**2)
    print(bmi)
