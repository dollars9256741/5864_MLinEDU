import json
import requests
from pprint import pprint

# get data from HTTP request
# 用 HTTP request 抓取網頁資料

## <Notes> 有很多類似的 package (e.g. request, requests, PycURL) 
## 可做到一樣的功能，要注意每個 package 回傳的資料結構可能差很多。
r = requests.get('https://pm25.lass-net.org/data/last-all-airbox.json')
data = r.text # text 是以 string 的格式存剛抓到的資料
# 可以用 dir(r) 來查詢 r 的 member function

# cf. 
## print raw data(string format) from RESTful api
print(data)
print('-'*20)

## wrap raw data as json structure (nested dictionary)
json_data = json.loads(r.text)
print(json_data)
print('-'*20)

## use PrettyPrint to get better visualization
pprint(json_data)
pprint('-'*20)

