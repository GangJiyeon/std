# 파이 계산하기 - 이건 내생각
Pi = 0

play = int(input("반복횟수: "))
plus = True
for i in range(1, 2*play, 2):

    if(plus):
        Pi += 4/i
        plus = False
    else:
        Pi -= 4/i
        plus = True


print(f"Pi = {Pi}")


# 
pi = 0

play = int(input("반복횟수: "))

for n in range(play):
    pi += ((-1) ** n) * (4 / (2*n + 1))

print(f"Pi = {pi}")