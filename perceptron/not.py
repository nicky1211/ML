from random import choice 
from numpy import array, dot, random 
unit_step = lambda x: 0 if x < 0 else 1

training_data = [ 
					
					(array([0,1]), 1), 
					(array([1,1]), 0), 
 ] 
w = random.rand(2) 
errors = [] 
eta = 0.2 
n = 100 
for i in xrange(n): 
	x, expected = choice(training_data) 
	result = dot(w, x) 
	error = expected - unit_step(result) 
	errors.append(error) 
	w += eta * error * x 
for x, _ in training_data: 
	result = dot(x, w) 
	print("{}: {} -> {}".format(x[:1], result, unit_step(result)))
