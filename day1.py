#SUBSCRIPTING
# print("abcdef"[0:6])
# print("abcdef"[5])
# print("abcdef"[-1])
# print("abcdef"[0:5])
# print("abcdef"[0:5:1])
# print("abcdef"[0:5:2])


#STRING
#or way-first declare an variable or take it as user input
# var1="String"
# var2=input()
# # var2=input(3) # for this statement data type is str, its value always start with 3. Only interger are allowed to use in (), it will give error if eneter other, eg- var2=input(hh) or var2=input("gg")
# # var2=input("hh") #always starts with hh, data type will be str.
# # var2=int(input(3)) # for this statement data type is int, its valau always start with 3, it will give error if user enter other than integer.
# # print(type(var2))

# print("var1:",var1)
# print("var2:",var2) # or print(f"{var1}"var1)
# print(f"var1:{var1}\nvar2:{var2}")
# print(type(var1))
# print(type(var2))


# #INTEGER = WHOLE NUMBERS
# print(233+100)

# '''LARGE INTEGERS- 
# when we write large number then wr use commas eg. 126,758 or 23,456
# In python we enter any alrge number then internally python take it as seperated by underscors.
# eg- we do this-print(7484659), but oyhton takes it as 7_484_659'''
# print(234_457_678) # same as print(234457678)

#FLOAT = FLOATING POINT NUMBER
# print(3.455)

# # BOOLEAN
# print(True)
# print(False)

#The App Brewery

# var=567890
# len(var) # will give type eror
# #OR
# len(2345) #it will give error because len fucntion does not take integer as arugment.

# #Type check in python : type fucntion takes only one arugment at a time
# print(type("String")) #string
# print(type(2)) #integer
# print(type(76.456)) #float
# print(type(True)) #boolean
# print(type([1,2,3,4,4])) #list
# print(type([1,'233',3,'string','yh5'])) #list
# print(type({"key1":1,"key2":4})) #dict
# print(type((2,2,56,7))) #tuple
# print(type((3,4,5,6,'hgh','dhf7h788',"dhdud",34,"fhf788"))) #tuple

# print(type("tss",67)) #it will give type error

# print((6,'yyh',8.9,7.99,'hfy77',"7u8u8i","67890"))
# print([6,'yyh',8.9,7.99,'hfy77',"7u8u8i","67890"])


# # TYPE CASTING
# # 1. Converting string to integer use- int
# print(type(int('123')))
# var1=int("4678")
# var2=int('3959')
# var3=int(3455) #it makes no sense as the number is already integer
# print(type(var1)) #int
# print(type(var2)) #int

# print(int("30")+int("60")) #90

# # 2. Converting int to string use- str
# # Using the str() Function (Most Common)
# var1 = str("2345") #it makes no sense as "2345" is already string
# var2 = str(684)
# print(type(var1))
# print(type(var2))

# # Using f-strings (Modern & Readable)
# num = 123
# formatted_str = f"{num}"
# print(formatted_str)  # Output: "123"
# #OR
# num2=f"{12345}"
# print(type(num2))

# # Using the .format() Method
# num = 456
# formatted_str = "Value: {}".format(num)
# print(type(formatted_str))


# # 3. Converting float to string, float to int
# num=23.99
# numint=str(int(num))
# print(numint)
# print(type(numint))

# # 4. Converting int to bool
# var = 123456 #or var = 0 for False
# varbool=bool(var)
# print(varbool)
# print(type(varbool))

# # 5. Converting str to bool
# var = "yhdimg" # or var = ""/'' for False
# varbool=bool(var)
# print(varbool)
# print(type(varbool))

# #Solution to problem asked in video
# #print("Number of letters in your name: "+len(input("Enter your name")))
# print("Number of letters in your name: ",len(input("Enter your name: ")))
# #OR
# print("Number of letters in your name: "+ str(len(input("Enter your name: "))))
# #OR
# length=len(input("Enter your name: "))
# print("Number of letters in your name: "+str(length))

print("String"+str(12))
print(234+24)
print(7-3)
print(5/3)
print(5*3)
print(5**3)
print(6//5)
print(type(6/3))
print(type(6/5))
print(type(6//5))