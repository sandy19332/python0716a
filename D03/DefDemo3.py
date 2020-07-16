def getBMI(h,w):
    bmi = w/((h/100))**2
    return bmi

bmi = getBMI(170,60)
print("%.3f" % bmi)