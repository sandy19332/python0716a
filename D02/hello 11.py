#骰子遊戲 決定比大(輸入1)比小(輸入0
flag = int(input('比大(輸入1)or比小(輸入0):')
user = r.randint(1,6)+r.randint(1,6)+r.randint(1,6)
pc = r.randint(1,6)+r.randint(1,6)+r.randint(1,6)
if flag == 1:
    winner = '使用者' if user > pc else '電腦'
else :
    winner = '使用者' if user < pc else '電腦'
result = '比{0},使用者的點數:{1},電腦的點數:{2},贏家是{3}'\
    .format('大' if flag== 1 else '小',user,pc,winner)
print(result)
