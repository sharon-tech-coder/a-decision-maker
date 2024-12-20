import random

class Decision:
    def __init__(self,title,options=None):
        self.title = title
        self.options = options if options is not None else []
        self.options_data = []

    def collect_options(self):
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

        self.options.extend(option_inputs)
        print("Options collected successfully.")

    def display_options(self):
        print(f"For your decision: {self.title}")
        if len(self.options) == 1:
            print(f"You entered the following option: ")
        else:
            print(f"You entered the following options: ")
        for index, option in enumerate(self.options):
            print(f"{index+1}. {option}")

    def logic_operator(self):
        for index, option in enumerate(self.options):
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
            self.options_data.append(option_data)

    def optimal_option(self):
        if self.options_data:
            optimal = max(self.options_data, key=lambda x: x["final_total_weight"])
            print(f"Your optimal option is: {optimal['option']}")
        else:
            print("No options collected.")
    
    def random_operator(self):
        print("Looks like you'd like to try your luck with uncertainty this time.")
        random_option = random.choice(self.options)
        while True:
            accept_random = input("Please enter 'yes' to receive your result: ").strip().lower()
            if accept_random == 'yes':
                print(f"Here is your random option: {random_option}")
                break
            elif accept_random in ['quit','q'] or accept_random.startswith('q'):
                print("You chose to quit. Going back now.")
                break
            else:
                print("You must enter the exact word 'yes' to receive your answer, or 'quit' to go back.")

    def intuition_operator(self):
        pass

