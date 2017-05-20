def cheese_and_cracker(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of cheese_and_cracker!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_cracker(20,30)

print "OR, we can use cariables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_cracker(amount_of_cheese,amount_of_crackers)
