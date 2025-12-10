# In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
# In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
# 

with open("day3_input.txt") as f:
    lines = f.read().splitlines()
    # print(lines)

def largest(a):
    current = 0
    for i in range(len(a)):
        temp = int(a[i])
        for j in range(i + 1, len(a)):
            idk = temp*10 + int(a[j])
            if idk > current:
                current = idk
    return current # bad method but works

final=0
for i in lines:
    # print(largest(i))
    final+= largest(i)

print("[^] Final Output is -> ", final)