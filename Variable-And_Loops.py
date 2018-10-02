import numpy as np	#We use numpy for many things

def main():
	i = 0		#Declare i equal to 0
	n = 10		#Declare n equal to 10
	x = 119.0	#Declare x equal to 119.0
	
	#We can use numpy to quickly make arrays
	y = np.zeros(n,dtype=float) #declares 10 zeros
	
	#We can use four loops to iterate through a varable
	for i in range(n): #i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1.0 #Set y = 2i+1
	#We can iterate through the y elements one by one
	for y_element in y:
		print(y_element)
		
#execute the main function
if __name__ == "__main__":
	main()

#This program is designed to list the first 10 odd numbers in a sequential
#list starting from 0.