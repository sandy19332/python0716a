import requests
import json
path ='https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceQualified.aspx'
data = requests.get(path).text #取得網路原始字串資料
list = json.loads(data) #將 json字串模式轉成 Python 可用的物件

for rice in list:
    name = str(rice.get('品名'))
    if name.__contains__('池上米'):
       print(rice.get('品名'),rice.get('國際條碼'))