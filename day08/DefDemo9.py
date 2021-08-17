# 寫一個方法能夠自動將列表裡面及格的分數自動+20%
# 例如: scores = [50, 60, 70]
# 變成: scores = [50, 72, 84]
def add(x):
    global scores
    for i in range(0, len(scores)):
        if scores[i] >= 60:
            scores[i] = scores[i] + scores[i] * x / 100
if __name__ == "__main__":
    scores = [50, 60, 70]
    print(scores)
    add(20)
    print(scores)