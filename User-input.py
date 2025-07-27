adult_vari = input("Are you an adult? Type yes or no: ").strip().lower()

if adult_vari == "yes":
    x = True
    while x:
        age = input("Enter your age: ")
        try:
            y = float(age)
            x = False  # input is valid, exit loop
        except ValueError:
            print("Oops! That's not a valid number. Try again...")
else:
    print("Okay, not an adult!")
