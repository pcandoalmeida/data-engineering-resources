import sys

class Menu():

    def __init__(self, title, options):
        self.title = title
        self.options = {
                "0": self.quit,
                "1": self.option_menu,
                "2": self.order_menu,
                "3": self.courier_menu
                }

    def display_menu(self):
        print("""
Main Menu
0. Quit
1. Open options menu
2. Open orders menu
3. Open couriers menu
""")

    def run(self):
        '''Display the menu and respond to the options.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid option")

    def quit(self):
        print("Thank you for using your cafe today.")
        sys.exit(0)


