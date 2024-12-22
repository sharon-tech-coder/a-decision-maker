import random
from anytree import Node, RenderTree
from font_colours import *
import json
import os

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

class Decision:
    def __init__(self,title):
        self.title = title
        self.options = []
        self.options_data = []
        self.optimal_option = ""
        self.future_tree = {}
        self.decision_data = {}

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

    def logic_operator(self):
        print("Evaluating your options based on pros and cons.")
        for option in self.options:
            option.add_pros()
            option.add_cons()
            option.calculate_total_weight()
            option.display_pros_and_cons()
            self.options_data.append({
                'name': option.name,
                'pros': option.pros_data,
                'cons': option.cons_data,
                'final_total_weight': option.final_total_weight
            })
        self.optimal_option = max(self.options_data, key=lambda x: x["final_total_weight"])
        print_on_highlights(f"\nBased on pros and cons, your optimal option is: {self.optimal_option['name']}")

    def random_operator(self):
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

    def intuition_operator(self):
        future = colored("future","light_blue")
        print(f"For the options you entered, imagine a {future} with them...")
        root = Node(f"For {self.title} - the following is what you see in the long term:")
        
        for option in self.options:
            child = Node(f"{option}", parent=root)
            while True:
                imagination_2_years = input(f"For option {option}, what do you see in 2 years: ").strip()
                if imagination_2_years:
                    grandchild_level1 = Node(f"In 2 years: {imagination_2_years}", parent=child)
                    self.future_tree["In 2 years"] = imagination_2_years
                    break
                else:
                    print_on_warning("Your imagination can't be empty. Please try again.")
            while True:
                imagination_5_years = input(f"For option {option}, what do you see in 5 years: ").strip()
                if imagination_5_years:
                    grandchild_level2 = Node(f"In 5 years: {imagination_5_years}", parent=grandchild_level1)
                    self.future_tree["In 5 years"] = imagination_5_years
                    break
                else:
                    print_on_warning("Your imagination can't be empty. Please try again.")
            while True:
                imagination_10_years = input(f"For option {option}, what do you see in 10 years: ").strip()
                if imagination_10_years:
                    grandchild_level3 = Node(f"In 10 years: {imagination_10_years}", parent=grandchild_level2)
                    self.future_tree["In 10 years"] = imagination_10_years
                    break
                else:
                    print_on_warning("Your imagination can't be empty. Please try again.")

        for pre, fill, node in RenderTree(root):
            print(f"{pre} {node.name}")

        print_on_successful("Hope that gives you a bit insights.")

    def make_decision(self):
        exit_program = False
        while True:
            while True:
                mode = input(f"\nPlease select a mode - (1) Logic Mode | (2) for Random Mode | (3) for Intuition Mode: ")
                if ('1' in mode and ('2' not in mode and '3' not in mode)) or 'logic' in mode.lower():
                    self.logic_operator()
                    break
                elif ('2' in mode and ('1' not in mode and '3' not in mode)) or 'random' in mode.lower():
                    self.random_operator()
                    break
                elif ('3' in mode and ('1' not in mode and '2' not in mode)) or 'intuition' in mode.lower():
                    self.intuition_operator()
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
                    exit_program = True
                    break
                else:
                    print_on_warning("Sorry I didn't understand you. Please type again.")

            if exit_program:
                break

    def add_decision(self,decision_data):
        self.decision_data = {
            "title": self.title,
            "options": self.options_data,
            "optimal_option":self.optimal_option,
            "future_tree":self.future_tree
        }
        if os.path.exists("decisions.json"):
            with open("decisions.json", "r") as file:
                try:
                    current_data = json.load(file)
                except json.JSONDecodeError:
                    current_data = []
        else:
            current_data = []

        current_data.append(self.decision_data)
        try:
            with open("decisions.json", "w") as file:
                json.dump(current_data, file, indent=4)
        except FileNotFoundError:
            print_on_warning("The folio file does not exist.")
        except json.JSONDecodeError:
            print_on_warning("There was an error accessing your folio.")
        except Exception as e:
            print_on_warning(f"An unexpected error occurred: {e}")

        print_on_successful("Your new decision has been added to the folio.")
        print("But you can't view it now. The function of viewing folio is under construction.")
        print_on_highlights("Meantime, thanks for using Decision Maker v1.0. I hope you've got the answer you wanted.")

    