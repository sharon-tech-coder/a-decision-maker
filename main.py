from blueprints import *

if __name__ == "__main__":
    name = input("Welcome to Decision Maker! What's your name? ")
    while True:
        decision = Decision(input(f"Hello, {name}! What is the decision you'd like to make? "))
        if decision.title.strip():
            break
        else:
            print("Sorry I didn't get you. Please try again.")
    decision.collect_options()
    decision.make_decision()
