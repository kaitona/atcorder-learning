def solve(string):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    string = string[::-1]
    for i in range(len(string)):
        index += len(s)**i * (s.find(string[i])+1)
    print(index)


string = list(input())
solve(string)