from file_operations import load_data, save_data

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
        print("Use pros and cons to sort out what's the best for you.")
        
        for index, option in enumerate(option_inputs):
            print(f"For option {index+1}. {option} - ")

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

            option_data = {
                "option":option,
                "pros": pros_dict,
                "cons": cons_dict,
                "final_total_weight": final_total_weight
            }
            options_data.append(option_data)
        
        # update decision data
        decision_data["options_data"] = options_data
        optimal_option = max(options_data,key=lambda x: x[final_total_weight])
        
        # save data to a json file
        print("Thanks for your entry.")
        save_data(decision_data,'decision_data.json')

        # reporting
        print(f"Based on pros and cons, it seems that the following option emerges as the most optimal choice:\n{optimal_option['option']}")
        if optimal_option["final_total_weight"] < 0:
            print("Just a friendly reminder - even if it is your preferred option, the cons still outweigh the pros.")
            
        
    # random mode
    elif mode == "#2 - Random Mode":
        import random
        print("Looks like you'd like to try your luck with uncertainty this time.")
        random_option = random.choice(option_inputs)
        while True:
            accept_random = input("Please enter 'yes' to receive your result: ").strip().lower()
            if accept_random == 'yes':
                print(f"Here is your random option: {random_option}")
                break
            else:
                quit_random = input("You have to enter the exact word 'yes' to receive your answer. Just a little effort to pay. \nAlternatively enter 'quit' to go back: ").strip().lower()
                if quit_random in ['quit','q'] or quit_random.startswith('q'):
                    break
                elif quit_random == 'yes':
                    print(f"Here is your random option: {random_option}")
                    break
                else:
                    print("Sorry I didn't understand you.")
                    
    # intuition mode
    else:
        pass

    # retry
    while True:
        retry = input("Would you like to select the mode again? (yes/no): ").strip().lower()
        if (retry in ['yes','y'] or retry.startswith('yes')) and ('n' not in retry):
            break
        elif (retry in ['no','n'] or retry.startswith('no')) and ('y' not in retry):
            print("Thank you for using Decision Maker. I hope you've got the answer you wanted.")
        else:
            print("Sorry I didn't understand you. Please type again.")
