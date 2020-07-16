#define 自帶參數
def printBMI(h,w):
    bmi = w / ((h / 100) ** 2)
    print("%.3f" % bmi)

printBMI(170,60)