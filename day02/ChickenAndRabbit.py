# 1. 使用者輸入雞+兔的總數
# 2. 使用者輸入雞腳+兔腳的總數
# 則系統會自動算出雞兔各有幾隻
if __name__ == '__main__':
    sum = int(input('輸入雞+兔的總數: '))
    # 奇數, 負數, 不是數字資料(try-catch處理)...都會造成都會造成sum錯誤
    # 檢查 sum 是否是奇數或負數
    # homework

    min, max = sum * 2, sum * 4
    feet = int(input('輸入雞腳+兔腳的總數( %d ~ %d ): ' % (min, max)))
    if(min <= feet <= max):
       rabbit = (feet - sum * 2) / 2
       chicken = sum - rabbit
       print("雞:%d 兔:%d" % (chicken, rabbit))
    else:
        print("雞+兔的腳數不再合法範圍內")
