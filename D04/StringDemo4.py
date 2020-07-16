report = "台積電目前價格每股315.5元，可賣出4000股，目前我的庫存有6000股"
#求賣出後的庫存總值?
price = report[9:14]
剩餘 = int(report[32:35]) - int(report[19:22])
庫存總值 = 剩餘 * float(price)
print(庫存總值)