def logic_operator():

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
    return final_total_weight
