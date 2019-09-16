# set_and_tuple.py

# set 可以當作數學上的集合，set 內元素是無序且不重複

## 建立 set 可以用下面兩種方式
vegetables = {'apple', 'orange', 
              'tomato', 'apple'} # apple 重複，只計一次
fruits = set(['tomato', 'spinach', 'broccoli'])

## 用換行符號 '\n' 來隔開兩個要印的 set
print(vegetables, fruits, sep='\n')

## 集合間的運算 (e.g. 交集、聯集、差集）
print("Intersection of veggies & fruits: ", vegetables & fruits)
print("Unions of veggies & fruits: ", vegetables | fruits)
print("veggies not fruits: ", vegetables - fruits)
print('\n', '-'*10, '\n')


# tuple 即數學上的有序對，元素順序是固定的
# python 內的 tuple 可視為不可變動的序列(immutable list)

t1 = (1, 3, 2, 6, 7)
print(t1)

## 你可以試試看把下面那行註解拿掉會發生什麼事
## t1[0] = 5

## 一般的 list 可以賦值也可以進行排序 
l1 = list(t1)
l1[0] = 5
print("\nAfter assign l1[0] to 5 : \n", l1)

l1.sort()
print("\nAfter sort l1 : \n", l1)
