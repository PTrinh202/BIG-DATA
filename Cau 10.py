print('Nhập số lượng câu: ')
t = int(input())
if 0 < t <= 100:
    for i in range(1, t + 1):
        print('Nhập câu: ')
        str = input()
        list_ten = str.split()
        tenchuanhoa=''
        for a in list_ten:
            if a != '':
                tenchuanhoa += a + ' '
        print(tenchuanhoa.title())