class Person:
    age = 0
    def __init__(self,initialAge):
        if initialAge < 0: 
            print('Age is not valid, setting age to 0.')
            self.age = 0
        else: self.age = initialAge
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.age < 13: 
            print('You are young.')
        elif self.age >= 13 and self.age < 18: 
            print('You are a teenager.')
        else: print('You are old.')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
    #    print('you are {}'.format(self.age))
        self.age += 1
    #    print('now you are {}'.format(self.age))
        # Increment the age of the person in here