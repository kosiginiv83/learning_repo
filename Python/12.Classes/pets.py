"""
Необходимо реализовать классы животных на ферме:
Коровы, козы, овцы, свиньи;
Утки, куры, гуси.
Условия:
Должен быть один базовый класс, который наследуют все остальные животные.
Базовый класс должен определять общие характеристики и интерфейс.
"""


class Pets:
    quantity = 0
    drink = 'water'
    
    def __init__(self, name):
        self.name = name
    
    def __new__(cls, name):
        cls.quantity += 1
        #Pets.quantity += 1
        return super().__new__(cls)
    
    def voice(self):
        print('breethe')
    
    def eating(self):
        print('Om nom nom')


class Birds(Pets):
    wings = True
    give_eggs = True
    legs = 2
    
    def eating(self):
        print(self, 'Pecking')


class Animals(Pets):
    legs = 4
    give_milk = True
    
    def eating(self):
        print(self, 'Chewing')


class Ducks(Birds):
    def voice(self):
        print('quack')


class Goats(Animals):
    def voice(self):
        print('bleat')


class Hens(Birds):
    def voice(self):
        print('cluck')


class Geese(Birds):
    def voice(self):
        print('gaggle')


class Sheeps(Animals):
    def voice(self):
        print('bleat')


class Pigs(Animals):
    give_milk = False
    
    def voice(self):
        print('grunt')


pig0 = Pigs("NafNaf")
print('pig0.__dict__', pig0.__dict__)
print('Pigs.quantity', Pigs.quantity)
print('Ducks.quantity', Ducks.quantity)
print('pig0.give_milk', pig0.give_milk)
print('pig0.name', pig0.name)
pig0.eating()
pig0.voice()
print('\n')

hens0 = Hens("Ryaba")
hens1 = Hens("Ptica")
print('hens0.name', hens0.name)
print('hens1.name', hens1.name)
print('hens0.drink', hens0.drink)
print('hens0.legs', hens0.legs)
print('hens0.wings', hens0.wings)
hens0.eating()
hens0.voice()
print('Hens.quantity', Hens.quantity)