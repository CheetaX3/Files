students = [
    {
        'name': 'John',
        'age': 20,
        'subjects': ['Math', 'Physics', 'History', 'Chemistry', 'English'],
        'grades': {'Math': 95, 'Physics': 88, 'History': 72, 'Chemistry': 84, 'English': 90}
    },
    {
        'name': 'Alice',
        'age': 19,
        'subjects': ['Biology', 'Chemistry', 'Literature', 'Math', 'Art'],
        'grades': {'Biology': 80, 'Chemistry': 92, 'Literature': 78, 'Math': 88, 'Art': 86}
    },
    {
        'name': 'Michael',
        'age': 22,
        'subjects': ['Computer Science', 'English', 'Art', 'History', 'Economics'],
        'grades': {'Computer Science': 87, 'English': 78, 'Art': 90, 'History': 82, 'Economics': 75}
    },
    {
        'name': 'Sophia',
        'age': 18,
        'subjects': ['Geography', 'Economics', 'Music', 'Physics', 'Biology'],
        'grades': {'Geography': 92, 'Economics': 85, 'Music': 95, 'Physics': 88, 'Biology': 90}
    },
    {
        'name': 'Robert',
        'age': 21,
        'subjects': ['Chemistry', 'Biology', 'Physics', 'Literature', 'Math'],
        'grades': {'Chemistry': 76, 'Biology': 85, 'Physics': 90, 'Literature': 78, 'Math': 82}
    },
    {
        'name': 'Emma',
        'age': 20,
        'subjects': ['History', 'Chemistry', 'Music', 'Biology', 'Computer Science'],
        'grades': {'History': 85, 'Chemistry': 88, 'Music': 92, 'Biology': 78, 'Computer Science': 84}
    },
    {
        'name': 'William',
        'age': 19,
        'subjects': ['Math', 'English', 'Geography', 'Chemistry', 'Economics'],
        'grades': {'Math': 90, 'English': 85, 'Geography': 80, 'Chemistry': 92, 'Economics': 78}
    },
    {
        'name': 'Olivia',
        'age': 22,
        'subjects': ['Art', 'History', 'Computer Science', 'Physics', 'Math'],
        'grades': {'Art': 88, 'History': 82, 'Computer Science': 90, 'Physics': 85, 'Math': 80}
    },
    {
        'name': 'James',
        'age': 20,
        'subjects': ['Chemistry', 'English', 'Biology', 'Geography', 'Economics'],
        'grades': {'Chemistry': 78, 'English': 85, 'Biology': 92, 'Geography': 90, 'Economics': 84}
    },
    {
        'name': 'Ava',
        'age': 18,
        'subjects': ['Music', 'Art', 'History', 'Biology', 'Chemistry'],
        'grades': {'Music': 95, 'Art': 90, 'History': 82, 'Biology': 88, 'Chemistry': 80}
    },
    {
        'name': 'Alexander',
        'age': 19,
        'subjects': ['Computer Science', 'Economics', 'English', 'Geography', 'History'],
        'grades': {'Computer Science': 82, 'Economics': 88, 'English': 80, 'Geography': 85, 'History': 90}
    },
    {
        'name': 'Mia',
        'age': 21,
        'subjects': ['Physics', 'Math', 'Biology', 'English', 'Chemistry'],
        'grades': {'Physics': 90, 'Math': 85, 'Biology': 88, 'English': 78, 'Chemistry': 82}
    },
    {
        'name': 'Ethan',
        'age': 18,
        'subjects': ['Chemistry', 'Biology', 'Art', 'Music', 'Geography'],
        'grades': {'Chemistry': 84, 'Biology': 80, 'Art': 92, 'Music': 85, 'Geography': 78}
    },
    {
        'name': 'Charlotte',
        'age': 20,
        'subjects': ['Computer Science', 'Economics', 'History', 'Math', 'Physics'],
        'grades': {'Computer Science': 88, 'Economics': 82, 'History': 90, 'Math': 78, 'Physics': 85}
    },
    {
        'name': 'Jacob',
        'age': 19,
        'subjects': ['English', 'Chemistry', 'Biology', 'Geography', 'History'],
        'grades': {'English': 82, 'Chemistry': 90, 'Biology': 78, 'Geography': 88, 'History': 85}
    },
    {
        'name': 'Liam',
        'age': 21,
        'subjects': ['Art', 'Music', 'History', 'Computer Science', 'Physics'],
        'grades': {'Art': 85, 'Music': 78, 'History': 90, 'Computer Science': 82, 'Physics': 88}
    }
]

# Задание 1
for i in students:
    student_grades =i['grades'].values()
    print(f'Средний балл для студента {i['name']}: ', end = '')
    print(sum(student_grades) / len(student_grades))


# Задание 2
name = input('Enter the student name: ').capitalize()
n = 0
for i in students:
    if i['name'] == name:
        print(
            f'Name: {i['name']}', f'Age: {i['age']}',
            f'Subjects: {i['subjects']}', f'Grades: {i['grades']}',
            sep = '\n'
        )
        n += 1
if n == 0:
    print ('The student with that name was not found.')


# # Задание 3
best_st = ''
best_aver = 0
worst_st = ''
worst_aver = 101

for i in students:
    student_grades = list(i['grades'].values())
    aver = sum(student_grades) / len(student_grades)
    if aver > best_aver:
        best_st = i['name']
        best_aver = aver
    if aver < worst_aver:
        worst_st = i['name']
        worst_aver = aver

print(f'The best student: {best_st} (Average score: {best_aver})')
print(f'The worst student: {worst_st} (Average score: {worst_aver})')