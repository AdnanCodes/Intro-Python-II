from room import Room
from player import Player
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Adnan", room['outside'])

# Write a loop that:


def adventure_game():
    print("Welcome to the Adventure Game")
    print(f"Welcome {player}!")
    print(f"{player} is {player.current_room}")

# Now player wants to go North Door\n what's the syntax

    while True:
        command = input("Enter commands --> n, e, s, w OR q to quit: ")

        if command == 'n':
            print(f"\nYou have entered {command!r}\n")
        else:
            print("\n\nPlease select the correct input\n\n")

        if command == ('n' or 'e' or 's' or 'w' or 'q'):
            print("Lets go to the North Door\n")
            if player.current_room.n_to == None:
                print(
                    f"Oops, there is no Door here, {player} will remain in {player.current_room}")
            else:
                player.current_room = player.current_room.n_to
                print("Going through the Door\n")
                print(f"{player}'s room is {player.current_room}")

        if command == 's':
            print("Lets go to the South Door\n")
            if player.current_room.s_to == None:
                print(
                    f"Oops, there is no Door here, {player} will remain in {player.current_room}")
            else:
                player.current_room = player.current_room.s_to
                print("Going through the Door\n")
                print(f"{player}'s room is {player.current_room}")
        if command == 'e':
            print("Lets go to the East Door\n")
            if player.current_room.e_to == None:
                print(
                    f"Oops, there is no Door here, {player} will remain in {player.current_room}")
            else:
                player.current_room = player.current_room.e_to
                print("Going through the Door\n")
                print(f"{player}'s room is {player.current_room}")

        if command == 'w':
            print("Lets go to the West Door\n")
            if player.current_room.w_to == None:
                print(
                    f"Oops, there is no Door here, {player} will remain in {player.current_room}")
            else:
                player.current_room = player.current_room.w_to
                print("Going through the Door\n")
                print(f"{player}'s room is {player.current_room}")
        elif command == 'q':
            print("Exiting game")
            break


if __name__ == '__main__':
    adventure_game()

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
