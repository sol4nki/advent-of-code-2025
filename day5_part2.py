# The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 
# 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

with open('day5_input.txt') as f:
    lines = list(map(str.strip, f.readlines()))
    index = lines.index('') # that one line gap b/w ranges n ings '' as i stripped \n when mapping
    # print(index)
    ranges = lines[:index]
    ingredients = lines[index + 1:]
inventory = 0

x = []
j = []
for i in ranges:
    p, q = map(int, i.split('-'))
    x.append((p, q))
    j.extend([p,q])
x.sort()
# print(x)

# somehow intersect these values like 12 - 18 and 16 - 20 can be merged to 12 - 20
merged = []

for start, end in x:
    if not merged:
        merged.append([start, end])
        continue
    if merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
print(merged)
        
for i in merged:
    inventory += (i[1] - i[0] + 1)



print("[!^!] Total number is -> ", inventory)