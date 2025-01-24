# The below mentioned is not correct way to perform arithmetic operation
#  because there may be a chance of typing wrong digits and also time consuming 
# so, to overcome this we use variables here we assign the values to a variable 
# so, that we can use the Variables instead of entering the no's.
# Arthimetic Operations
print(1234+5678)
print(1234-5678)
print(1234*5678)
print(1234/5678)
#Using Variables
# * Used To Refer a Memory Block

num1=100
num2=20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)
print(num1//num2)
print(num1 % num2)

# Strings -- Sequence Of Characters.
# Space is also Character 
#we will denote in 'Single_Qoute' and "Double_Qoutes".
#examples
A='str'
#print(A) # Here it will throw an Error NameError: name 'A' is not defined because it is "Case-Sensitive"
print(A) # The output will be -- str
# To know the type of the Variable we use type
print(type(A))
# To know the Length of the Variable we use len
print(len(A))

#Slicing
a="python classes are going_on"
print(a[5])  
#Index it will denote in [Square Brackets]
print(a[2 : 9]) 
# in place of index valu 9 it will give the 8 value because it will consider upper boundary -1
print(a[-3]) 
# -ve indexing from last it will show the output in this case the o/p will be "a"
print(a[1 : 21 : 2])
# the last digit 2 defines that from the range 1 to 11 it has to skip 1 letter ex the o/p will be a aeN
print(a[-2 : -21 : -1]) 
# in -ve indexing o/p will be in reverse

# If u want to change any Character in a string we can use a[5]="g" in other lang. like c,c++ it is possible
# In Python change of character is not posible because of its "Immutable Property" 
# It is possible when u want to replace or change the Entire string because it will store in different memory addres
# To know the Memory Address of a Var 
var = "rajender_veesam"
var = "rajender_veesam"
print(id(var))  # same ip address will be printed because it will refer to same memory block due same value
var_2 ="radiographer"
print(id(var_2))  #store in different memory location 

goodmorning='veesam rajender'
print(len(goodmorning))
print(goodmorning[0])
print(goodmorning[1])
print(goodmorning[2])
print(goodmorning[14])
print(goodmorning[:5])
print(goodmorning[5:])
print(goodmorning[5:11])

# Complex Numbers  
x = 2+5j
y = 4+2j
print(type(x))
print(x+y) #using Arithmetic Operations
print(x-y)
print(x*y)
print(x/y)
print(x**y)
#print(x // y)
#print(x % y)

# Boolean  - true or false
print(32.5 > 32)
print(76 <= 76)
print(95 < 58)
 # To know the integer value of true or false
print(int(False))
print(int(True))
atm_pin=9876
print(atm_pin==9876)
print(atm_pin==9875)
#list is set of data elements
#list syntax []
#lists - It is Muttable we can the item or elements present in the list and denoted in [Square brackets with ,]
new_list=[2,3,4,5,6,"lists",False,[9,"int",5]]
print(new_list)
print(type(new_list))
print(len(new_list))
print(new_list[4])
print(new_list[-6])
print(new_list[2 : 5 : 1])
# To access the list of the sublist
print(new_list[7][2])
print(new_list[7][2]) =="float"  # here we can the value of int to float so, it is Muttable
print(new_list[-2 : -6])
print(len(new_list[7]))  # It gives the length of the False

# Tuple  - It is Immutable we can't change the elements
tup1 = (9,8,7,6,[2,5,8],"Tuple")
print(type(tup1))
print(len(tup1))
#tup1[-3] = "hello" # Immutable we cant change elements one's assgined in variable
print(type[1 : 4])
print(tup1[2:6:1])
print(tup1[-1:-5:-2]) 