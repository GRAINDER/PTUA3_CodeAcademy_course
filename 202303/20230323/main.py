class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.__age = age

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self.__age


class Antanas(Person):
    pass


me = Antanas(name="Paulius", age=35)


print(me.get_name())
print(me.get_age())
