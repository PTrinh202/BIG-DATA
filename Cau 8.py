def dem_tu(s1):
    str = s1.split(" ")
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
#hàm sorted(dict, key=dict.get, reverse=False) sẽ trả về một list các giá trị đã được sắp xếp
    for i in sorted(count, key=count.get, reverse=False):
        print(f"{i}-{count[i]}")

t = int(input("nhập số lân: "))
if 0 < t <= 100:
    for i in range(t):
        s1 = input("nhap chuoi: ")
        print(f"test {i + 1}:", end="\n")
        dem_tu(s1)