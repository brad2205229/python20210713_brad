# 遞減迴圈
for x in range(10, 0, -1):
    print(x, end=" ")
print("")
'''
*
**
***
****
*****
****
***
**
*
'''
max = 10# 最多幾顆星
max = max + 1
for x in range(1, max):
    for y in range(0, x):
        print('*', end="")
    print()
for x in range(max-2, 0, -1):
    for y in range(0, x):
        print('*', end="")
    print()

