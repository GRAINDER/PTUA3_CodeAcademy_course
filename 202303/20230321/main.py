import sys

# greeting = f"{sys.argv[1]} {sys.argv[2]}"
# print(greeting)


# my_list = [1, 2, 3]

# for item in my_list:
#     something = item + 1
#     print(something + 1)


# write a python script that adds all the numbers entered in the command line as arguments. Throw an error if user enters something other than number



# import sys

# sum = 0

# for arg in sys.argv[1:]:
#     try:

#         sum += float(arg)
#     except ValueError:
     
#         print(f"Error: '{arg}' inserted arguments is incorrect")
#         sys.exit(1)


# # print(sum)




  
# print("This is the name of the program:", sys.argv[0])
  
# print("Argument List:", str(sys.argv[2]))




add = 0.0
  
# Getting the length of command
# line arguments
n = len(sys.argv)
  
for i in range(1, n):
    add += float(sys.argv[i])
  
print ("the sum is :", add)