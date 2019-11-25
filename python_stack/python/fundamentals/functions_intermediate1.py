# import random
# def randInt(min=0, max = 100):
#     num = random.random()
#     return num
# print(randInt()) 		    # should print a random integer between 0 to 100
# print(randInt(max=50)) 	    # should print a random integer between 0 to 50
# print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

import random
def randInt():
    m = random.random()*3
    return round(m)
print(randInt())
# print(randInt(max=1000))
# print(randInt(min=90))
# print(randInt(min=40, max=80))
