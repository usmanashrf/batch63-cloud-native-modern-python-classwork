## Organizing Students and Their Grades

Imagine you are a teacher managing a classroom. You have a list of students, and for each student, you want to keep track of their grades in three different subjects: Math, Science, and English. You decide to use a nested list where each sublist represents a student, and within each sublist, you store the student’s name and their grades for the three subjects.

```
classroom = [
    ["Rehan", [85, 90, 88]],   # Rehan's grades: Math, Science, English
    ["Muzhar", [78, 85, 82]],  # Muzhar's grades: Math, Science, English
    ["Ibtisam", [92, 88, 91]], # Ibtisam's grades: Math, Science, English
    ["Usman", [60, 59, 65]]    # Usman's grades: Math, Science, English
]
```

In this nested list:

	•	The outer list represents the entire classroom, with each sublist representing a student.
	•	Each student’s sublist contains their name and another sublist of their grades in Math, Science, and English.


#### Accessing Specific Grades
***Rehan’s Science Grade:***

```
rehan_science_grade = classroom[0][1][1]
print(rehan_science_grade)  # Output: 90
```

***Usman’s English Grade:***
```
usman_english_grade = classroom[3][1][2]
print(usman_english_grade)  # Output: 65
```

#### Modifying a Student’s Grades
***Update Muzhar’s Math Grade:***
```
classroom[1][1][0] = 83
print(classroom[1])  # Output: ['Muzhar', [83, 85, 82]]
```
