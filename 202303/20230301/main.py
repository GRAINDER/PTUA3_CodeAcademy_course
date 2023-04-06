class Names:
    """This is old friend Antanas"""

    def __init__(self, name:str, surname: str, age: int) -> None:
        self.name = name
        self._surname = surname #<- sitas kintamas self._surname = surname turi buti naudojamas tik sitos klases viduje. 
        #Nors python to nedraudzia, bet negalima printe naudoti underscore. Nerasyta taisykle, negalima prie jo is isores kisti naugu
        self.__age = age #<- private
        
        print(name)
#         print(self.name)

my_name = Names(name="Antanas", surname="Kowalski", age=22)

print(my_name.name)
print(my_name._surname) # <- sitaip negalima daryti, negalim taip rasyti kodo
print(my_name.__age) #<- private

#skirtas tarp _ ir __ 4 obejktinio programavima inheritance , uncapsulation - apsaugojimas, polimofrimas formas, overriding, abstrakcija (panasiai kaip blueprint)
# print(Antanas("Antanas"))

# self.name  yra public
# self._name  yra ne public. Jis negali buti naudojamas kaip public. Jis yra protective, (Jis gali buti naudoajas tik kalses scope)
# 
#inheritance galima kelti klase, declarinti


class Car:
    def __init__(self, make_year: int, cost: float, color: str) -> None: #Blueprintas
        self.make_year = make_year
        self.cost = cost
        self.color = color
        self.full_info = f"Full info {cost}, linero {make_year}, {color}"

    def get_car_color(self)-> None:  #instant metodai
        print(f"my car color is {self.color}")
    def get_class(self)-> float:
        return self.cost
    def get_full_info(self)-> None:
        print(f"My full info is {self.full_info}")


class Car:
    def get_car_color(self, color: str)-> None:


        #motinine klase, kuris tinkamas visoms sub klasems


    #public tai betkur bus naudojam
    #protective tik klaseje
    #super svarbu negalima accessinti tik klases viduje deti 2 score


#Polymorphism
#Inheritance

