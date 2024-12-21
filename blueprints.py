import random

class Option:
    def __init__(self,name):
        self.name = name
        self.pros = []
        self.pros_data = {}
        self.cons = []
        self.cons_data = {}
        self.final_total_weight = None

    def __str__(self):
        return self.name

    def add_pros(self):
        while True:
            pros = input(f"\nFor option {self.name} - What are the pros? Please use '|' to separate them: ")
            self.pros = pros.split('|')
            new_pros_list = []
            for pro in self.pros:
                if pro.strip():
                    new_pros_list.append(pro)
            if new_pros_list:
                self.pros = new_pros_list
                break
            else:
                print("Sorry the pro can't be empty. Please try again.")
        
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
        while True:
            cons = input(f"\nFor option {self.name} - What are the cons? Please use '|' to separate them: ")
            self.cons = cons.split('|')
            new_cons_list = []
            for con in self.cons:
                if con.strip():
                    new_cons_list.append(con)
            if new_cons_list:
                self.cons = new_cons_list
                break
            else:
                print("Sorry the con can't be empty. Please try again.")
            
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
        print(f"Pros: {', '.join(self.pros)}")
        print(f"Cons: {', '.join(self.cons)}")
        print(f"Final Total Weight: {self.final_total_weight}")


class Decision:
    def __init__(self,title):
        self.title = title
        self.options = []
        self.options_data = []
        self.optimal_option = None

    def __str__(self):
        return self.title

    def collect_options(self):
        while True:
            try:
                option_nums = int(input("How many options do you have in mind? Please enter a number no smaller than 2: "))
                if option_nums <=0:
                    print("Please enter a positive number.")
                elif option_nums == 1:
                    print("Only 1 option? Seems like you already made a decision.")
                else:
                    print(f"You have {option_nums} options in mind.")
                    break
            except ValueError:
                print("Sorry I didn't get you. Please enter a valid number.")

        for i in range(option_nums):
            while True:
                option_input = input(f"Enter your option {i+1}/{option_nums}: ").strip()
                if option_input:
                    option_new = Option(option_input)
                    self.options.append(option_new)
                    break
                else:
                    print("Sorry you missed it. Please try again.")
        
        print(f"\nFor your decision: {self.title}")
        if len(self.options) == 1:
            print(f"You entered the following option: ")
            for option in self.options:
                print(option)
        else:
            print(f"You entered the following options: ")
            for index, option in enumerate(self.options):
                print(f"{index+1}. {option}")

    def logic_operator(self,options_data):
        print("Evaluating your options based on pros and cons.")
        for option in self.options:
            option.add_pros()
            option.add_cons()
            option.calculate_total_weight()
            self.options_data.append({
                'name': option.name,
                'final_total_weight': option.final_total_weight
            })
        self.optimal_option = max(options_data, key=lambda x: x["final_total_weight"])
        print(f"\nBased on pros and cons, your optimal option is: {self.optimal_option['name']}")

    def random_operator(self,options):
        print("Selecting an option based on pure luck.")
        random_result = random.choice(options)
        while True:
            accept_random = input("Please enter 'yes' to receive your result: ").strip().lower()
            if accept_random == 'yes':
                print(f"Here is your random option: {random_result}")
                break
            elif accept_random in ['quit','q'] or accept_random.startswith('q'):
                print("You chose to quit. Going back now.")
                break
            else:
                print("You must enter the exact word 'yes' to receive your answer, or 'quit' to go back.")

    def intuition_operator(self):
        pass

    def make_decision(self):
        exit_program = False
        while True:
            while True:
                mode = input("\nPlease select a mode - #1 for Logic Mode | #2 for Random Mode | #3 for Intuition Mode: ")
                if ('1' in mode and ('2' not in mode and '3' not in mode)) or 'logic' in mode.lower():
                    self.logic_operator(self.options_data)
                    break
                elif ('2' in mode and ('1' not in mode and '3' not in mode)) or 'random' in mode.lower():
                    self.random_operator(self.options)
                    break
                elif ('3' in mode and ('1' not in mode and '2' not in mode)) or 'intuition' in mode.lower():
                    print('maintaining...')
                    break
                else:
                    print("Sorry I didn't understand it. Please select from #1 #2 and #3.")

            while True:
                retry = input("Would you like to select the mode again? (yes/no): ").strip().lower()
                if (retry in ['yes','y'] or retry.startswith('yes')) and ('n' not in retry):
                    break
                elif (retry in ['no','n'] or retry.startswith('no')) and ('y' not in retry):
                    print("Thank you for using Decision Maker. I hope you've got the answer you wanted.")
                    exit_program = True
                    break
                else:
                    print("Sorry I didn't understand you. Please type again.")

            if exit_program:
                break

class User:
    def __init__(self,username = None,passwords = None):
        self.username = username
        self.passwords = passwords
        self.decision_folio = []

    def verify_passwords(self):
        input_passwords = input("Enter your password: ")
        if input_passwords == self.passwords:
            return True
        else:
            return False

    def add_to_folio(self,decision_item):
        if self.verify_passwords():
            self.decision_folio.append(decision_item)
        else:
            print("Failed to verify passwords. Please try again.")

    def view_folio(self):
        if self.verify_passwords():
            pass
        else:
            print("Failed to verify passwords. Please try again.")

class Guest(User):
    def __init__(self):
        super().__init__(username=None, passwords=None)

    def add_to_folio(self, decision_item):
        print("Guests cannot add items to the folio.")

    def view_folio(self):
        return super().view_folio()