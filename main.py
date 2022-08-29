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

def main():
    str = "Emma is Emma good  Emma developer. Emma is a writer"
    count = count_emma(str)
    print(count)

## Main function
if __name__ == "__main__":
    main()
