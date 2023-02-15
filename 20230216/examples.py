n = int(input())

my_list =[]

for i in range(n):

    num = int(input())

    my_list.append(num)

def IsListEven(my_list):

    for i in range(len(my_list)):

        if my_list[i] % 2 == 0:

            return True

        else:

            return False

def IsListOdd(my_list):

    for i in range(len(my_list)):

        if my_list[i] % 2 == 1:

            return True

        else:

            return False

def GetUserValues():

    if IsListOdd(my_list) == True:

        print("all odd")

    elif IsListEven(my_list) == True:

        print("all Even")

    else:

        print("not even or odd")