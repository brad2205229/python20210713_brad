import random
total = 100
cash = total
limit = int(cash/3)
amount = 0
while cash > 0:
    price = random.randint(1, 100)
    if(cash - price >= 0):
        cash = cash - price
        print('禮物價格 $ %d (買到) 剩下 $ %d' % (price, cash))
        amount = amount +1
    else:
        print('禮物價格 $ %d (沒買到) 剩下 $ %d' % (price, cash))
        # 若還剩下1/3繼續買
        if cash >= limit:
            continue
        else:
            break
avg = (total - cash)/amount
# 統計:
# 總共買到? 份禮物,禮物的平均價格?
print('總共買到 %d 份禮物, 禮物的平均價格 $%.1f, 錢包還剩下 $%d' % (amount, avg, cash))