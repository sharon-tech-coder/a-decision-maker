import random

class Option:
    def __init__(self,name):
        self.name = name
        self.pros = []
        self.pros_data = {}
        self.cons = []
        self.cons_data = {}
        self.final_total_weight = None

    def add_pros(self):
        pros = input("What are the pros? Please use '|' to separate them: ")
        self.pros = pros.split('|')
        for pro in self.pros:
            while True:
                try: 
                    weight = float(input(f"{pro} - How important is it to you? Please assign a weight (1-10): "))
                    if 1<= weight <= 10:
                        self.pros_data[pro] = weight
                        break
                    else:
                        print("Please enter a number between 1 and 10.")
                except ValueError:
                    print("Sorry I didn't get you. Please enter a valid number.")

    def add_cons(self):
        cons = input("What are the cons? Please use '|' to separate them: ")
        self.cons = cons.split('|')
        for con in self.cons:
            while True:
                try:
                    weight = float(input(f"{con} - How bad is it to you? Please assign a weight (1-10): "))
                    if 1<= weight <= 10:
                        self.cons_data[con] = weight
                        break
                    else:
                        print("Please enter a number between 1 and 10.")
                except ValueError:
                    print("Sorry I didn't get you. Please enter a valid number.")

    def calculate_total_weight(self):
        self.final_total_weight = sum(self.pros_data.values()) - sum(self.cons_data.values())

    def display_pros_and_cons(self):
        pass


class Decision:
    def __init__(self,title):
        self.title = title
        self.options = []
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

        for i in range(option_nums):
            while True:
                option_input = input(f"Enter your option {i+1}/{option_nums}: ")
                if not option_input.strip():
                    print("Sorry you missed it. Please try again.")
                else:
                    self.options.append(option_input)
                    break
        print("Options collected successfully.")
        
    def display_options(self):
        print(f"For your decision: {self.title}")
        if len(self.options) == 1:
            print(f"You entered the following option: ")
            for option in self.options:
                print(option)
        else:
            print(f"You entered the following options: ")
            for index, option in enumerate(self.options):
                print(f"{index+1}. {option}")


class Operation:
    @staticmethod
    def logic_operator(options_data):
        print("Evaluating your options based on pros and cons.")
        optimal_option = max(options_data, key=lambda x: x["final_total_weight"])
        print(f"Your optimal option is: {optimal_option['option']}")

    @staticmethod
    def random_operator(options):
        print("Selecting an option based on pure luck.")
        random_option = random.choice(options)
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

    @staticmethod
    def intuition_operator():
        print("Intuition operator is under construction...")
