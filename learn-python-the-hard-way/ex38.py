# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'Fl',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State hsa: ", cities['OR']

#print some states
print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)