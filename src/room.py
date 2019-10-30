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

    def __str__(self):
        return f"Room: {self.name}\nDescription: {self.description}"

    def __repr__(self):
        return f"Room name:({repr(self.name)}), description:({repr(self.description)})"
