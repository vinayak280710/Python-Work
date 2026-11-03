
#Question1
tests = [4, 6, 10, 15]

for a in tests:
    last = []
    for i in range(1, a + 1):
        if i % 3 == 0 and i % 5 == 0:
            last.append("FizzBuzz")
        elif i % 3 == 0:
            last.append("Fizz")
        elif i % 5 == 0:
            last.append("Buzz")
        else:
            last.append(str(i))
    print(last)



#Question2
tests = [12321, -5, 100, 7, 1221, 120021]

for x in tests:
    if x < 0:
        print("False")
    else:
        org = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        print("True" if org == rev else "False")


#Question3
tests = [[5, 6, 7], [4, 4], [9, 8, 7, 6, 5, 9], [1], [10, 20, 30, 40, 50, 10]]

for nums in tests:
    list = []
    c = 0
    for num in nums:
        if num in list:
            c += 1
        else:
            list.append(num)
    if c >= 1:
        print("True")
    else:
        print("False")

#Question4
tests = [([1, 5, 8, 3], 11), ([10, 2, 7, 15], 9), ([6, 4, 9, 2], 8), ([-3, 4, 3, 90], 0)]
for nums, target in tests:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print(i, j)


#Question5
tests = [[2, 4, 1], [3, 3, 5, 0, 0, 3, 1, 4], [1, 2, 3, 4, 5], [5], [10, 9, 8, 12]]
for nums in tests:
    max_profit = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            profit = nums[j] - nums[i]
            if profit > max_profit:
                max_profit = profit
    print(max_profit)



#Question6
tests = ["IX", "XL", "MMXXIV", "CDXLIV", "XIV"]
l= []
I ,V ,X ,L ,C ,D ,M = 1 ,5 ,10 ,50 ,100 ,500 ,1000
for i in tests:
    for j in i:
        if j=='I':
            l.append(1)
        if j=='V':
            l.append(5)
        if j=='X':
            l.append(10)
        if j=="L":
            l.append(50)
        if j=='C':
            l.append(100)
        if j=='D':
            l.append(500)
        if j=="M":
            l.append(1000)
   
    sum = 0
    a = l[0]
    
    for k in l:
        if k<=a:
            sum+=k
            a=k
        elif k>a:
            sum = sum +(k-a*2)
            a=k

    l=[]
    print(sum)

  

