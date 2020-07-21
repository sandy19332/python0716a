import random
def getScore(p):
    if p == 'A':
        return 1
    elif p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return p #2~10的數字


#牌局開始先發一張
poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'k'] * 4
random.shuffle(poker) #洗牌
print(poker)
p1 = poker.pop()
sum = getScore(p1)
print('已拿:',p1,'總分:' , sum)
print('剩餘:',poker)

#繼續拿牌??
count_user = 0;
while True:
    ask = input('是否要拿牌(y/n)')
    if ask == 'y':
        p = poker.pop()
        sum += getScore(p)
        print('再拿:',p, '總分:',sum)
        if sum > 10.5:
            print('User爆了')
            break
        else:
            count_user += 1
        if count_user == 5:
           print('User 過五關超強der ')
        break
    else:
        break


#PC拿牌
count_pc = 0
p2 = poker.pop()
sum = getScore(p2)
print('PC已拿:',p2,'總分:' , sum)
print('剩餘:',poker)

while True:
    if sum >= 9: #電腦若為9點(含)以上不須補牌
        break
    elif sum <7: #若電腦少於7點強迫補牌
        p = poker.pop()
        sum += getScore(p)
        print('PC再拿:', p, '總分:', sum)
    elif sum == 7 or sum == 7.5:
        amount = poker.count('A')+poker.count('2')+poker.count('3')
        if amount >= 10:
            p = poker.pop()
            sum += getScore(p)
            print('PC再拿:', p, '總分:', sum)
    elif sum == 8 or sum == 8.5:
        amount = poker.count('A')+poker.count('2')
        if amount >= 7:
            p = poker.pop()
            sum += getScore(p)
            print('PC再拿:', p, '總分:', sum)

    if sum > 10.5:
        print('PC爆了')
        break
    else:
        count_pc += 1
    if count_pc == 5:
        print ('PC過五關呃')
        break
