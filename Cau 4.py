#｡ﾟ(TヮT)ﾟ｡
#(´Д｀)
#╮ (. ❛ _ ❛.) ╭
n = int(input(f"Nhập số lần: "))
for i in range(0, n, 1):
    str = input(f"Nhập chuỗi {i + 1}: ")
    newStr = " ".join(str.strip().split())
    print(f"Text {i + 1}: {newStr}")