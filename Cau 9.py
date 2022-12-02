def count_word():
    string = input()
    word = string.split()
    return len(word)
y = int(input("nhập vào toàn bộ: "))
for i in range(1, y+1):
    t = input()
    x = dict()
    for j in t:
        if i in x:
            x[j] += 1
        else:
            x[j] = 1
    print(f"test {i} : {x}", end=" ")