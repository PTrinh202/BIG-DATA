t = int(input('Nhập số lần test: '))
if t > 0 and t <= 100:
    for i in range(t):
        print(f"test {i+1}: {input('Nhập câu: ').title()} ", end="\n")
else:
    print('Nhập sai')
