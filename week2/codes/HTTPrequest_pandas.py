import requests
import pandas as pd
import io

# 1. get data from api
url = "http://opendata.epa.gov.tw/ws/Data/AQI/?$format=csv"
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))


# 2. show the number of data
print(df.shape)


# 3. get specific column
cols = ['PM2.5_AVG']
print(df[cols])

# 4. plot the graph
import matplotlib.pyplot as plt
plt.title("PM2.5_AVG")
plt.xlabel("index")
plt.ylabel("$μg / m^3$") # LaTeX syntax (nipped by $...$)
plt.plot(df[cols])
