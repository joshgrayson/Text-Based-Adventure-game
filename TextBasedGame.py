#Joshua Grayson

def show_instructions():
   #print a main menu and the commands
  print("Snake Text Adventure Game")
  print("Collect 6 items to win the game, or be bitten by the Snake.")
  print("Move commands: go South, go North, go East, go West")
  print("Add to Inventory: get 'item name'")

#rooms dictionary
rooms = {
   'Kell Hall' : { 'South' : 'Library South', 'North': 'Library North', 'East' : 'College of Law', 'West' : 'College of Education' },
   'College of Education' : { 'East' : 'Kell Hall'},
   'Library North' : { 'East' : 'College of Business','South': 'Kell Hall'},
   'College of Business' : { 'West' : 'Library North'},
   'Library South' : {'North': 'Kell Hall', 'East': 'University bookstore'},
   'University bookstore' : {'West': 'Library South'},
   'College of Law':{'North': 'Science Center','West': 'Kell Hall'},
   'Science Center':{'South':'College of law'} #villian
}

#item dictionary
items = {
    'Kell Hall': '',
    'Library North': 'Armor',
    'College of Education': 'Shield',
    'College of Business': 'Potion',
    'Library South': 'Sword',
    'University bookstore': 'Book',
    'College of Law':'Helmet',
    'Science Center':'Snake' #villian

}

#variables
current_room = 'Kell Hall'
inventory = []
search_key = 'Kell Hall'


#show current satus
def show_status(current_room, user_move):
        new_room = current_room # declaring
        for i in rooms:  # loop
            if i == current_room:  # if
                if user_move in rooms[i]:  # if
                    new_room = rooms[i][user_move]
        return new_room  # return

def get_item(current_room, user_item):
    if user_item in rooms[current_room]:
        user_item = input("Enter get item name:")
        inventory.append(items[current_room])


show_instructions()
#main program
while True:

    print("\nYou are currently in {}".format(current_room))
    print("\nYou have in your inventory: {}".format(inventory))

    # user enters move for input
    user_move = input("\nEnter 'go North/South/East/West' to move or 'Exit': ").split()[-1].capitalize()





    # user to exit
    if user_move == 'Exit':
        current_room = 'exit'
        break
    if current_room == 'Science Center' and len(inventory)!=6:
        print("You lost the Game Goodbye")
        break


    # enters move for valid input in right room
    elif user_move in rooms[current_room]:
            current_room = rooms[current_room][user_move]
            print("\nYou are currently in {}".format(current_room))

    else:
        print("Cant go that way")
        continue
#if user looses the game but not having all items
    if current_room == 'Science Center' and len(inventory) != 6:
        print(" SSSSSSSSSSS...GAME OVER! \nThanks for playing the game. Hope you enjoyed it.")
        break
#if users had all items and reaches the snake
    if current_room == 'Science Center' and len(inventory) ==6:
        print(" Congratulations! You have collected all items and defeated the snake! \n Thanks for playing the game. Hope you enjoyed it. ")
        break
    if items[current_room]:
        print("\nYou see a " + items[current_room] + " in the room")
        user_item = input("\nAdd to Inventory: get 'item name:'").split()[-1].capitalize()
        if user_item not in inventory and user_item in items[current_room]:
                inventory.append(items[current_room])
        elif user_item in inventory:
            print('\nItem already exist in Inventory')
        elif user_item not in current_room:
             print("\nInvalid that item is not there")
else:
        print("\nInvalid Move. There is no room {}".format(user_move))




