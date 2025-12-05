with open("day2_input.txt") as f:
    x = f.readline().strip()
    x = x.split(',')
    print(x)

def doub(n):
    if len(n) % 2 == 0:
        if n[:len(n)//2] == n[len(n)//2:]:
            return int(n)
    return False

addition = 0
for i in x:
    x,y = map(int, i.split('-'))
    for o in range(x,y+1):
        if doub(str(o)):
            addition += o
            
print("Final Answer is [!] -> ", addition)
