class Grade:
    def __init__(self, weight, value) -> None:
        self.weight = weight
        self.value = value
    
    def calculate(self, weight, value):
        self.note = weight * value
    
    def add_lecture(self):
        pass