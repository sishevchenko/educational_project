"""Разработать функцию sweetest_icecream, которая принимается список инстанций класса IceCream и возвращает "уровень
сладости" самого сладкого мороженого.

"Уровень сладости" складывается из ароматизатора и количества посыпок. Сладость одной посыпки = 1, а сладость
ароматизаторов считается по таблице:

Plain = 0
Vanilla = 5
ChocolateChip = 5
Strawberry = 10
Chocolate = 10

В функцию будут передаваться два аргумента: ароматизатор (как строка) и кол-во посыпок.

Примеры

ice1 = IceCream("Chocolate", 13)         # 10 + 13 = 23
ice2 = IceCream("Vanillla", 0)           # 5 + 0 = 5
ice3 = IceCream("Strawberry", 7)         # 10 + 7 = 17
ice4 = IceCream("Plain", 18)             # 0 + 18 = 18
ice5 = IceCream("ChocolateChip", 3)      # 5 + 3 = 8

sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23
sweetest_icecream([ice3, ice1]) ➞ 23
sweetest_icecream([ice3, ice5]) ➞ 17"""


class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles


def sweetest_icecream(lst):
    d = {
        'Plain': 0,
        'Vanilla': 5,
        'ChocolateChip': 5,
        'Strawberry': 10,
        'Chocolate': 10
    }
    res = []
    for icecream in lst:
        res.append(d[icecream.flavor] + icecream.sprinkles)
    return max(res)
