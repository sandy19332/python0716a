exchange = {
    'usd' : lambda money : print(money / 30),
    'jpy' : lambda money : print(money * 4),
}
exchange.get('usd')(900) #右邊的括號填錢錢 哈哈要加.get喔
exchange.get('jpy')(900)
