
# # The joltage output for the bank is still the number formed by the digits of the 
# # batteries you've turned on; the only difference is that 
# # now there will be 12 digits in each bank's joltage output instead of two.
# # In 987654321111111, the largest joltage can be found by 
# # turning on everything except some 1s at the end to produce 987654321111

# with open("day3_input.txt") as f:
#     lines = f.read().splitlines()
#     # print(lines)

# # def largest(a):
# #     current = 0
# #     for i in range(len(a)):
# #         temp = int(a[i])
# #         for j in range(i + 1, len(a)):
# #             idk = temp*10 + int(a[j])
# #             if idk > current:
# #                 current = idk
# #     return current # bad method but works


# final=0
# for i in lines:
#     # print(largest(i))
#     temp = 0
#     # recursive(i,0,"")
#     final+= temp
#     print(final)

# print("[^] Final Output is -> ", final)

with open("day3_input.txt") as f:
    lines = f.read().splitlines()

# lines = """
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """.split()
def large_fn(num): 
    k = 12
    result = []
    start = 0
    n = len(num)

    while k > 0:
        end = n - k
        max_digit = max(num[start:end+1])
        pos = num.index(max_digit, start, end+1)

        result.append(max_digit)
        start = pos + 1
        k -= 1

    return int("".join(result))
final = 0
for i in lines:
    x = large_fn(i)
    # print(x)
    final += x

print("[^] Final Output is -> ", final)