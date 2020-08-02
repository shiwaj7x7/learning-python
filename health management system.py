# clients=["shivanshu","nalin","ramish"]
def getdate():
    import datetime
    return datetime.datetime.now()
client= str(input("name of the client:"))
if client=="shivanshu":
    detail=int(input("type 1 for diet or 2 for exercises prescribed:"))
    if detail==1:
        print(getdate())
        with open("shivanshudiet.txt") as f:
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline())
    if detail==2:
        print(getdate())
        with open("shivanshuexercises.txt") as f:
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline())
if client=="ramish":
    detail=int(input("type 1 for diet or 2 for exercises prescribed:"))
    if detail==1:
        print(getdate())
        with open("ramishdiet.txt") as f:
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline())
    if detail==2:
        print(getdate())
        with open("ramishexercises.txt") as f:
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline())
if client=="nalin":
    detail=int(input("type 1 for diet or 2 for exercises prescribed:"))
    if detail==1:
        print(getdate())
        with open("nalindiet.txt") as f:
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline())
    if detail==2:
        print(getdate())
        with open("nalinexercises.txt") as f:
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline(), end="")
            print(f.readline())



