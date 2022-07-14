import random
head = 0
tail =0
num = 0.5
print("Enter how many Times you flip the coin")
flip = int(input())
for count in range(1,flip+1):
    ran = random.random()
    if ran<num:
        tail += 1
    else:
        head += 1
print("No. of Heads = ", head)
print("No. of tails = ", tail)

Head_Percent = (head * 100)/flip
Tail_Percent = (tail * 100)/flip
print("Head Percentage :- ", Head_Percent)
print("Tail Percentage :- ", Tail_Percent)