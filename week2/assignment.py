from optparse import Values
from re import T
import re
from struct import pack
from tkinter import N


print("---------------------------------------")
print("W2-1")
print("=====")
def calculate(min, max, step):
# 請用你的程式補完這個函式的區塊
    res=0
    for num in range(min, max+1, step):
        res+= num
    print(res)


calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

print("---------------------------------------")
print("W2-2")
print("=====")

def avg(data):
# 請用你的程式補完這個函式的區塊   
   for k, v in data.items():
    sum=0
    i=0
    for item   in v:
        if item["manager"] ==False:
            sum += item["salary"]
            i +=1
    print(sum//i)

avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式


print("---------------------------------------")
print("W2-3")
print("=====")

def func(a):
# 請用你的程式補完這個函式的區塊
    return lambda b, c:print( a + (b * c))
      

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

print("---------------------------------------")
print("W2-4")
print("=====")
def maxProduct(nums):
    result =[]
    newNums = nums[1:]
    for i in nums:
        for j in newNums:
            if i !=j:
                result.append(i*j)
    print(max(result))       

        
  

# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

print("---------------------------------------")
print("W2-5")
print("=====")

   
def twoSum(nums, target):
    # your code here
    diff={}
    for i, num in enumerate(nums):
        if diff.get(num, None) == None:
            diff[target-num]=i
        else:
            return [diff[num], i]
      
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


print("---------------------------------------")
print("W2-6")
print("=====")


def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    count =0
    max_zeros = 0
    for num in nums:
        if num ==0:
            count +=1
        else:
            count =0
        max_zeros = max(max_zeros, count)
    print(max_zeros)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3


