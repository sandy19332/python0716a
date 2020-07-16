#雞+兔子83隻 240隻腳
def calc(x,y):
    rabbit = (y -(2*x))/2
    chicken = x - rabbit
    return (chicken, rabbit)

chicken, rabbit = calc(83,240)
print("雞:%d 兔: %d" % (chicken, rabbit))