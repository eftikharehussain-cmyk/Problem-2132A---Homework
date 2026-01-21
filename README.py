# Problem-2132A---Homework
for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    m = int(input())
    b = input().strip()
    c = input().strip()
    for i in range(m):
        if c[i] == "D":
            a = a + b[i]
        if c[i] == "V":
            a = b[i] + a
    print(a)

