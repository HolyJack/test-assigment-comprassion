import random

def convertNumberToAscii(num):
    return f"{chr(num // 255)}{chr(num % 255)}"

def convertNumberFromAscii(str): 
    return ord(str[0]) * 255 + ord(str[1])

def serializeArray(numbers): 
    result = ""
    
    for number in numbers:
        result += convertNumberToAscii(number)
    
    return result
        
def desserializeArray(str): 
    arr = []
    for i in range(0, len(str), 2):
        arr.append(convertNumberFromAscii(str[i:i+2]))
        
    return arr

def getRandomArr(size=1000, minVal=0, maxVal=300):
    arr = []
    for _ in range(size):
        arr.append(random.randrange(minVal, maxVal))
        
    return arr

def comprassionValue(arr, s): 
    return len(s) / len(str(arr))

def testCase(arr): 
    s = serializeArray(arr)
    return [str(arr), s, comprassionValue(arr, s)]


def testSerializer():
    
    print(*testCase(getRandomArr(size=50)))
    print(*testCase(getRandomArr(size=100)))
    print(*testCase(getRandomArr(size=500)))
    print(*testCase(getRandomArr(size=1000)))
    
    print(*testCase(getRandomArr(minVal=0, maxVal=9)))
    print(*testCase(getRandomArr(minVal=10, maxVal=99)))
    print(*testCase(getRandomArr(minVal=100, maxVal=300)))
    
    print(*testCase(sorted(getRandomArr(size=300)*3)))
    print(*testCase(sorted(getRandomArr(size=150)*6)))
    print(*testCase(sorted(getRandomArr(size=100)*9)))

testSerializer()