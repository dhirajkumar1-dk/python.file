# Input number from the user
num = int(input("Enter a number: "))

# Handle the case where the user enters 0
if num == 0:
    print("Digit 0 occurs 1 time")
else:
    # Make the number positive if it's negative
    if num < 0:
        num = -num

    # We check for every possible digit from 0 to 9
    digit_to_check = 0
    while digit_to_check <= 9:
        count = 0
        temp = num  # Use a temporary variable to loop through the number
        
        # Extract digits one by one using a while loop
        while temp > 0:
            last_digit = temp % 10  # Get the last digit
            if last_digit == digit_to_check:
                count += 1
            temp = temp // 10  # Remove the last digit
        
        # If the digit was found in the number, print its count
        if count > 0:
            print(f"Digit {digit_to_check} occurs {count} time(s)")
            
        digit_to_check += 1

num = int(input("Enter the number"))

