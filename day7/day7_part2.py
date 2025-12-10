# data = list(map(list, """
# .......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............
# """.strip().split("\n")))

with open("day7_input.txt", "r") as f:
    data = list(map(str.strip, f.readlines()))

# print(data)
first = (1, len(data)/2 -1)

set = {}

coords = []
for line in range(len(data)):
    for content in range(len(data[line])):
        if data[line][content] == "^":
            coords.append((line,content)) 
    
# print(first)
print((coords))
# beam = (1, len(data)/2)
# for i in coords:
#     if i[-1] == beam[-1]:
#         beam = (i[0], i[-1]-1)
        # another case of beam + 1

from functools import lru_cache
# had to import no other choice otherwise it gets too slow

@lru_cache(None)
def beam_calc(beam, cooking):
    for i in coords:
        # print(i)
        if i[0] <= cooking:
            # print("skip -> ", i, end="")
            continue
        if i[-1] == beam[-1]:
            # print("1", (i[0], i[-1]-1),(i[0], i[-1]+1) )
            return beam_calc((i[0], i[-1]-1), i[0]) + beam_calc((i[0], i[-1]+1), i[0])
            # beam_calc((i[0], i[-1]-1), i[0])
            # beam = (i[0], i[-1]-1)
    
    return 1

print(beam_calc(first, 0))

# this was simple i just couldnt figure out the cache part F
# import sys

# with open("day7_input.txt") as f:
#     data = list(map(list, f.read().strip().split("\n")))

# def rec_flow(data, line, row, sett):
#     # row_set = False
#     if sett:
#         data[line][row] = "|"
#         row += 1
    
#     while data[line][row] == ".":
#         row+=1
#         if row >= len(data[0]):
#             line+=1
#             row = 0
    
#     if row == len(data[0]):
#         line+=1
#         row = 0
        
#     if line == len(data):
#         return 1
#     if data[line][row] == "S":
#         data[line+1][row] = "|"
#         row += 1
#     if data[line][row] == "^":
#         print("hi")
#         return rec_flow(data, line, row-1, True) + rec_flow(data, line, row+1, True)

#     # row += 0 if row_set else 1
    



#     return 1 + rec_flow(data, line, row, False)

# # sys.setrecursionlimit(300000) 

    

# print(rec_flow(data, 0, 0, False))

# def newfn(data, line, row):
#     while True:
#         while data[line][row] == ".":
#             row+=1
#             if row == len(data[0]):
#                 line+=1
#                 row = 0
#             print(".", end="")
#         if data[line][row] == "S":
#             data[line+1][row] = "|"
#             print("S", end="")
#             row = 0
#             line+=1 # ill just skip to new line 
#         while data[line][row] == ".":
#             row+=1
#             if row == len(data[0]):
#                 line+=1
#                 row = 0
#             print(".", end="")
#         if data[line-1][row] == "|":
#             data[line][row] = "|"
#         while data[line][row] == ".":
#             row+=1
#             if row == len(data[0]):
#                 line+=1
#                 row = 0
#             print(".", end="")
#         if data[line][row] == "^":
#             one = [r[:] for r in data]
#             two = [r[:] for r in data]
#             one[line][row-1] = "|" 
#             two[line][row+1] = "|" 
#             return newfn(one, line, row) + newfn(two, line, row)
#         while data[line][row] == ".":
#             row+=1
#             if row == len(data[0]):
#                 line+=1
#                 row = 0
#             print(".", end="")
#         if line == len(data):
#             return 1
#         else:
#             continue
# print(newfn(data, 0, 0))