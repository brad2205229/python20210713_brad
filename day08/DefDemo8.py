# 寫一個方法能夠自動將 scores 裡面的分數自動+10
# 例如: scores = [50, 60, 70]
# 變成: scores = [60, 70, 80]
def add(scores, x):
    for i in range(0, len(scores)):
        scores[i] = scores[i] + 10
    pass
def add(x):
    global scores
    for i in range(0, len(scores)):
        scores[i] = scores[i] + 10
if __name__ == "__main__":
    scores = [50, 60, 70]
    # add(scores, 10)
    print(scores)
    add(10)
    print(scores)