with open("day6_input.txt", "r") as f:
    data = list(map(str.strip, f.readlines()))
pointer = 0
tot = 0

test = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip().split("\n")


k = []
idkidk = []

for i in data:
    k = []
    for j in i.split():
        k.append(j)
    idkidk.append(k)
# print(idkidk)

# not optimal at all but workss

for i in range(len(idkidk[0])):
    l = []
    for o in range(4):
        l.append(idkidk[o][i])
    # print(l, idkidk[3][i])
    match idkidk[-1][i]:

        case '*':
            
            temp = 1
            for num in l:
                temp *= int(num)
            tot += temp
        case '+':
            temp = 0
            for num in l:
                temp += int(num)
            tot += temp

print("[+] Final Answer!! -> : ",tot)

