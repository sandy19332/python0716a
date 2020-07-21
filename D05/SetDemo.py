import random as r
lotto = []
while len (lotto) <5 :
    lotto.append(r.randint(1,10))
print(lotto,"可變更，可重複")

lotto = tuple(lotto)
print(lotto,"不可變更")

lotto2 = set()
while len (lotto2) <5 :
    lotto2.add(r.randint(1,10))
print(lotto2,"可變更，不可重複")