from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
       dead("You greedy bastard!")


def bear_room():
    print "there is a bear in here."
    print "The bear has a bunch of honey."
    print "The fat bear is infront of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "Take honey":
          dead("the bear looks at you the slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print   'the beqar has moved from the dooe. You can go throuh it now.'
            bear_moved =  True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and ches off your leg.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

#start()


