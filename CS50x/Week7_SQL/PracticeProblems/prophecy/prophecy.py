import csv
from cs50 import SQL

def main():
    db = SQL("sqlite:///roster.db")
    house_id = 0

    with open("students.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            id = {"id": int(row["id"])}
            student = row["student_name"]
            house = {"house_name": row["house"]}
            head = row["head"]

            ids = db.execute("SELECT id FROM students")
            if id not in ids:
                db.execute("INSERT INTO students(id, student_name) VALUES(%s, %s)", id["id"], student)

            houses = db.execute("SELECT house_name FROM houses")
            if house not in houses:
                house_id = house_id + 1
                db.execute("INSERT INTO houses(id, house_name, head) VALUES(%s, %s, %s)", house_id, house["house_name"], head)

            stu_id = {"student_id": id["id"]}
            asgn = db.execute("SELECT student_id FROM assignments")
            if stu_id not in asgn:
                hou_id = db.execute("SELECT id FROM houses WHERE house_name = %s", house["house_name"])
                db.execute("INSERT INTO assignments(student_id, house_id) VALUES(%s, %s)", stu_id["student_id"], hou_id[0]["id"])


main()