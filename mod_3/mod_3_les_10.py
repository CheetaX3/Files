# полиморфизм
class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def get_absolute_url(self):
        return f'https://ivashev-edu.com/courses/{self.title}'

class StudentProfile:
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email

    def get_absolute_url(self):
        return f'https://ivashev-edu.com/profiles/{self.full_name}'

courses = ['python', 'django', 'javascript']

for course in courses:
    course = Course(course, 3)
    print(course.get_absolute_url())


profiles = ['Ivan_Ivanov', 'Petr_Petrov']

for profile in profiles:
    profile = StudentProfile(profile, f'{profile}@gmail.com')
    print(profile.get_absolute_url())