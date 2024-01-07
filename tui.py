import tui

def menu():
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("     [A] View Data")
    print("     [B] Visualise Data")
    print("     [X] Exit")
    enter = ""

    while enter != "X":
        enter = input().upper()
        if enter == "A":
            viewdata()
        elif enter == "B":
            visualise()
        else:
            print("Error, Please ")
