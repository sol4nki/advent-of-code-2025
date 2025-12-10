with open("day4_input.txt") as f:
    test = list(map(str.strip, f.readlines())) # just rename to test
    # print(lines)

# test = """
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """.strip().split("\n")

def counter(i,j):
    num=0
    if i > 0:
        if test[i-1][j] == '@':
            num+=1
        if j < len(test[i])-1:
            if test[i-1][j+1] == '@':
                num+=1
        if j > 0:
            if test[i-1][j-1] == '@':
                num+=1
    if i < len(test)-1:
        if test[i+1][j] == '@':
            num+=1
        if j > 0:
            if test[i+1][j-1] == '@':
                num+=1
        if j < len(test[i])-1:
            if test[i+1][j+1] == '@':
                num+=1
    if j > 0:
        if test[i][j-1] == '@':
            num+=1
    if j < len(test[i])-1:
        if test[i][j+1] == '@':
            num+=1
    return num

total = 0

def iterative():
    total = 0
    for i in range(len(test)):
        for j in range(len(test[i])):
            # counting logic
            num = 0
            if test[i][j] == '@':
                num+=counter(i,j)

                if num < 4:
                    total+=1
                    print("x", end="")
                    test[i] = test[i][:j] + 'x' + test[i][j+1:]
                else:
                    print(test[i][j], end="")
            else:
                print(test[i][j], end="")
        print()
    return total

x = 1
while x:
    x = iterative()
    total += x

    
print("[!] Final answer is -> : ", total)

