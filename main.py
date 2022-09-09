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


def printEvenValue(strs):
    for i in range(0, len(strs)):
        if i % 2 == 0: print(strs[i])


def removeChars(strs, nums):
    result = strs[nums: len(strs)]
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


def isAppeared(strs, value):
    print(strs.count(value))


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
    reverse = 0
    for i in range(len(str(numb))):
        temp = numb % 10
        numb = numb // 10
        reverse = (reverse * 10) + temp
    if reverse == original:
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
    totalTax = 0
    if amount > 20000:
        totalTax = (10000 * 10) / 100 + ((amount - 20000) * 20) / 100
    if amount <= 20000:
        totalTax = (10000 * 10) / 100
    if amount <= 10000:
        totalTax = 0
    return totalTax


def multipliTable(nums):
    for i in range(nums):
        for j in range(nums):
            print((i + 1) * (j + 1), end=' ')
        print('')


def printDownwardSquarePyramid(rows):
    while rows > 0:
        for j in range(rows):
            print('*', end=' ')
        print('\n')
        rows -= 1


def exponent(base, exp):
    result = 1
    for idx in range(exp):
        result = result * base
    return result


def romanToInt(strs):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    idx = 0
    while idx < len(strs):
        char1 = values[strs[idx]]
        if idx + 1 < len(strs):
            char2 = values[strs[idx + 1]]
            if char1 >= char2:
                total += char1
                idx += 1
            else:
                total -= char1
                idx += 1
        else:
            total += char1
            idx += 1
    return total


def longestCommonPrefix(strs):
    common_prefix = ''
    matching = True
    i = 0
    while matching:
        current_char = strs[0][i] if i < len(strs[0]) else None
        for word in strs:
            if i >= len(word) or word[i] != current_char:
                matching = False
                break
        if matching:
            common_prefix += current_char
            i += 1
    return common_prefix


def mergeListsSort(list1, list2):
    listFinal = []
    if len(list1) == 0:
        listFinal = list2
    if len(list2) == 0:
        listFinal = list1
    else:
        if len(list1) < len(list2):
            for i in list1:
                listFinal = list2
                listFinal.append(i)
        else:
            for i in list2:
                listFinal = list1
                listFinal.append(i)
    listFinal.sort()
    listFinal = set(listFinal)
    return listFinal


def maxProfit(prices):
    maxProfit = 0
    minPrice = prices[0]
    for i in range(len(prices)):
        profit = prices[i] - minPrice
        maxProfit = max(profit, maxProfit)
        minPrice = min(prices[i], minPrice)
    return maxProfit


def plusOne(digits):
    result = []
    num = 0
    if len(digits) < 2:
        num = digits[0]
    else:
        for i in range(len(digits)):
            num = num * 10 + digits[i]
    num += 1
    while num > 0:
        lastDigit = num % 10
        num = num // 10
        result.append(lastDigit)
    return result[::-1]


def searchInsert(nums: list[int], target: int):
    if nums.__contains__(target):
        index = nums.index(target)
    else:
        if target < nums[0]:
            index = 0
        for i in range(len(nums) - 1):
            if nums[i] < target & target <= nums[i + 1]:
                index = i + 1
        if target > nums[len(nums) - 1]:
            index = len(nums)
    return index


def lengthOfLastWord(s:str):
    return len(s.strip().split(' ')[-1])


def main():
    s = "    fly me   to   the moon  "
    print(lengthOfLastWord(s))


## Main function
if __name__ == "__main__":
    main()
