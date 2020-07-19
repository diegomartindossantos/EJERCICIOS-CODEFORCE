x=0
n=int(input())
for _ in range(n):
    operacion = input()
    if "++" in operacion:
        x += 1
    else:
        x -= 1
print (x)
        

