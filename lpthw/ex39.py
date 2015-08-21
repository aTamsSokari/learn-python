# map state names to short forms
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# map cities to state short codes
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# assign some more cities using bracket notation
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print 'NY State has: ', cities['NY']
print 'OR State has: ', cities['OR']

# print out some state abbreviations
print '-' * 10
print 'Michigan\'s abbreviation is: ', states['Michigan']
print 'Florida\'s abbreviation is: ', states['Florida']

# print out some more cities, this time using nested bracket notation
print '-' * 10
print 'Michigan has: ', cities[states['Michigan']]
print 'Florida has: ', cities[states['Florida']]

# print every states abbreviation
print '-' * 10
for state, abbrev in states.items():
    print '%s state is abbreviated as %s' % (state, abbrev)

# print every city in each state
print '-' * 10
for abbrev, city in cities.items():
    print '%s has the city %s' % (abbrev, city)

# do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print '%s state is abbreviated as %s and has %s city' % (state, abbrev,
        cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that may not be there
state = states.get('Texas', None)

if not state:
    print 'Sorry. No Texas'

# get a city with a default value
city = cities.get('TX', 'Does Not Exist.')

print 'The city for state \'TX\' is %s' % city