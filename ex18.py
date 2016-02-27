#the function is like a script with an argv
def print_two_args(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#that args is pointless, can just do  this
#In Python we can skip the whole unpacking arguments and just use the names we want right inside ().
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


#this justtakes one argument
def print_one(arg1):
    print "agr1: %r" % arg1

# this one take no areguments
def print_none():
    print "I got nothin'."

print_two_args("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#"To 'run,' 'call,' or 'use' a function all mean the same thing."
