from math import floor

class Farm:

    fields = []
    animals = {'cow': 0, 'pig': 0, 'chicken': 0}
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
        print('pasture -> add some animals to your pasture')
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
        elif input == 'pasture':
            self.pasture()
        elif input == 'exit':
            quit()
        else:
            print("Invalid input, please enter one of the listed options.")
            pass

    def new_field(self):
        print("What kind of field is it: corn, what, or tomacco?")
        field_type = input()
        while field_type not in ['corn', 'wheat', 'tomacco']:
            print("Please enter either corn, wheat, or tomacco.")
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
            elif item['type'] == 'tomacco':
                harvested_food = 50 * item['size']
            print("Harvesting {} food from {} hectare {} field.".format(harvested_food, item['size'], item['type']))
            self.harvest_totals += harvested_food
        self.fields = []
        print("Your animals have been busy breeding!")
        self.animals['pig'] = floor(self.animals['pig'] * 1.5)
        self.animals['cow'] = floor(self.animals['cow'] * 1.2)
        self.animals['chicken'] = floor(self.animals['chicken'] * 2)
        self.status()

    def status(self):
        for item in self.fields:
            print("This {} field is {} hectares.".format(item['type'], item['size']))
        if self.animals['pig'] > 0:
            print("There are {} pigs roaming about right now.".format(self.animals['pig']))
        if self.animals['cow'] > 0:
            print("There are {} cows roaming about right now.".format(self.animals['cow']))
        if self.animals['chicken'] > 0:
            print("There are {} chickens roaming about right now.".format(self.animals['chicken']))
        if self.harvest_totals == 0:
            print("The farm has harvested no food yet.")
        else:
            print("The farm has harvested {} units of food so far.".format(self.harvest_totals))

    def pasture(self):
        print("What kind of animal is it: cow, pig, or chicken?")
        animal_type = input()
        while animal_type not in ['cow', 'pig', 'chicken']:
            print("Please enter either cow, pig, or chicken.")
            animal_type = input()
        print("How many {}s are you adding?".format(animal_type))
        num_animals = int(input())
        if animal_type == 'cow':
            self.animals['cow'] += num_animals
            total_of_new_type = self.animals['cow']
        elif animal_type == 'pig':
            self.animals['pig'] += num_animals
            total_of_new_type = self.animals['pig']
        elif animal_type == 'chicken':
            self.animals['chicken'] += num_animals
            total_of_new_type = self.animals['chicken']
        print("{} {}s have been added to your grazing animals, for a total of {} {}s.".format(num_animals, animal_type, total_of_new_type, animal_type))

    def relax(self):
        if self.fields == []:
            print("That's one empty farm you have right now.")
        else:
            for item in self.fields:
                if item['type'] == 'corn':
                    print("Oh dang look at that, there's {} hectares of corn in that field!".format(item['size']))
                elif item['type'] == 'wheat':
                    print("Aw it's just wheat, but there's {} hectares of it in that field.".format(item['size']))
                elif item['type'] == 'tomacco':
                    print("You hit the motherlode, that's pure tomacco! There's {} hectares of it, ripe for the picking.".format(item['size']))


my_farm = Farm()
my_farm.main_menu()
