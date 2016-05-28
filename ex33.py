# ################ chap 33 while loop ###################

'''
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom is %d" % i

print "The numbers: "

for num in numbers:
    print num
'''
#rewoking as a function

def while_rewrite(n):
    i = 0
    numbers = []
    while i < 6:
      numbers.append(n)
      i = i + 1
      print "The Numbers: %d" % i
while_rewrite(1)

