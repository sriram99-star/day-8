# Python program to print 
# mean of elements 

  
# list of elements to calculate mean 

n_num = list(input (" Enter 3 numbers to find its mean"))

n = len(n_num) 

  

get_sum = sum(n_num) 

mean = get_sum / n 

  

print("Mean / Average is: " + str(mean))
