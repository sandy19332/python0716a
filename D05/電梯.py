from time import sleep
current_floor = 1

print("這是一個7樓的電梯系統，運作如下")
while True:
    target_floor = input('您現在在' + str(current_floor)+'樓，請問想到哪一樓\n>>')
    try:
        target_floor = int(target_floor)
    except ValueError