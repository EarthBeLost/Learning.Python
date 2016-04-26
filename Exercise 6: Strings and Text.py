# This line gives X a value of a string.
x = "There are %d types of people." % 10
# This is a pointless variable.
binary = "binary"
# So is this one but I had to do it... following the book!
do_not = "don't"
# This gives Y a value with 2 values.
y = "Those who know %s and those who %s" % (binary, do_not)

# Prints X and Y.
print x
print y

# It prints out X and Y again but in a different format.
print "I said: %r" %x
print "I also said: '%s'." % y

# Assigns a value to hilarious and joke_evaluation...
hilarious = False
joke_evaluation = "Isn't that joke sooo funny?! %r"

# Prints out joke_evaluation and hilarious, for fun.
print joke_evaluation % hilarious

# Assigns some more variables!
w = "This is the left side of..."
e = "a string with a right side!"

#This prints them both out.
print w + e
