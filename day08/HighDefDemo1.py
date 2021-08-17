# 高階函式
# 將函式做為參數帶入
def add(x):
    return  x + 1
def sub(x):
    return  x - 1
def calc(func, x):
    result = func(x)
    return result

if __name__ == "__main__":
    print(add(2))
    print(sub(2))
    print(calc(add, 5))
    print(calc(sub, 5))
    