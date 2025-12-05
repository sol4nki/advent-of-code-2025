# method 0x434C49434B time.
# take into account the fact that going throught 5 -> 99 (L6) we pass throught 0 once
# so need to figure out additional zero crossing logic

with open("day1_input.txt") as f: # same as prev part1
    lines = list(map(str.strip, f.readlines()))
    

test = list(map(str.strip,"""
L150
L50

L150
R50

R150
L50

R150
R50
""".split()))

# print(test)
print(-150//100)
counter = 50
passkey_number = 0

for move in test:

    if move[0] == 'L':
        prev = counter
        counter -= int(move[1:])
        print("L", counter, "passkey: ", passkey_number)
        if counter <= 0:
            if counter == 0:
                passkey_number += 1
            else:
                passkey_number -= counter // 100 
                
                counter = counter % 100
                if prev == 0:
                    passkey_number -= 1
        
        print("new = L", counter, "passkey: ", passkey_number)
       
    else:
        counter += int(move[1:])
        print("R", counter, "passkey: ", passkey_number)
        if counter >= 100:
            passkey_number += counter // 100
            counter = counter % 100 
        print("new R", counter, "passkey: ", passkey_number)

    # if counter == 0:
    #     passkey_number+=1 # still valid
    #     print("====zero xyzxyz====")

# print(-550//100)

print("[!!] Final Answer!!!! -> ", passkey_number)