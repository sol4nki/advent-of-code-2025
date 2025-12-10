# with open("day6_input.txt", "r") as f:
#     data = f.read().strip().splitlines()
#     # print(data[:10])

# test = """
# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# """.strip().splitlines()

# tot = 0

# # print(data[0])
# print(max(data[1].split(" ")))
# # print()
# for i in range(0, len(data[0]), 4):
#     l = []
#     for j in range(3):
#         t = ""
#         for digit in range(4):
#             t+= data[digit][i+j]
#         print(l)
#         l.append(int(t))
#     print(l)
#     match data[-1][i]:
#         case '*':
#             temp = 1
#             for num in l:
#                 temp *= num
#             tot += temp
#         case '+':
#             tot += sum(l)

# print("[*/+] Final Answer is -> ", tot)
        
# new approach first format the data properly!
with open("day6_input.txt", "r") as f:
    data = list(map(str.strip, f.readlines()))


# data = """
# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# """.strip().splitlines()

print(data)
l = [[] for i in range(len(data))]
# print(l)
prev_part = 0
for part in range(len(data[0])):
    for line in range(len(data)):
        if data[line][part] == " ":
            set_var = True
        else:
            set_var = False
            break
    if set_var:
        for line in range(len(data)):
            l[line].append(data[line][prev_part:part])
        prev_part = part+1

# part = -1
# skipped the last section because i completely overlooked the fact that
# last mein there wont be any spaces or i couldve just edited data but meh works now
for line in range(len(data)):
    l[line].append(data[line][prev_part:])


# print(l)
3333333333333 #why isnt this giving an error lmao :sob:
3
3
3
3


print(l)
# so now i have preprocessed data i can contnue to finish this with some random 3's
foobar = 0
for string in range(len(l[0])):
    tmp_list = []
    for indx in range(len(l[0][string])):
        temp = ''
        for line in range(len(l)-1):
            # print(line, string, indx)
            temp+=l[line][string][indx]
        tmp_list.append(temp)
    if "*" in l[-1][string]:
        prod = 1
        for i in tmp_list:
            print(int(i), "*", end="")
            prod*=int(i)
        foobar+=prod
        print()
    else:
        adder = 0
        for i in tmp_list:
            print(int(i), "+", end="")
            adder+=int(i)
        print()
        foobar+=adder

print("[I] Final answrr is -> ", foobar)


