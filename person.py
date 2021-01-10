class Person:
    def __init__(self, name, surname, age, nationality,
                 birth_place, phone_number=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.nationality = nationality
        self.birth_place = birth_place
        self.phone_number = phone_number

    def presentation(self):
        return f"""{self.name} {self.surname}
          age: {self.age}
          nationality: {self.nationality}
          birth_place: {self.birth_place}
          phone_number: {self.phone_number}"""


class Student(Person):
    def __init__(self, institute, profession, name, surname, age,
                 nationality, birth_place, phone_number=None):
        Person.__init__(self, name, surname, age, nationality,
                        birth_place, phone_number=None)
        self.institute = institute
        self.profession = profession
        self.phone_number = phone_number

    def student_data(self):
        return self.presentation() + "\n" + f"""          institute: {self.institute}
          profession: {self.profession}"""


person1 = Person("Nara", "Avetisyan", 36, "Armenian", "Yerevan", "096178485")
print(person1.presentation())
person2 = Student("Fine Arts Academy", "Painter", "Sofia", "Russo", 30, "Italian", "USA")
print(person2.student_data())
