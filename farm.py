class Farm:

    fields = []
    harvest_totals = 0

    def main_menu(self):
        while True:
            self.print_main_menu()
            selection = input()
            self.call_action(selection)
            print('')

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
            self.harvest()
        elif input == 'status':
            self.status()
        elif input == 'relax':
            self.relax()
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
        self.fields.append({'type': field_type, 'size': field_size})
        print("Added a {} field of {} hectares!".format(field_type, field_size))

    def harvest(self):
        for item in self.fields:
            if item['type'] == 'corn':
                harvested_food = 20 * item['size']
            elif item['type'] == 'wheat':
                harvested_food = 30 * item['size']
            print("Harvesting {} food from {} hectare {} field.".format(harvested_food, item['size'], item['type']))
            self.harvest_totals += harvested_food
        self.fields = []
        self.status()

    def status(self):
        for item in self.fields:
            if item['type'] == 'corn':
                print("This corn field is {} hectares.".format(item['size']))
            elif item['type'] == 'wheat':
                print("This wheat field is {} hectares.".format(item['size']))
        if self.harvest_totals == 0:
            print("The farm has harvested no food yet.")
        else:
            print("The farm has harvested {} units of food so far.".format(self.harvest_totals))

    def relax(self):
        if self.fields == []:
            print("That's one empty farm you have right now.")
        else:
            for item in self.fields:
                if item['type'] == 'corn':
                    print("Oh dang look at that, there's {} hectares of corn in that field!".format(item['size']))
                elif item['type'] == 'wheat':
                    print("Aw it's just wheat, but there's {} hectares of it in that field.".format(item['size']))


my_farm = Farm()
my_farm.main_menu()
