import time
import tui


def fpage():
    file = open("files/disneyland_reviews.csv")

    width = 26
    print("-" * width)
    print("Disneyland Review Analyser")
    print("-" * width)

    print("Reading Database...")
    time.sleep(2)
    print("Database Read Successfully!")
    row_count = sum(1 for row in file) - 1
    file.close()
    print("There are", row_count, "reviews available")


fpage()
tui.menu()
