def power(b,e):
    if e<=1:
        return b
    else:
        return b*power(b,e-1)
    
print(power(5,2))
