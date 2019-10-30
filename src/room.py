# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''
        self.items = []

    def __str__(self):
        s = f"\n{self.name}\n{self.description}\nItems: \n"

        for i in self.items:
            s += f"{i}\n"

        return s

    def __repr__(self):
        return f"Room name:({repr(self.name)}), description:({repr(self.description)})"

    def add_room_item(self, item):
        return self.items.append(item)
