# list_and_dict.py

# list 是拿來裝連續資料
animals = ['cat', "bird", 'crab'] # python 的單引號和雙引號都代表字串，使用上沒有差別，但建議不要一直換
legs = [4, 2, 10]
print(len(animals)) # 印出 list 的長度
print(animals, ', animals[0]:', animals[0])
print('-'*10)

# dictionary 拿來裝成對資料 (key-value pair)，可當作索引值(index)為字串的 list
num_of_legs = {"cat": 4, "bird":2, "crab": 10}
print(num_of_legs, ', num_of_legs["crab"]:', num_of_legs["crab"])
print('-'*10)


# 可以用 zip 將兩個 list 綁在一起，再 construct 一個新 dictionary
temp = zip(animals, legs)
print(dict(temp))
print('-'*10)

# 可以分別取得 dictionary 的 key 和 value，也可以轉成 list
print(num_of_legs.keys())
print(num_of_legs.values())
print(list(num_of_legs.values()))


