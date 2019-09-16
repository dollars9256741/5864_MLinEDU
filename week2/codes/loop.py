# loop.py

array1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
array2 = [-1, 10000, 2, 3, 4, 5, 4, 3, 2, 1]


## 一個個存取 array1 裡的每一個 element
### 方法 1
for element in array1:
    print(element*2, end=',')
print()

### 方法 2
for index, element in enumerate(array1):
    print(array1[index]**2, end=',')
print('\n')


## expected value
result = 0
for element in array1:
    result = result + element  # or using '+=' operator
result = result / len(array1)  # or using '/=' operator
print("E(array1): ", result)

### Yet another way to get expectation
print("E(array1): ", sum(array1)/len(array1))
print('-'*10)

## variance
result = 0
mean = sum(array1)/len(array1)
for element in array1:
    result += (element - mean)**2
result /= len(array1)
print("Var(array1): ", result)

mean = sum(array2)/len(array2)
for element in array2:
    result += (element - mean)**2
result /= len(array2)
print("Var(array2): ", result)
print('-'*10)

## using if-else to filter outliers
result = 0
for index, element in enumerate(array2):
    if element < 0: 
        print(index, '-th element is negative :', element)
    elif element > 100:
        print(index, '-th element is too large:', element)
    else:
        result += element
result /= len(array2)  # or using '/=' operator
print("Var(array2 w/o outliers) : ", result)


