# need to find Left n right pointing at 0

with open("day1_input.txt") as f:
    lines = list(map(str.strip, f.readlines())) # yes i finally know how to use map functionally
    # print(lines)

# print((-5)%100) # since this works i can just use thsi to wrap around

counter = 50
passkey_number = 0

for move in lines:
    # print(move[0])
    if move[0] == 'L':
        counter -= int(move[1:])
        if counter < 0:
            counter = counter % 100
       
    else:
        counter += int(move[1:])
        if counter >= 100:
            counter = counter % 100 
        print(counter)

    if counter == 0:
        passkey_number+=1

# so what i did wrong was the wrap around logic cause R226 and such huge inputs exist breaking normal -100 and +100 cases when < 100 or > 100 respectively.

print("[!] Final answer is -> : ", passkey_number)