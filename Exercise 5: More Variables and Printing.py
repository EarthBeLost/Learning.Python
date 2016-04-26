name = 'Daniel Nathan Williams'
age = 21 # June 14th, 1993 baby!
height = 75 # Inches
height_in_cm = height * 2.54 # Conversion into CM!
weight = 112 # Lbs
weight_in_kg = weight * 0.45 # Conversion in KG!
eyes = 'Green'
teeth = 'White' # O.o
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %f cm tall!" % height_in_cm
print "He's %d pounds heavy." % weight
print "That's %f KG." %weight_in_kg
print "Actually, that's not too bad!"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are always %s because he brushes twice a day!" % teeth

#Apparently this is a tricky line!
print "If I add %d %d and %d I get: %d." % (age, height, weight, age + weight + weight)
