# A Decision Maker

An app that facilitates and helps decision making. 

## Features
- input a decision that user need to make
- input pros and cons
- assign weights to pros and cons
- calculate and display the optimal option
- a random mode which selects a random option from the provided inputs
- a decision tree which displays what you see in the future

## Introduction
Decision Maker is a Python-based application that helps you make decisions by evaluating multiple options. It provides three different modes:
- Logic Mode - Evaluate the pros and cons of options.
- Random Mode - Select an option randomly.
- Intuition Mode - Imagine future outcomes and visualize long-term results.
The application allows you to input options, weigh the pros and cons, and even visualize potential future scenarios before making your decision.

## System Requirements
- Python 3.7 or higher
- anytree for managing hierarchical structures (used for visualizing future scenarios)
- termcolor for text color formatting in the terminal

## Installing Dependencies
Install Python: Download and install Python from python.org.
Install Required Libraries:
- pip install anytree
- pip install termcolor

## File Structure
.
├── blueprints.py            # Core logic for the Decision and Option classes
├── font_colours.py          # Helper functions for terminal text color formatting
├── main.py                  # Main script to run the Decision Maker
├── requirements.txt         # To install the same packages in a new environment
├── decisions.json           # To save your decision files, but the viewing function is under construction
├── LICENSE.md               # Licenses info
├── LICENSE.md               # Security documentation
└── README.md                # This README file

## Key Modes
1. Logic Mode
In this mode, you evaluate your options based on the pros and cons. You assign a weight to each pro and con (on a scale of 1-10), and the application calculates the total score for each option. The option with the highest score is considered the optimal choice.
2. Random Mode
If you are uncertain, this mode randomly selects one of the options for you. It's a quick, fun way to make decisions when you're not sure what to choose.
3. Intuition Mode
In this mode, you imagine the long-term consequences of each option. You envision what the future might look like in 2, 5, and 10 years with each choice. This helps you visualize the impact of your decision.

## How To Use
1. Open a terminal window.
2. Navigate to the folder where you have saved the Decision Maker files.
3. Run the following command: python main.py

## Troubleshooting
- Error: "Please enter a valid number"
Cause: You entered a value that isn’t a valid number (e.g., a string).
Solution: Ensure that you enter a valid number between 1-10 when assigning weights to pros and cons.
- Error: "Sorry, I didn't get you"
Cause: The program didn’t understand your input (e.g., an empty string).
Solution: Follow the exact instructions given by the program, ensuring you provide input in the expected format.

