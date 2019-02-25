class Farm:

    def main_menu(self):
        while True:
            self.print_main_menu()
            selection = input()
            self.call_action(selection)

    def print_main_menu(self):
        print('Options:')
        print('field -> adds a new field')
        print('harvest -> harvests crops and adds to total harvested')
        print('status -> displays some information about the farm')
        print('relax -> provides lovely descriptions of your fields')
        print('exit -> exits the program')

    def call_action(self, input):
        if input == 'field':
            self.new_field()
        elif input == 'harvest':
            # call the harvest function
            pass
        elif input == 'status':
            # call the status function
            pass
        elif input == 'relax':
            # display info about the fields
            pass
        elif input == 'exit':
            quit()

    def new_field(self):
        print("What kind of field is it: corn or what?")
        field_type = input()
        while field_type not in ['corn', 'wheat']:
            print("Please enter either corn or wheat.")
            field_type = input()
        print("How large is the field in hectares?")
        field_size = int(input())
        # If I have time, add something here to make sure the input is an int
        # add a new field to our list of fields
        print("Added a {} field of {} hectares!".format(field_type, field_size))


my_farm = Farm()
my_farm.main_menu()
