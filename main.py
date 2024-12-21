

# collect data 
name = input("Welcome to Decision Maker. What's your name? ")
decision = input(f"Hello {name}, what is the decision you'd like to make today? ")
decision_data = {
    "name": name,
    "decision": decision
}

# collect options
while True:
    try:
        option_nums = int(input("How many options do you have in mind? "))
        if option_nums > 0:
            print(f"You have {option_nums} {'option' if option_nums == 1 else 'options'} in mind.")
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Sorry I didn't get you. Please enter a valid number.")

option_inputs = []
options_data = []
for i in range(option_nums):
    while True:
        option_input = input(f"Enter your option {i+1}: ")
        if not option_input.strip():
            print("Sorry you missed it. Please try again.")
        else:
            option_inputs.append(option_input)
            break

print("\nYou entered the following options: ")
for index, option in enumerate(option_inputs):
    print(f"{index+1}. {option}")


# select mode
while True:
    while True:
        mode = input("\nPlease select a mode - #1 for Logic Mode | #2 for Random Mode | #3 for Intuition Mode: ")
        if ('1' in mode and ('2' not in mode and '3' not in mode)) or 'logic' in mode.lower():
            mode = "#1 - Logic Mode"
            print(mode)
            logic_operator()
            break
        elif ('2' in mode and ('1' not in mode and '3' not in mode)) or 'random' in mode.lower():
            mode = "#2 - Random Mode"
            print(mode)
            random_operator()
            break
        elif ('3' in mode and ('1' not in mode and '2' not in mode)) or 'intuition' in mode.lower():
            mode = "#3 - Intuition Mode"
            print(mode)
            intuition_operator()
            break
        else:
            print("Sorry I didn't understand it. Please select from #1 #2 and #3.")

    # retry
    while True:
        retry = input("Would you like to select the mode again? (yes/no): ").strip().lower()
        if (retry in ['yes','y'] or retry.startswith('yes')) and ('n' not in retry):
            break
        elif (retry in ['no','n'] or retry.startswith('no')) and ('y' not in retry):
            print("Thank you for using Decision Maker. I hope you've got the answer you wanted.")
        else:
            print("Sorry I didn't understand you. Please type again.")
