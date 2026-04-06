class Person:
    people = {}

    def __init__(
        self,
        name: str,
        age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for i in people:
        person = Person(i["name"], i["age"])
        person_list.append(person)

    for i, person in zip(people, person_list):
        wife_name = i.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = i.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return person_list
