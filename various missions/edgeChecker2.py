def solve(num1, num2):
    if (num1 * 2 == num2) or ((num1 * 2 + 1) == num2):
        return "Yes"
    else: return "No"

a, b = map(int, input().split(" "))
print(solve(a, b))