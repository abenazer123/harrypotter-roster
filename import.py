# TODO
import csv
import cs50
from sys import argv, exit

if len(argv) != 2:
    exit("ERROR: provide proper command line arguments")

open("students.db", "w")
db = cs50.SQL("sqlite:///students.db")

db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")


#accept name of CSV file as a command-line argument
with open(argv[1]) as students:

    reader = csv.DictReader(students)
    #parse name and get the first, middle, and last name

    # first = ""
    # middle = ""
    # last = ""

    for row in reader:
        fullname = row["name"]
        nameList = fullname.split(" ")

        if len(nameList) == 2:
            first = nameList[0]
            last = nameList[1]
            middle = None
        else:
            first = nameList[0]
            middle = nameList[1]
            last = nameList[2]
        house = row["house"]
        birth = row["birth"]

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)
