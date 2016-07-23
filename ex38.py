ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things on that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print "adding: ", next_one
  stuff.append(next_one)
  print "There are %d items now" % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #Whoa fancy coding
print stuff.pop()
print ' '.join(stuff) #Whoa cool
print '#'.join(stuff[3:5]) #Super Stellar
print '$'.join(stuff) #testing join
print ' '.join(stuff[3:5]) #Super test
