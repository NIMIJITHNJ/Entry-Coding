#Recursive Function to Generate Fibonacci Series

def fibonacci(index):                                     #Function calculating the Fibonacci number using recursion.
    if index == 0:                                        #Return Fibonacci number at index 0.
        return 0
    elif index == 1:                                      #Return Fibonacci number at index 1.
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)    #Return Fibonacci number at any other index other than 0 or 1.  

try:    
    terms = int(input('Enter the required number of terms in the fibonacci series: '))  #Take input from the user - Number of terms in the Fibonacci series.
    if terms <= 0:                                                                      #To check whether the input is a positive integer.
        print('Please enter a positive integer')
    else:
        print('\nThe Fibonacci series of first', terms, 'term(s):')
    for i in range(terms):                                                          #Loop to create the Fibonacci series having terms requested by the user.        
        if i == terms-1:                                                            #Check the last element in the series.
            print(fibonacci(i),'\n')                                                #Print the last element in the series.
        else:
            print(fibonacci(i), end=' , ')                                          #Print all other element except the last one.
except ValueError:
    print('Invalid input!, Please enter a valid number')                            #try-except block to handle invalid user inputs.