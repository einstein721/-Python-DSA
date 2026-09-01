# SET x TO 0, y TO 20
x = 0
y = 20

# REPEAT block initialization
while True:
    # SUBTRACT 4 FROM y
    y -= 4
    
    # ADD 2/y TO x
    x += (2 / y)
    
    # UNTIL y IS LESS THAN 6 (evaluate the exit condition)
    if y < 6:
        break # Exit the loop if the condition is met

# DISPLAY x
print(f"The value of x is: {x}")
