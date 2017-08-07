#Task 1
print("Hello World")
#Task 2
print("Task 2")
hello = "Hello World"
print(hello)
#Task 3
print("Task 3")
def printString(text):
    print(text)
printString("Hi people!")
#Task 4
print("Task 4")
def addingUp(a, b):
    print(a+b)
addingUp(1,2)
#Task 5
print("Task 5")
def addingIfTrue(c, d, trueSum):
    if (trueSum):
        result = c + d
    else:
        result = c * d
    print(result)
addingIfTrue(5,6,False)
#Task 6
print("Task 6")
def makeSureNoZeroes(e, f, trueSum):
    if (e == 0):
        result = f
    elif (f == 0):
        result = e
    else: 
        if (trueSum):
            result = e+f
        else:
            result = e*f
    print(result)
makeSureNoZeroes(3,4,False)
#Task 7
print("Task 7")
for g in range(0,10):
    makeSureNoZeroes(g,4,True)
#Task 8
print("Task 8")
numberList = [1,2,3,4,5,6,7,8,9,10]
for h in range(0,10):
    makeSureNoZeroes(numberList[h],numberList[-(h+1)],False)
#Task 9
print("Task 9")
for i in numberList:
    print(i)
#Task 10
print("Task 10")
valueList = []*10
for j in range(0,10):
    valueList.append(j)
    for j in valueList:
        print(j*10)
#Task 11
print("Task 11")
print("Please enter the size of the list you want")
listSize = int(input("> "))
inputList = []
for k in range(listSize):
    inputList.append(k)
    for k in inputList:
        print(inputList)
#Task 12
print("Task 12")
from functools import partial
def doublingUp(l,m):
    return l*m
print("Enter the number you wish to double and treble")
userNumber = int(input("> "))
double = partial(doublingUp, 2)
triple = partial(doublingUp, 3)
print("Double is",str(double(userNumber)), "and treble is"\
,str(triple(userNumber)))
#Task 13
print("Task 13")
def checkNumbers(n,o):
    if (n > 21 and o > 21):
        result = 0
        print("Both busted!")
    elif (n > o and n <= 21):
        result = n
        print(n, "is the winner!")
    else:
        result = o
        print(o, "is the winner!")
    return result
checkNumbers(22, 19)
#Task 14
print("Task 14")
def uniqueSum(p,q,r):
    if (p == q or p == r):
        return r
    elif (q == r):
        result = p+r
        print(result)
        return result
    elif (r == p or r == q):
        result = p + q
        print(result)
        return result
    elif (p == q and q == r):
        print("0")
        return 0
    else:
        result = p+q+r
        print(result)
print(uniqueSum(1,3,2))