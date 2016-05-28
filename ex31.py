print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a chesse cake. what do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
      print "The Bear eats your face off. Good Jorb!"
    elif bear == "2":
      print "the Bear eats your legs off. Good Job!"
    else:
      print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow Jacket clothepins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
      print "Your body survives powered by a mind of Jello. Good Job!"
    else:
      print "The insanity rots yours eyes into a pool of muck. Good Jorb!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
