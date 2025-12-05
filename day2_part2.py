# numbers with double and also more than double rep digits like 1212121212 etc


with open("day2_input.txt") as f:
    x = f.readline().strip()
    x = x.split(',')
    print(x)

def doub(n):
    # if len(n) % 2 == 0:
    #     if n[:len(n)//2] == n[len(n)//2:]:
    #         return int(n)
    # return False
    for i in range(len(n)//2):
        temp = n[:i+1]
        if n.count(temp) * len(temp) == len(n):
            return int(n) # WORKED IN FIRST TRY DAWG 
        # BASICALLY TAKE SOME PART LESS THAN HALF OF DIGIT AND CHECK IF THAT PART IS IN N
        # IF ITS COUNT MULTI WITH ITS LEN IS SAME AS LEN N THAT MEANS
        # N IS COMPLETELY COMPOSED OF IT 
        # FIRST TRY FIRST RUN LETS GOO
    return False
        

addition = 0
for i in x:
    x,y = map(int, i.split('-'))
    for o in range(x,y+1):
        if doub(str(o)):
            addition += o
            
print("Final Answer is [!] -> ", addition)
