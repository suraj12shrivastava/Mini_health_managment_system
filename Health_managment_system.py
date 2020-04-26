#health managment system
def getdate():
    import datetime
    return datetime.datetime.now()
def food_harry():
    f= open("harry.txt","w")
    f.write(input())
    f.close()

def food_rohan():
    f = open("rohan.txt", "w")
    a = f.write(input())
    f.close()
def food_hammad():
    f= open("hammad.txt","w")
    a = f.write(input())
    f.close()
def ex_harry():
    f = open("harry.txt.txt", "w")
    a = f.write(input())
    f.close()
def ex_rohan():
    f = open("rohan.txt", "w")
    a = f.write(input())
    f.close()
def ex_hammad():
    f= open("hammad.txt","w")
    a = f.write(input())
    f.close()
def rt_harry():
    f = open("harry.txt")
    a = f.read()
    print(getdate(),a)
    f.close()
def rt_rohan():
    f = open("rohan.txt")
    a = f.read()
    print(getdate(),a)
    f.close()
def rt_hammad():
    f = open("hammad.txt")
    a = f.read()
    print(getdate(),a)
    f.close()
def rt_harry_ex():
    f = open("harry.txt")
    a = f.read()
    print(getdate(),a)
    f.close()
def rt_rohan_ex():
    f = open("rohan.txt")
    a = f.read()
    print(getdate(),a)
    f.close()
def rt_hammad_ex():
    f = open("hammad.txt")
    a = f.read()
    print(getdate(),a)
    f.close()

print("Welcome for health managment system")
value1 = int(input("enter 1 for Lock and 2 for retrieve   : "))
if value1==1:
    value2=int(input("enter 1 for harry and 2 for rohan and 3 for hammad  : "))
    if value2==1:
        value3= int(input("enter 1 for food and 2 for excersize  : "))
        if value3==1:
            food_harry();
        elif value3==2:
            ex_harry();
    elif value2==2:
        value3= int(input("enter 1 for food and 2 for excersize  : "))
        if value3==1:
            food_rohan();
        elif value2==2:
            ex_rohan();
    elif value2==3:
        value3= int(input("enter 1 for food and 2 for excersize   : "))
        if value3==1:
            food_hammad();
        elif value3==2:
            ex_hammad();
elif value1==2:
    value2 = int(input("enter 1 for harry and 2 for rohan and 3 for hammad"))
    if value2 == 1:
        value3 = int(input("enter 1 for food and 2 for excersize"))
        if value3 == 1:
            rt_harry();
        elif value2 == 2:
            rt_harry_ex();
    elif value2 == 2:
        value3 = int(input("enter 1 for food and 2 for excersize"))
        if value3 == 1:
            rt_rohan();
        elif value2 == 2:
            rt_rohan_ex();
    elif value2 == 3:
        value3 = int(input("enter 1 for food and 2 for excersize"))
        if value3 == 1:
            rt_hammad();
        elif value3 == 2:
            rt_hammad_ex();