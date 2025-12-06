with open("day6_input.txt", "r") as f:
    data = f.read().strip().splitlines()
    # print(data[:10])

test = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip().splitlines()

tot = 0

# print(data[0])
print(max(data[1].split(" ")))
# print()
for i in range(0, len(data[0]), 4):
    l = []
    for j in range(3):
        t = ""
        for digit in range(4):
            t+= data[digit][i+j]
        print(l)
        l.append(int(t))
    print(l)
    match data[-1][i]:
        case '*':
            temp = 1
            for num in l:
                temp *= num
            tot += temp
        case '+':
            tot += sum(l)

print("[*/+] Final Answer is -> ", tot)
        