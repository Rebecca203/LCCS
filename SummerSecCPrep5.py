fName = input("enter a first name ")
sName = input("Enter a Surname ")


while True:
    fName = input("enter a first name ")
    sName = input("Enter a Surname ") 
    print("runninbg while loop")
    check=input("Do you want the loop to continue? Y/N ")
    if check in ("Y","y"):
        print("continuing loop")
    else:
        break