#字典資料格式
fruits = {'orange':20,'apple':10,'watermalon':30}
#利用get(放入key值) 得到value 值
#{'key值':value} 字典格式
print('orange 幾元', fruits.get('orange'))
print('apple 幾元', fruits.get('apple'))
print('watermalon 幾元', fruits.get('watermalon'))
print('banana 幾元', fruits.get('banana'))
print(fruits)
#setdefault(key值, 預設值(若找不到此元素))
print('banana 幾元', fruits.setdefault('banana'),70)
print(fruits)
#取得所有的 key 值
names = fruits.keys()
print(names, type(names))

values = fruits.values()
print(values, type(values), sum(values))

