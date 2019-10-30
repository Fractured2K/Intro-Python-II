class Item:
    def __init__(self, name, description):
        self.name = name
        self.description: name

    def __str__(self):
        return f"{self.name}\n{self.description}"

    def __repr__(self):
        return f"Item name:({repr(self.name)}), description:({repr(self.description)})"

    def item_name(self):
        return {self.name}
