# The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 
# 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

with open('day5_input.txt') as f:
    lines = list(map(str.strip, f.readlines()))
    index = lines.index('') # that one line gap b/w ranges n ings '' as i stripped \n when mapping
    # print(index)
    ranges = lines[:index]
    ingredients = lines[index + 1:]


def check_range(ing):
    for i in ranges:
        p, q = map(int, i.split('-'))
        if p <= int(ing) <= q: # as both inclusive :DD
            return True
    return False
fresh = 0 
for i in ingredients:
    if check_range(i):
        fresh+=1

print("[!^!] Total number is -> ", fresh)