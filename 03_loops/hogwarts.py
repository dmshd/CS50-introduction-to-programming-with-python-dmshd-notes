def main():
    # students = ["Hermione", "Harry", "Ron", "Draco"]
    # houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
    # print(students[0])
    # print(students[1])
    # print(students[2])
    # for student in students:
    #     print(student)
    # for i in range(len(students)):
    #     print(i + 1, students[i])
    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin"
        }
    # print(students["Hermione"])
    # print(students["Harry"])
    # print(students["Ron"])
    # print(students["Draco"])

    # print('\n')

    # for student in students:
    #     print(student, students[student], sep=", ")


    students_improved = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]

    for student in students_improved:
        print(student["name"], student["house"], student["patronus"], sep=", ")


main()

