class Calories:
    """Gives information of how much calories a person should
    consume based on age, height and weight."""

    def __init__(self, weight, height, age):
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self, temperature):
        return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * temperature.get()
