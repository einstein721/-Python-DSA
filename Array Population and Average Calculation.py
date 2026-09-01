# Initialize an empty list (array) to store the user inputs
values_array = []

# Use a for loop to continually ask the user for 5 values
for i in range(5):
    # Prompt user for input, convert to float, and dynamically display the current iteration
    user_input = float(input(f"Enter value {i + 1} of 5: "))
    
    # Append the entered value to the array
    values_array.append(user_input)

# Calculate the sum of all values in the array
total_sum = sum(values_array)

# Calculate the average by dividing the sum by the length of the array
average = total_sum / len(values_array)

# Display the populated array and the calculated average
print(f"The values input into the array are: {values_array}")
print(f"The average of these values is: {average}")
