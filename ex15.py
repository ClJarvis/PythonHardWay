from sys import argv

script, filename = argv
# open user submitted file
txt = open(filename)
# prints text of file
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
