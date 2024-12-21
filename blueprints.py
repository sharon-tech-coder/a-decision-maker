import random
from anytree import Node, RenderTree
from termcolor import colored, cprint

# font colours

print_on_pros = lambda x: cprint(x, "black","on_light_green")
print_on_cons = lambda x: cprint(x, "black","on_light_red")
print_on_warning = lambda x: cprint(x, "light_yellow")
print_on_highlights = lambda x: cprint(x, "white","on_blue")


# class Option

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
                print_on_warning("Sorry the pro can't be empty. Please try again.")
        
        for pro in self.pros:
            while True:
                try: 
                    weight = float(input(f"{pro} - How important is it to you? Please assign a weight (1-10): "))
                    if 1<= weight <= 10:
                        self.pros_data[pro] = weight
                        break
                    else:
                        print_on_warning("Please enter a number between 1 and 10.")
                except ValueError:
                    print_on_warning("Sorry I didn't get you. Please enter a valid number.")

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
                print_on_warning("Sorry the con can't be empty. Please try again.")
            
        for con in self.cons:
            while True:
                try:
                    weight = float(input(f"{con} - How bad is it to you? Please assign a weight (1-10): "))
                    if 1<= weight <= 10:
                        self.cons_data[con] = weight
                        break
                    else:
                        print_on_warning("Please enter a number between 1 and 10.")
                except ValueError:
                    print_on_warning("Sorry I didn't get you. Please enter a valid number.")

    def calculate_total_weight(self):
        self.final_total_weight = sum(self.pros_data.values()) - sum(self.cons_data.values())

    def display_pros_and_cons(self):
        print_on_pros(f"Pros: {', '.join(self.pros)}")
        print_on_cons(f"Cons: {', '.join(self.cons)}")
        print_on_highlights(f"Final Total Weight: {self.final_total_weight}")


# class Decision

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
                coloured_option_nums = colored(option_nums,"blue")
                if option_nums <=0:
                    print_on_warning("Please enter a positive number.")
                elif option_nums == 1:
                    print_on_warning("Only 1 option? Seems like you already made a decision.")
                else:
                    print(f"You have {coloured_option_nums} options in mind.")
                    break
            except ValueError:
                print_on_warning("Sorry I didn't get you. Please enter a valid number.")

        for i in range(option_nums):
            while True:
                option_input = input(f"Enter your option {i+1}/{option_nums}: ").strip()
                if option_input:
                    option_new = Option(option_input)
                    self.options.append(option_new)
                    break
                else:
                    print_on_warning("Sorry you missed it. Please try again.")
        
        print(f"\nFor your decision: {self.title}")
        if len(self.options) == 1:
            print(f"You entered the following option: ")
            for option in self.options:
                print(option)
        else:
            print(f"You entered the following options: ")
            for index, option in enumerate(self.options):
                print_on_highlights(f"{index+1}. {option}")

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
        self.optimal_option = max(self.options_data, key=lambda x: x["final_total_weight"])
        print_on_highlights(f"\nBased on pros and cons, your optimal option is: {self.optimal_option['name']}")

    def random_operator(self,options):
        print("Selecting an option based on pure luck.")
        random_result = random.choice(self.options)
        while True:
            accept_random = input("Please enter 'yes' to receive your result: ").strip().lower()
            if accept_random == 'yes':
                print_on_highlights(f"Here is your random option: {random_result}")
                break
            elif accept_random in ['quit','q'] or accept_random.startswith('q'):
                print("You chose to quit. Going back now.")
                break
            else:
                print_on_warning("You must enter the exact word 'yes' to receive your answer, or 'quit' to go back.")

    def intuition_operator(self,options):
        future = colored("future","light_blue")
        print(f"For the options you entered, imagine a {future} with them...")
        root = Node(f"For {self.title} - the following is what you see in the long term:")
        
        for option in self.options:
            child = Node(f"{option}", parent=root)
            imagination_2_years = input(f"For option {option}, what do you see in 2 years: ")
            grandchild_level1 = Node(f"In 2 years: {imagination_2_years}", parent=child)
            imagination_5_years = input(f"For option {option}, what do you see in 5 years: ")
            grandchild_level2 = Node(f"In 5 years: {imagination_5_years}", parent=grandchild_level1)
            imagination_10_years = input(f"For option {option}, what do you see in 10 years: ")
            grandchild_level3 = Node(f"In 10 years: {imagination_10_years}", parent=grandchild_level2)

        for pre, fill, node in RenderTree(root):
            print(f"\n{pre} {node.name}")

        print_on_highlights("Hope that gives you a bit insights.")

    def make_decision(self):
        exit_program = False
        while True:
            while True:
                mode = input(f"\nPlease select a mode - #1 for Logic Mode | #2 for Random Mode | #3 for Intuition Mode: ")
                if ('1' in mode and ('2' not in mode and '3' not in mode)) or 'logic' in mode.lower():
                    self.logic_operator(self.options_data)
                    break
                elif ('2' in mode and ('1' not in mode and '3' not in mode)) or 'random' in mode.lower():
                    self.random_operator(self.options)
                    break
                elif ('3' in mode and ('1' not in mode and '2' not in mode)) or 'intuition' in mode.lower():
                    self.intuition_operator(self.options)
                    break
                elif mode in ['quit','q'] or mode.startswith('q'):
                    print("You chose to quit. Going back now.")
                    exit_program = True
                    break
                else:
                    print_on_warning("Sorry I didn't understand it. Please select from #1 #2 and #3, or 'quit' to go back.")
            
            if exit_program:
                break

            while True:
                retry = input("\nWould you like to select the mode again? (yes/no): ").strip().lower()
                if (retry in ['yes','y'] or retry.startswith('yes')) and ('n' not in retry):
                    break
                elif (retry in ['no','n'] or retry.startswith('no')) and ('y' not in retry):
                    print("Thank you for using Decision Maker. I hope you've got the answer you wanted.")
                    exit_program = True
                    break
                else:
                    print_on_warning("Sorry I didn't understand you. Please type again.")

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
        print("Guests cannot view saved the decision folio.")