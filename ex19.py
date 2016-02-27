#function is defined with arguments
def chesse_and_crakers(chesse_count, boxes_of_crackers):
  #lines are printed with variables
    print "You have %d chesses!" % chesse_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"
# notice unindented here
# 20 and 30 are set directly to the % d
print "We can just give the function numbers directly:"
chesse_and_crakers(20, 30)

# setting variables in script form
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

chesse_and_crakers(amount_of_cheese, amount_of_crackers)

#Setting variables with math
print "We can even do math insdie too:"
chesse_and_crakers(10 + 20, 5 + 6)

print "and we can combine the two, variables and math:"
chesse_and_crakers(amount_of_cheese + 100, amount_of_crackers + 1000)

def book_collection(authors, titles):
    print "My collection contains books by %d authors!" % authors
    print "and over %d titles" % titles
    print "Time to read! \n"

book_collection(25, 400)

