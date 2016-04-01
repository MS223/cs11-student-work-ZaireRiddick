a = 0
while a< 100:
	print a
"""
Prediction: 0 will be printe on a continuous loop
Observation: the code made 0 appear an infinite amount of times
 """

a = 0
while a < 100:
	a = a + 1
	print a
"""
Prediction: the code will go faster, adding 0 faster than before
Observation: the coe does the same thing, not sure if faster
 """

a = raw_input("Would you like to quit: ")
while a != "y":
	a = raw_input("Would you like to quit: ")
"""
Prediction: gives the option to quit the loop
Observation: "there is too much output to process"
 """
