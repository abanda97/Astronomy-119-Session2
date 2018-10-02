#Include the numpy library
import numpy as np
#this gives us access to the no py library - often a tool to make arrays of different kinds

#Define the main() function
def main():

	i = 0			#Declare an integer i, set to 0
	x = 119.0		#Declare a float x, with val of 119
	
	for i in range(120):	#Loops i from 0 through 119
							#Range is 120 because we are counting 0,1,2,3,4,...119=120 numbers
		if((i%2)==0):		#"i modulo 2"; is used to check if i is equal to 2; essentially saying "If i is even"
			x += 3.0		#add 3 to x
		else:				#if i odd
			x -= 5.0		#x = x - 5
			
	s = "%3.2e" % x			#Make a string that shows x with scientific notation
							#3.2 means 3 significant figures and .2 means 2 places in exponent
	
	print(s)
	
#Now the rest of the program
if __name__ == "__main__":
	main()
	
#continue