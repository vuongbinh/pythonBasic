def multipleOrSum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

def iterationSum():
    print("Printing current and previous number sum in a range(10)")
    for i in range(1, 11):
        previous_Number = i - 1
        print("Current Number", i, "Previous Number", previous_Number, "Sum: ", i + previous_Number)

def printEvenValue(str):
    for i in range(0, len(str)):
        if (i % 2 == 0): print(str[i])

def removeChars(str, nums):
    result = str[nums: len(str)]
    return result

def checkNumberInList(arr):
    if arr[0] == arr[-1]:
        return True
    else:
        return False

def isDivisibleForFive(arr):
    for item in arr:
        if item % 5 == 0:
            print(item)

def isAppeared(str, value):
    print(str.count(value))

def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

def printTriangle(rows):
    for i in range(rows):
        for j in range(i):
            print(i, end=' ')
        print('')

def isPalindromeNumber(numb):
    print(str(numb))
    print(len(str(numb)))
    original = numb
    reversed = 0
    for i in range(len(str(numb))):
        temp = numb % 10
        numb = numb // 10
        reversed = (reversed * 10) + temp
    if reversed == original:
        print("Yes, this is Palindrome number")
        return True
    else:
        print('No, this is not Palindrome number')
        return False

def mergeListByCondition(list1, list2):
    finalList = []
    for index in range(len(list1)):
        if list1[index] % 2 != 0:
            finalList.append(list1[index])
    for index in range(len(list2)):
        if list2[index] % 2 == 0:
            finalList.append(list2[index])
    finalList.sort()
    print(finalList)

def reverseNumber(numb):
    extract = []
    for idx in range(len(str(numb))):
        temp = numb % 10
        extract.append(temp)
        numb = numb // 10
    return extract

def calculateIncomeTax(amount):
    if amount > 20000:
        totalTax = (10000 * 10)/100 + ((amount - 20000) * 20) / 100
    if amount <= 20000:
        totalTax = (10000 * 10) / 100
    if amount <= 10000:
        totalTax = 0
    return totalTax

def multipliTable(nums):
    for i in range(nums):
        for j in range(nums):
            print((i+1)*(j+1), end=' ')
        print('')

def printDownwardSquarePyramid(numsOfRows):
    while numsOfRows > 0:
        for j in range(numsOfRows):
            print('*',end=' ')
        print('\n')
        numsOfRows -= 1

def exponent(base, exp):
    result = 1
    for idx in range(exp):
        result = result*base
    return result

def main():
    base = 5
    exp = 4
    print(base, ' raises to the power of ', exp, ':', exponent(base,exp))

## Main function
if __name__ == "__main__":
    main()
