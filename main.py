from file_operations import load_data, save_data

# collect data 
name = input("Welcome to Decision Maker. What's your name? ")
decision = input(f"Hello {name}, what is the decision you'd like to make today? ")

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
    mode = input("\nPlease select a mode - #1 for Logic Mode | #2 for Random Mode | #3 for Intuition Mode: ")
    if ('1' in mode and ('2' not in mode and '3' not in mode)) or 'logic' in mode.lower():
        mode = "#1 - Logic Mode"
        print(mode)
        break
    elif ('2' in mode and ('1' not in mode and '3' not in mode)) or 'random' in mode.lower():
        mode = "#2 - Random Mode"
        print(mode)
        break
    elif ('3' in mode and ('1' not in mode and '2' not in mode)) or 'intuition' in mode.lower():
        mode = "#3 - Intuition Mode"
        print(mode)
        break
    else:
        print("Sorry I didn't understand it. Please select from #1 #2 and #3.")

# logic mode
if mode == "#1 - Logic Mode":
    print("Use your sensible side to sort out what's the best for you. Let's think of a few pros and cons.")
    pros = input("What are the pros? Please use '|' to separate them: ")
    cons = input("What are the cons? Please use '|' to separate them: ")

    pros_list = pros.split('|')
    cons_list = cons.split('|')

    pros_dict = {}
    for pro in pros_list:
        while True:
            try: 
                weight = float(input(f"{pro} - How important is it to you? Please assign a weight (1-10) to it: "))
                if 1<= weight <= 10:
                    pros_dict[pro] = weight
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Sorry I didn't get you. Please enter a valid number.")
    pros_total_weights = sum(pros_dict.values())

    cons_dict = {}
    for con in cons_list:
        while True:
            try:
                weight = float(input(f"{con} - How bad is it to you? Please assign a weight (1-10) to it: "))
                if 1<= weight <= 10:
                    cons_dict[con] = weight
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Sorry I didn't get you. Please enter a valid number.")
    cons_total_weights = sum(cons_dict.values())

    final_total_weight = pros_total_weights - cons_total_weights



# save data to a json file

        

