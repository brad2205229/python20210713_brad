# 判斷 x 是否是質數
# 只能被 1 與自己整除
x = 13
isPrime = True
for i in range(2, int(x/2+1)):
    print(i, x % i)
    if x % i == 0:
        isPrime = False
        break
print("%d 是否是質數: %s" % (x, isPrime))

