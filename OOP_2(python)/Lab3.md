# Lab 3

### Multiplication:
```python
def multiplication(n):
    for i in range(1, 11):
        if(i == 6):
            continue
        if(i == 9):
            break
        print(f"{n} * {i} = {n*i}")

n = int(input("Enter a number: "))
multiplication(n)
```
<br>


### Sum of even number
```python
sum = 0
for i in range(1, 11):
    if(i & 1 != 1):  sum += i

print(f"sum: {sum}")
```
<br>

### Sum of all even number from a list
```python
sum = 0
thislist = [1, 3, 7, 8, 2]
for x in thislist:
    if(x & 1 != 1): sum += x

print(f"sum: {sum}")
```
<br>

### Counting number of even and odd
```python
oddCnt = evenCnt = 0
list1 = [1, 3, 7, 8, 2]
for x in list1:
    if(x & 1 != 1): evenCnt += 1
    else:            oddCnt += 1

print(f"Number of even: {evenCnt} & odd: {oddCnt}")
```
<br>


### Sum of odd indexes value
```python
oddIdxSum = 0
list2 = [1, 3, 7, 8, 2, 5, 10, 3]
for i in range(0, len(list2)):
    if(i & 1): oddIdxSum += list2[i]

print(f"sum of all odd indexes value is: {oddIdxSum}")
```
<br>

### Multiply 5 with odd indexes value:
```python
list2 = [1, 3, 7, 8, 2]
for i in range(0, len(list2)):
    if(i & 1):
        # print(f"{i} * 5 = {list2[i]*5}")
        print(list2[i] * 5, end = " ")      # without newline
print()
```
<br>

## List some operations:
```python
list3 = [1, 3, 5, 7, 4]
# Access:
print(list3[-2], list3[2])
print(list3[-1], list3[1])

# Change:
print(f"Before change: {list3[-3]}")
list3[-3] = 50
print(f"After change: {list3[-3]}")
print()

print(list3[2:4])
print()

# adding the last index 100
list3.append(100)
print(list3)
print()

# insert in index
list3.insert(2, 200)
print(list3)
print()

# Remove last index element
list3.pop()
print(list3)
print()

# Remove the index value
list3.pop(2)
print(list3)
print()

# extend list
list4 = [2, 4, 6]
list3.extend(list4)
print(list3)
print()

# sort
list3.sort()
print(list3)
print()

# Copy
list5 = list3.copy()
print(list5)
print()

# print list using loop
for x in list3:
    print(x, end = " ")
print()

``` 
<br>

#### Python File [Here](Lab3_code.py)
