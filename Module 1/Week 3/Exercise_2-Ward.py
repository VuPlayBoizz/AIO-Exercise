class Student():
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(
            f"Student Name: {self.name} - Year of Birth: {self.yob} - Grade: {self.grade}")


class Doctor():
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor Name: {self.name} - Year of Birth: {self.yob} - Specialist: {self.specialist}")


class Teacher():
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f"Teacher Name: {self.name} - Year of Birth: {self.yob} - Subject: {self.subject}")


class Ward():
    def __init__(self, name):
        self.name = name
        self.person = []

    def add_person(self, person):
        self.person.append(person)

    def describe(self):
        print(f"Ward name: {self.name}")
        for person in self.person:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.person if isinstance(person, Doctor))

    def sort_age(self):
        self.person.sort(key=lambda x: x.yob, reverse=True)

    def compute_average(self):
        result = []
        for person in self.person:
            if isinstance(person, Teacher):
                result.append(person.yob)
        return sum(result) / len(result)


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()


print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()


print(f"\nNumber of doctors: {ward1.count_doctor()}")


print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()


print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
