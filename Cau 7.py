def count_word():
    string = input()
    word = string.split()
    return len(word)

t = int(input("nhập vào toàn bộ"))
for i in range (1, t+1):
    result = count_word()
    print(f"test {i}: {result}")