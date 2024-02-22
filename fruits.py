class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        return f"Ці {self.color} {self.name} смачні"

class Apple(Fruit):
    def __init__(self):
        super().__init__(name='яблука', color='червоні')

class Banana(Fruit):
    def __init__(self):
        super().__init__(name='банани', color='жовті')

class Blueberry(Fruit):
    def __init__(self):
        super().__init__(name='ягоди', color='сині')

apple = Apple()
banana = Banana()
blueberry = Blueberry()

print(apple.describe())
print(banana.describe())
print(blueberry.describe())