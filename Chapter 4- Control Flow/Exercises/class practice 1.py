# if-else statment    
print("# if-else statment :")
price = float (input ("Enter price :"))
discount = 0
if price > 50 :
    discount = 25
else:
    discount = 0
print("Your discount: "+str( discount),"\n")

# Nested Desicion structure
print("# Nested Desicion structure :")
x = 10
y = 20

if x == 10:
    if y == 20:
        print("x is 10 and y is 20","\n")
    else:
        print("x is 10 but y is not 20","\n")
else:
    print("x is not 10","\n")

# if-elif-else statment
print("# if-elif-else statment :")
x = float (input ("Enter your number "))

if x > 10:
    print("x is greater than 10","\n")
elif x > 15:
    print("x is greater than 15","\n")
elif x > 18:
    print("x is greater than 18","\n")
else:
    print("x is smaller than or equal to 10","\n")
