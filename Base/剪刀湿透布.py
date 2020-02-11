import random

computer = random.randint(1,3)
print(computer)

player = int(input('1:剪刀,2:石头,3:布 请输入：'))
if (player == 1 and computer == 3) or (player == 2 and computer ==1) or (player == 3 and computer == 2):
    print('玩家胜利')
elif (player == computer):
    print('平局，再来')
else:
    print('电脑胜利')
