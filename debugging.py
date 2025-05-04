import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')  #To set the logging level to DEBUG so that debug messages are shown in the terminal

def calculateAverage(numbers):                                                  #Function to calculate the average of numeric values in the given list

    try:

        if not isinstance(numbers, list):                                       #To Check if the input is a list
            raise TypeError("Input must be a list.")
        
        logging.debug(f"Original input: {numbers}")                             #To log the original list of values for debugging

        numericValues = [x for x in numbers if isinstance(x, (int, float))]     #To filter only int and float values and ignore other entries

        logging.debug(f"Filtered numeric values: {numericValues}")              #To log the filtered numeric values for verification

        if not numericValues:                                                   #To raise an error if no valid numeric values remain
            raise ValueError("There are no numeric values to calculate average.")

        average = sum(numericValues) / len(numericValues)                       #Calculating the average

        logging.debug(f"Calculated average: {average}")                         #To log the final calculated average

        return average

    except TypeError as e:                                                      #To Catch TypeError if invalid operations are attempted
        print("TypeError:", e)

    except ValueError as ve:                                                    #To Catch ValueError if the input is empty or all elements are invalid
        print("ValueError:", ve)

#Test Cases

print("Average:", calculateAverage([15, 25, 35]))                              #Case 1: Valid list of numbers (Expected: 25)

print("Average:", calculateAverage([22, 'c', 43]))                             #Case 2: Mixed list with non-numeric value (Expected: 32.5 ignoring 'c')

print("Average:", calculateAverage(['a', 'b']))                                #Case 3: Only non-numeric values (Expected: ValueError)

print("Average:", calculateAverage([]))                                        #Case 4: Empty list (Expected: ValueError)

print("Average:", calculateAverage(123))                                       #Case 5: Invalid input, not a list (Expected: TypeError)