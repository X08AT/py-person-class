class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for entity in people:
        human = Person(entity["name"], entity["age"])
        person_list.append(human)

    for entity in people:
        human = Person.people[entity["name"]]
        if "wife" in entity and entity["wife"] is not None:
            human.wife = Person.people[entity["wife"]]
        if "husband" in entity and entity["husband"] is not None:
            human.husband = Person.people[entity["husband"]]

    return person_list
