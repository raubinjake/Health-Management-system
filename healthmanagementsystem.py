def janyread():
    """read jany data from file"""
    print("1. Deight")
    print("2. Exercise")
    j = int(input())
    if j == 1:
        f = open("janydeight.txt")
        print(f.read())
        f.close()
    else:
        f = open("janyexe.txt")
        print(f.read())
        f.close()
def lararead():
    """read lara data from file"""
    print("1. Deight")
    print("2. Exercise")
    j = int(input())
    if j == 1:
        f = open("laradeight.txt")
        print(f.read())
        f.close()
    else:
        f = open("laraexe.txt")
        print(f.read())
        f.close()

def jamesread():
    """read james data from file"""
    print("1. Deight")
    print("2. Exercise")
    j = int(input())
    if j == 1:
        f = open("jamesdeight.txt")
        print(f.read())
        f.close()
    else:
        f = open("jamesexe.txt")
        print(f.read())
        f.close()
#time and date function
def getdate():
    import datetime
    return datetime.datetime.now()

def janywrite():
    """print jany data in file"""
    print("1. Deight")
    print("2. Exercise")
    j = int(input())
    if j == 1:
        w = input("Enter about ur deight")
        f = open("janydeight.txt","a")
        f.write(str([str(getdate())])+": "+w+"\n")
        print("successfully print in file")
        f.close()
    else:
        w = input("Enter about ur Exercise")
        f = open("janyexe.txt","a")
        f.write(str([str(getdate())]))
        f.write(str(w)+"\n")
        print("successfully print in file")
        f.close()

def larawrite():
    """print lara data in file"""
    print("1. Deight")
    print("2. Exercise")
    j = int(input())
    if j == 1:
        w = input("Enter about ur deight")
        f = open("laradeight.txt","a")
        f.write(str([str(getdate())]))
        f.write(str([w])+"\n")
        print("successfully print in file")
        f.close()
    else:
        w = input("Enter about ur Exercise")
        f = open("laraexe.txt")
        f.write(str([str(getdate())]))
        f.write(str([w])+"\n")
        print("successfully print in file")
        f.close()

def jameswrite():
    """print james data in file"""
    print("1. Deight")
    print("2. Exercise")
    j = int(input())
    if j == 1:
        w = input("Enter about ur deight")
        f = open("jamesdeight.txt")
        f.write(str([str(getdate())]))
        f.write(str([w])+"\n")
        print("successfully print in file")
        f.close()
    else:
        w = input("Enter about ur Exercise")
        f = open("jamesexe.txt")
        f.write(str([str(getdate())]))
        f.write(str(w)+"\n")
        print("successfully print in file")
        f.close()

while(True):
    print("1. Retrive data from file")
    print("2. Write data into file")
    print("0. Exit")
    c = int(input())
    if c == 1:
        print("1. Jany")
        print("2. Lara")
        print("3. James")
        r = int(input())
        if r == 1:
            janyread()
        elif r == 2:
            lararead()
        elif r == 3:
            jamesread()
        else:
            print("Wrong input ! try again")
    elif c == 2:
        print("1. Jany")
        print("2. Lara")
        print("3. James")
        r = int(input())
        if r == 1:
            janywrite()
        elif r == 2:
            larawrite()
        elif r == 3:
            jameswrite()
        else:
            print("Wrong input ! try again")
    elif c == 0:
        print("Have a nice day Bye!")
        break
    else:
        print("Wrong input try again!")

