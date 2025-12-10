with open("day9_input.txt") as f:
    data = f.read().strip().split("\n")
    # print(data)


test = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip().split("\n")

coord_list = []

# for i in range(len(data)):
#     for j in range(len(data[i])):
#         if data[i][j] == "#":
#             coord_list.append((i, j))

for i in range(len(data)):
    # print(data[i])
    x, y = data[i].split(",")
    coord_list.append((int(x), int(y)))

# print(coord_list)

max = [0,0,0]
for i in coord_list:
    for o in coord_list:
        if max[0] < (abs(i[0]-o[0])+1)*abs((i[1]-o[1])+1):
            max = [(abs(i[0]-o[0])+1)*abs((i[1]-o[1])+1), i, o]

print("Coord list + diag**2 is -> ", max)
# print(max[1][0]*max[2][0])
print("Final Answer is -> ", (abs(max[1][0]-max[2][0])+1)*(abs(max[1][1]-max[2][1])+1))