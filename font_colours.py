from termcolor import colored, cprint

print_on_pros = lambda x: cprint(x, "black","on_light_green")
print_on_cons = lambda x: cprint(x, "black","on_light_red")
print_on_warning = lambda x: cprint(x, "light_yellow")
print_on_highlights = lambda x: cprint(x, "white","on_blue")
print_on_successful = lambda x: cprint(x, "light_green")
