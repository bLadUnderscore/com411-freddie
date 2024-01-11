import csv

def parkr(park):
    with open("files/disneyland_reviews.csv", "r") as reviews:
        csv_reader = csv.reader(reviews)
        headings = next(csv_reader)
        for row in csv_reader:
            if any(park.lower() in column.lower() for column in row):
                print(headings)
                print(row)