students = int(input())
failingStudents = 0.0
averageStudents = 0.0
goodStudents = 0.0
excellentStudents = 0.0
averageGrade = 0.0

for i in range(1, students+1):
    grade = float(input())

    if 2.00 <= grade <= 2.99:
        failingStudents += 1
        averageGrade += grade

    if 3.00 <= grade <= 3.99:
        averageStudents += 1
        averageGrade += grade

    if 4.00 <= grade <= 4.99:
        goodStudents += 1
        averageGrade += grade

    if grade >= 5.00:
        excellentStudents += 1
        averageGrade += grade

print("Top students: {:.2f}%".format(excellentStudents/students * 100))
print("Between 4.00 and 4.99: {:.2f}%".format(goodStudents/students * 100))
print("Between 3.00 and 3.99: {:.2f}%".format(averageStudents/students * 100))
print("Fail: {:.2f}%".format(failingStudents/students * 100))
print("Average: {:.2f}".format(averageGrade/students))
