# Homogeneous List / Python Supports Hetrogeneous List other
names =["cat" , "dog" , "rat" ] 
print (names)

# Hetrogeneous List
Student =["besti","18","9.5"]
print (Student)

# Repitition Operator * To repeat data
numbers = [8,4,6,48]
new_numbers = numbers * 2
print (new_numbers)

# Positive Indexing
numbers =[5,9,7,6,4,7]
print(numbers[4])

# Negative indexing starts from -1, bez 0 is a non-negative
numbers = [4,9,8,7,3,2]
print (numbers[-3])

# lens function
numbers = [2,3,9,3,5,6]
print ("number of elements in the list:" ,len (numbers))

# Mutability (Changable)
numbers =[5,66,7,5,3,6]
numbers[0]=8

#Concatenation
List_1 = [2,7,3,5,6]
List_2 = [9,3,7,9,5]

List_3=List_1 + List_2
print (List_3)

# List slicing - to use one part of list
new_list =[10,2,13,10,5,6,7]
result= new_list [0:4]# 2nd index exclusive index - 0-3 index
print (result)

# find elements in list -if operator
new_list1 =[9,4,3,5,7,7,5,9]
if 10 in new_list1:
    print("found")
else:
    print("Not found")

# (not in)operator
new_list2 = [1,2,3,5,6,7,8,9]
if 20 not in new_list2: 
    print ("yes")
else:
    print ("No")

# built in methods - append
New_list3 = [4,5,6,7,8]
New_list3.append (9)
print (New_list3)

# built in methods - index
New_list4 = [4,5,6,6,7]
print (New_list3. index (5)) #identify index of number 5

# built in methods - sort
New_list5 = [4,8,6,3,1]
New_list5. sort ()
print(New_list5)

# built in methods - reverse
New_list6 = [4,7,5,3,8]
New_list6. reverse()
print (New_list6)

# built in methods - remove

New_list7 = [4,8,6,3,2]
New_list7. remove (6)
print (New_list7)

# min max number
print(max (New_list7))
print(min (New_list7))