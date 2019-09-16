import requests
import json

# 1. get data from api
url = "http://opendata.epa.gov.tw/ws/Data/AQI/?$format=json"
s = requests.get(url)
s_json = json.loads(s.text)

# 2. show the number of data
print(len(s_json))

print(type(s_json[0]['PM2.5_AVG']))

# 3. collect specific attribute into list
data_list = []
for data in s_json:
    try:
        data_list.append(int(data['PM2.5_AVG'])) # type casting to int
    except:
        pass

# 4. plot the graph
import matplotlib.pyplot as plt
plt.title("PM2.5_AVG")
plt.xlabel("index")
plt.ylabel("$μg / m^3$") # LaTeX syntax (nipped by $...$)
plt.plot(data_list)
plt.show()
