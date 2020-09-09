import csv
import cs50
from sys import argv, exit

if len(argv) != 2:
    exit("ERROR: provide proper command line arguments")

db = cs50.SQL("sqlite:///students.db")

roster = db.execute(f"SELECT * FROM students WHERE house = (?)", argv[1])

newros = []
for row in roster:

    firstName = row["first"]
    if row["middle"] != None:
        middleName = row["middle"]
    fake["lastName"] = row["last"]
    fake["house"] = argv
    fake["birth"] = row["birth"]
    newros.append(fake)
print(newros)
