l = 0
x = 1
y = 0
z = 0

def factorial(l, x, y, z):
    print("da n8umber so far are", l, "and", x)
    vryg = l + x
    print("the fibonacci number is now", vryg)
    l = x
    x = vryg
    z += 1
    
    if (z<y):
        factorial(l,x,y,z)


print("how long do you want your sequence to go to")
y = int(input())
factorial(l, x , y, z)
