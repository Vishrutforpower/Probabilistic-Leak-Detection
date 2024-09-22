n = int(input("Enter a number: "))
b = True
for i in range(2, n):
    if n % i == 0:
        b = False
print(str(b))