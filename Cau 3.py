def count_word():
    string = input("Nhập chuỗi: ")
    word = string.split()
    return len(word)

t = int(input("Nhập số lần: "))
if 0 < t <= 100:
    for i in range(1, t+1):
        result = count_word()
        print(f"Lần {i}: {result}", end="\n")