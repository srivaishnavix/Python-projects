def missingNumbers(n):
    numbers = set(n)
    missednums = []
    for i in range(1,len(n)-1):
        if i not in numbers:
            missednums.append(i)
    return missednums

num = [1,4,5,6,7,8,9]
print(f"The missing numbers in the list are {missingNumbers(num)}")


