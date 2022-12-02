n = int(input(f"Nhap vao n: "))
for i in range(0, n, 1):
    str = input(f"Nhap vao chuoi {i + 1}: ")
    newStr = " ".join(str.strip().split())
    print(f"Text {i + 1}: {newStr}")