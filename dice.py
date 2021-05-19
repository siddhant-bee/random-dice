import random 
def ran():
    n = random.randint(1,6)
    return n
print("Roll your dice ->")
x="y"

while x == "y":
    n=ran()
    if(n==1):

        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")
    elif(n==2):
        print("-----------")
        print("|         |")
        print("|  0  0   |")
        print("|         |")
        print("-----------")
    elif(n==3):
        print("-----------")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("-----------")    
    elif(n==4):
        print("-----------")
        print("|  0   0  |")
        print("|         |")
        print("|  0   0  |")
        print("-----------")
    elif(n==5):
        print("-----------")
        print("|  0   0  |")
        print("|    0    |")
        print("|  0   0  |")
        print("-----------")    
    else:
        print("-----------")
        print("|  0   0  |")
        print("|  0   0  |")
        print("|  0   0  |")
        print("-----------")

    x=input("want to roll again press y :")


