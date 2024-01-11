import process

# Main def for first main menu
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
    print("Goodbye!")
    exit()

def viewdata():
    print("Please enter one of the following options:")
    print("     [A] View Reviews by Park")
    print("     [B] Number of Reviews by Park and Reviewer Location")
    print("     [C] Average Score per year by Park")
    print("     [D] Average Score epr Park by Reviewer Location")
    enter = ""

    while enter != "A" or "B" or "C" or "D":
        enter = input().upper()
        if enter == "A":
            parktype()
        if enter == "B":
            numberR()
        if enter == "C":
            PandY()
        if enter == "D":
            print("test")

def parktype():
    print("What park would you like to see the reviews for?")
    enter=input()
    process.parkr(enter)

def visualise():
    print("Please enter one of the following options:")
    print("     [A] Most Reviewed Parks")
    print("     [B] Average Scores")
    print("     [C] Park Ranking by Nationality")
    print("     [D] Most Popular Month by Park")#
    enter = ""

