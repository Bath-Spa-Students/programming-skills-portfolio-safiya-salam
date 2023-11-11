#Write a python program with nested decision structures that perform the following: 
#If amount1 is greater than 10 and amount2 is less than 100, 
#display the greater of amount1 and amount2

# Get user input for amount1 and amount2
amount1 = int(input("Enter the value for amount1: "))
amount2 = int(input("Enter the value for amount2: "))

# Check if amount1 is greater than 10 and amount2 is less than 100
if amount1 > 10:
    if amount2 < 100:
        # Display the greater of amount1 and amount2
        if amount1 > amount2:
            print("amount1 is greater than amount2: ", amount1)
        elif amount2 > amount1:
            print("amount2 is greater than amount1: ", amount2)
        else:
            print("amount1 and amount2 are equal: ", amount1 , amount2)
    else:
        print("amount2 is not less than 100.")
else:
    print("amount1 is not greater than 10.")
