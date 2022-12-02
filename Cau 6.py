def thay_the(s1, s2, s3):
    print(s1.replace(s2, s3))


t = int(input("nhập vào so lan thuc hien: "))
if 0 < t <= 100:
    for i in range(t):
        s1 = input("nhap chuoi: ")
        s2 = input("nhap chuoi thay the cu: ")
        s3 = input("nhap chuoi thay the mơi: ")
        print(f"test {i + 1}:", end="\n")
        thay_the(s1, s2, s3)