class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

def object_to_dict(obj):
    return vars(obj)

person = Person("Alice", 30, "USA")
dope = Person("Jacko",35,"Poland")

person_dict = object_to_dict(person)
print(person_dict)

person_dict = object_to_dict(dope)
print(person_dict)