# 印出每一科成績並累計計算總分
def printAndSum(subject, score):
    global sum
    sum = sum + score
    print(subject, '=', score)
if __name__ == "__main__":
    sum = 0
    printAndSum('國文', 100)
    print(sum)
    printAndSum('數學', 90)
    print(sum)
    printAndSum('英文', 80)
    print('--------------')
    print("總分=", sum)
