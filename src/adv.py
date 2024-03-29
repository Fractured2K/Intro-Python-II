from room import Room
from player import Player
from helpers import (
    clear_screen,
    move_direction
)

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms
room["foyer"].add_room_item(["Book", "Map"])
room["overlook"].add_room_item(["Flare", "Stick", "Parachute"])
room["narrow"].add_room_item(["Lead"])

clear_screen()
player_name = input("Enter player name: ")
current_room = room['outside']
clear_screen()

# Create new player
player = Player(player_name, current_room)
print(f"Welcome {player_name}!")

while True:
    # Prints the current room name and description.
    print(player.current_room)

    # Waits for user input and decides what to do.
    userInput = input().lower()

    # If the user enters "q", quit the game.
    if userInput == "q":
        print("Qutting game...")
        exit()

    # If the user enters a cardinal direction, attempt to move to the room there.
    if userInput == "n" or userInput == "s" or userInput == "e" or userInput == "w":
        move_direction(userInput, player)
    else:
        # Print an error message if the movement isn't allowed.
        print("Please enter a valid cardinal direction")
