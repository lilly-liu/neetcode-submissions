class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married

class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool:
        ...

class AdultFilter(PersonFilter):
    # Implement Adult filter
    def apply(self, person: Person):
        if person.age >= 18:
            return 1
        else:
            return 0



class SeniorFilter(PersonFilter):
    # Implement Senior filter
    def apply(self, person: Person):
        if person.age >= 65:
            return 1
        else:
            return 0

class MarriedFilter(PersonFilter):
    # Implement Married filter
    def apply(self, person: Person):
        if person.married:
            return 1
        else:
            return 0

class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        # Implement method here
        return sum([self.filter.apply(p) for p in people])
    
