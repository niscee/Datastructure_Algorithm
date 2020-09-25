""" 
    Recursion: 0 1 1 2 3 5 8 13 using while loop
"""
# def recursion(val):
#     n1, n2 = 0, 1
#     count = 1
#     if val == 0 and val == 1:
#        print(val)
#     while count <= val:
#        print(n1, end=" ")
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1


# #start
# no = int(input("Enter:"))
# recursion(no)


def recursion(val):
    if val == 0 or val == 1:
        return val
    return recursion(val - 1) + recursion(val - 2)    

""" steps
recursion(4):
   r4 = r(3) + r(2) --- (i)
   r3 = r(2) + r(1) --- (ii)

   r2 = r(1) + r(0)
   r2 = 1

   r2 value on r3, 
   r3 = 1 + 1 = 2
   r4 = 2 + 1 = 3 
"""         

#start
no = int(input("Enter:"))
result = recursion(no)
print(result)



