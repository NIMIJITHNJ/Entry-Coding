n = int(input("Enter the number of rows required for the pyramid: ")) #Taking input from the user
if n <= 0:
    print("Please enter a positive integer")           #Notifying the user to provide a positive integer                        
else:        
    for i in range(1, n+1):                            #Executing a loop that visits every row of the pyramid.
            
        space = n-i                                    #Determining the number of spaces required to align the stars in the centre.
            
        star = 2*i-1                                   #Determining the odd number of stars in the current row
            
        row = '  ' * space + ' *' * star               #Building the row using the calculated spaces and stars.
            
        print(row)                                     #Print the row.