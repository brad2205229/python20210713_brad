'''
由系統產生 1~99 之間的亂數
假設 ans = 77
      min~max
=> 請在 0~100 之間猜一個數字
使用者猜 50
=> 請在 50~100 之間猜一個數字
使 用者猜 90
=>請在 50~90 之間猜一個數字
...
使用者猜 77
答對了
ps:
最多猜7次，若超過則程式自動結束
'''
import random as r
ans = r.randint(1, 99)
min, max = 0, 100
max_amount = 7
cur_amount = 0
while True:
    # User猜 (最多猜7次)
    cur_amount = cur_amount + 1
    if (cur_amount > max_amount):
        print('次數用完，程式結束。答案: %d' % ans)
        break
    guess = input('(%d/%d)請在 %d ~ %d 之間猜一個數字:' % (cur_amount, max_amount, min, max))
    guess = int(guess)  # 將字串轉數字
    #  驗證範圍
    if (guess >= max or guess <= min):
        print('範圍錯誤，請重新輸入')
        continue
    #  判斷是否猜對
    if guess < ans:
        min = guess
    elif guess > ans:
        max = guess
    else:
        print('恭喜猜對了!')
        break
