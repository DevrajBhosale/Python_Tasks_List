# Validate user input as an integer.

while(True):
    num = input("Enter a Number: ")
    try:
        if(int(num) or int(num) == 0):
            print(f"You entered: {num}")
            break
    except:
        print("Invalid input. Please enter a number.")
        continue
            