data = list(map(list, """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip().split("\n")))
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

def newfn(data, line, row):
    while True:
        while data[line][row] == ".":
            row+=1
            if row == len(data[0]):
                line+=1
                row = 0
            print(".", end="")
        if data[line][row] == "S":
            data[line+1][row] = "|"
            print("S", end="")
            row = 0
            line+=1 # ill just skip to new line 
        while data[line][row] == ".":
            row+=1
            if row == len(data[0]):
                line+=1
                row = 0
            print(".", end="")
        if data[line-1][row] == "|":
            data[line][row] = "|"
        while data[line][row] == ".":
            row+=1
            if row == len(data[0]):
                line+=1
                row = 0
            print(".", end="")
        if data[line][row] == "^":
            one = [r[:] for r in data]
            two = [r[:] for r in data]
            one[line][row-1] = "|" 
            two[line][row+1] = "|" 
            return newfn(one, line, row) + newfn(two, line, row)
        while data[line][row] == ".":
            row+=1
            if row == len(data[0]):
                line+=1
                row = 0
            print(".", end="")
        if line == len(data):
            return 1
        else:
            continue
print(newfn(data, 0, 0))