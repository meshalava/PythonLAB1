n = int(input("Введить довжину сторони квадратного масиву:"))
print("Введіть єлементи масиву:")
s = input()
s = s.split()
matrix = []
l=len(s)
if(l!=n*n):
    print("Введено невірну кількість єлементів масиву")
else:
    i = 0
    while i < n*n:
        print(s[i: i + n])
        matrix.append(s[i: i + n])
        i += n
    k = 0
    for i in range(n-1):
        for j in range(n-1):
            if matrix[i][j] != matrix[n-j-1][n-i-1]:
                k = k + 1
    if k == 0:
        print("Масив симетричний відносно не головної діагоналі")
    else:
        print("Масив не симетричний відносно не головної діагоналі")
