# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __int__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Room: {self.name}, Description: {self.description}"

    def __repr__(self):
        return f"Room name:({repr(self.name)}), description:({repr(self.description)})"
