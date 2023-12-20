class Car:
    def __init__(self, model, color, weight, high_speed):
        self.model = model
        self.color = color
        self.weight = weight
        self.high_speed = high_speed
    def getModel(self):
        return f"{self.model}"
    def getColor(self):
        return f"{self.color}"
    def getWeight(self):
        return f"{self.color}"
    def getHighSpeed(self):
        return f"{self.high_speed}"
        