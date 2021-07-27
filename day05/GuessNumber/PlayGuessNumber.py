'''
由系統產生 1~99 之間的亂數
User 與 PC 對戰
'''
import random as r
ans = r.randint(1, 99)
min, max = 0, 100
while True:
    guess = input('User請在 %d ~ %d 之間猜一個數字:' % (min, max))
    guess = int(guess)  # 將字串轉數字
    #  驗證範圍
    if (guess >= max or guess <= min):
        print('User輸入的範圍錯誤')
    else:
        #  判斷User是否猜對
        if guess < ans:
            min = guess
        elif guess > ans:
            max = guess
        else:
            print('恭喜User猜對了!')
            break

    #  PC猜
    guess = r.randint(min+1, max-1)
    print('PC在 %d ~ %d 之間猜一個數字: %d' % (min, max, guess))
    #  判斷PC是否猜對
    if guess < ans:
        min = guess
    elif guess > ans:
        max = guess
    else:
        print('恭喜PC猜對了!')
        break