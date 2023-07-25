from typing import List


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __str__(self):
        return "Cake kind: {}, name: {} and additives: {}".format(self.kind, self.name, self.additives)

    def __iadd__(self, other):
        if isinstance(other, str):
            self.additives.append(other)
            return self
        elif isinstance(other, list):
            self.additives.extend(other)
            return self
        else:
            raise Exception


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
print(cake01)
cake01 += "banana"
print(cake01)
cake01 += ["toffee", "coffee"]
print(cake01)
cake01 += 123
