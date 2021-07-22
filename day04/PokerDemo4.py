import random as r
def point(p):  # 取得點數
    # A -> 1, J, Q, K -> 0.5點
    if p == 'A':
        return  1
    if p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return int(p)
if __name__ == '__main__':
    pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    r.shuffle(pokers)
