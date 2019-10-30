import os


def move_direction(direction, player):
    room = ''

    if direction == "n":
        room = player.current_room.n_to
    elif direction == "s":
        room = player.current_room.s_to
    elif direction == "e":
        room = player.current_room.e_to
    else:
        room = player.current_room.w_to

    if room != "":
        player.current_room = room
    else:
        print("No rooms that way!")


def clear_screen():
    os.system('cls' if os.name == 'clear' else "clear")
