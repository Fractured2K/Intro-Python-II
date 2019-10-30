class Item:
    def __init__(self, name, description):
        self.name = name
        self.description: name

    def __str__(self):
        return f"{self.name}\n{self.description}"
