from file_operations import load_data, save_data
from input_operations import float_maker, input_pro_weight, input_con_weight

# collect data - logic mode
name = input("Welcome to Decision Maker - Logic Mode. What's your name? ")
decision = input(f"Hello {name}, what is the decision you'd like to make today?" )

input_pro_weight = input("How important is it to you?(rate between 1 to 10): ")
input_con_weight = input("How terrible is it to you?(rate between 1 to 10): ")

option_1 = input("Now think about 2 options. What is your first option? ")
op1_pros_1 = input("Now think about 3 pros and 3 cons to help you make this decision. What's the 1st pro in your mind? ")
op1_pros_1_weight = input_pro_weight
op1_pros_2 = input("Now think about the 2nd pro. What is it? ")
op1_pros_2_weight = input_pro_weight
op1_pros_3 = input("Now think about the last pro. What is it? ")
op1_pros_3_weight = input_pro_weight
op1_cons_1 = input("Now it's time to think about 3 cons. Enter the 1st con: ")
op1_cons_1_weight = input_con_weight
op1_cons_2 = input("Now think about the 2nd con. What is it? ")
op1_cons_2_weight = input_con_weight
op1_cons_3 = input("Now think about the last con. What is it? ")
op1_cons_3_weight = input_con_weight

option_2 = input("Now think about your 2nd option. What is it? ")
op2_pros_1 = input("Now think about 3 pros and 3 cons. What's your 1st pro? ")
op2_pros_1_weight = input_pro_weight
op2_pros_2 = input("Now think about the 2nd pro. What is it? ")
op2_pros_2_weight = input_pro_weight
op2_pros_3 = input("Now think about the last pro. What is it? ")
op2_pros_3_weight = input_pro_weight
op2_cons_1 = input("Now it's time to think about 3 cons. Enter the 1st con: ")
op2_cons_1_weight = input_con_weight
op2_cons_2 = input("Now think about the 2nd con. What is it? ")
op2_cons_2_weight = input_con_weight
op2_cons_3 = input("Now think about the last con. What is it? ")
op2_cons_3_weight = input_con_weight

# convert weight to float
input_pro_weight = float_maker(input_pro_weight)

# structure the data in a dictionary
decision_data = [
    option_1,option_2
]

# save data to a json file
save_data(decision_data,'decision_data.json')
    

