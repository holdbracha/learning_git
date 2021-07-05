print("hello")
print("I am Brachi")
print("new day")
def print_range(num):
    for i in range(num):
        print(f'num: {i}')

def printSubsequence(input, output):
    if len(input) == 0:
        print(output, end=' ')
        return
    printSubsequence(input[1:], output + input[0])
    printSubsequence(input[1:], output)
printSubsequence("changing goldie to chava", "")
