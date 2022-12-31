def solve(string):
    print(solveHelper(string))

def solveHelper(string):
    reverseString = string[::-1]
    words = ["dream", "dreamer", "erase", "eraser"]
    words = [word[::-1] for word in words]
    isExist = True
    while len(reverseString) > 0:
        for word in words:
            if reverseString[:len(word)] == word:
                reverseString = reverseString[len(word):]
                break
            if word == words[3]: return "NO"
            
    return "YES"


string = input()

solve(string)