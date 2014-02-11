

# Output should look like this:
    # Restaurant 'Andalu' is rated at 3.
    # Restaurant "Arinell's" is rated at 4.
    # Restaurant 'Bay Blend Coffee and Tea' is rated at 3.
    # Restaurant 'Casa Thai' is rated at 2.
    # Restaurant 'Charanga' is rated at 3.
    # Restaurant 'El Toro' is rated at 5.
    # Restaurant 'Giordano Bros' is rated at 2.
    # Restaurant "Irma's Pampanga" is rated at 5.
    # Restaurant 'Little Baobab' is rated at 1.
    # Restaurant 'Pancho Villa' is rated at 3.
    # Restaurant 'Taqueria Cancun' is rated at 2.
    # Restaurant 'Urbun Burger' is rated at 1.

# Read file
f = open('scores.txt')

# Initiate empty dict
rest_scores = {}

# Go line by line to go through each line to split key/value pairs by colon(:)
for line in f:
    line = line.strip()
    split_line = line.split(":")
    rest_scores[split_line[0]] = split_line[1]
# print "Restaurant %s is rated at %s" % (, rest_scores[keys])

# Return ratings in alphabetical order by restaurant
alpha_rest = sorted(rest_scores.keys())
for restaurant in alpha_rest:
    print "Restaurant %s is rated at %s" % (restaurant, rest_scores[restaurant])


"""
TO-DO Try to sort by score and then by restaurant alpha order. Use sorted tuples 
instead of creating a reverse index dictionary like in Ex 6
"""



"""
# How to use readline - need to use a while loop

# Need to assign readline to variable so can reference in the while loop w/o moving to next line

line = f.readline()
while line is not None:
    line = line.strip()
    ...
# Need this to move to the next line or else will just keep reading same line
    line = f.readline()
"""
