import math as m
# 資料轉換
chinese = "90"
math = "80"
english = "100"
sum = chinese + math + english
print("sum=", sum)  # 「+」號對字串而言是連接符號
print(type(chinese), type(math), type(english))
sum2 = int(chinese) + int(math) + int(english)
print("sum2=", sum2)
# 資料的轉換(Lab)
# 球 bmi 取道小數點2位
h, w = "180.5", "85"
print(type(h), type(w))
h = float(h)
w = float(w)
print(type(h), type(w))
bmi = w / m.pow(h/100, 2)
print("bmi= %.2f" % bmi)