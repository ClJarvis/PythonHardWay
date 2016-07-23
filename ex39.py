#Creating amapping of state to abbrevation
states = {
  'Oregon' : 'OR',
  'Florida': 'FL',
  'California' : 'CA',
  'New York' : 'NY',
  'Tennesse' : 'TN'
}

#creating a list of states and thier cities
cities = {
  'CA': 'San Francisco',
  'TN': 'Nashville',
  'FL': 'Orlando'
}

#Test spacing
#print states['Oregon']
#print cities['TN']
#RESULT Spacing of : after Key has no effect on running program BUut looks better to have it after key

#add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR has:", cities['OR']

#print some states
print '_' * 10
print "Tennesse's abbrevation is:", states['Tennesse']
print "Florida's abbrevation is:", states['Florida']

#do it by using the state then cities dict
print '_' * 10
print "Tennesse has:", cities[states['Tennesse']]
print "Florida has:", cities[states['Florida']]

#print every state abbrevation
print '_' * 10
for state, abbrev, in states.items():
  print "%s is abbreviated %s" % (state, abbrev)

# Print every city in state
print '_' * 10
for abbrev, city in cities.items():
  print "%s has the city %s" % (abbrev, city)

# now do both at teh saem time
print '_' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
print '_' * 20
# safely get an abbrevation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city





