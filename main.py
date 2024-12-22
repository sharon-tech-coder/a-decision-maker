from blueprints import Decision
from font_colours import *

def main():
    print("Welcome to the Decision Maker!")
    while True:
        decision_title = input("What is the decision you'd like to make? ").strip()
        if decision_title:
            decision = Decision(decision_title)
            decision.collect_options()
            decision.make_decision()
            decision.add_decision(decision.decision_data)
            break
        else:
            print_on_warning("Decision title cannot be empty. Please try again.")

if __name__ == "__main__":
    main()
