# 1. TASK: print "Hello World"
print( 'hello world' )
# 2. print "Hello Noelle!" with the name in a variable
name = "Hoang Ta"
print( 'this is my', name )	# with a comma
print( 'this is my '+name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( 'my age is', name  )	# with a comma
#print( 'my age is '+ name  )	# with a +	-- this one should give us an error!
print( 'my age is '+ str(name)  )
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "water"
fave_food2 = "melon"
print( 'i love to eat {}, {}'.format(fave_food1,fave_food2) ) # with .format()
print(f"i love to eat {fave_food1}, {fave_food2}") # with an f string