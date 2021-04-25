# Consider the case of an installation wizard.

# A typical wizard may contain multiple phases or screens 
# that capture a user's preferences.

# While the user browses through the wizard, s/he makes certain choices.
# Wizards are typically implemented with the Command pattern.
# A wizard is first launched with an object called the Command object. 
# The preferences or choices made by the user in multiple phases of the wizard 
# are then stored in the Command object.
# 
# When the user clicks on the Finish button on the last screen of the wizard,
# the Command object runs an execute() method,
# which considers all the stored choices and runs the appropriate installation procedure.
# Thus, all the information regarding the choices are encapsulated in an object
# that can be used later to take an action.






# The following Python code implements the Command design pattern.
# We talked about the example of the wizard earlier in this chapter 
# Consider that we want to develop a wizard for installation or, popularly, installer 
# Typically, an installation implies the copying or moving of files in the
# filesystem based on the choices that a user makes.
# In the following example, 
# In the client code, we start by creating the Wizard object and
# use the preferences() method that stores the choices made by the user
# during various screens of the wizard. 
# On the wizard, when Finish button is clicked, 
# the execute() method is called. 
# the execute() method picks up the preference and starts the installation:
class Wizard():
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir 
        self.src = src 
    
    def preferences(self, command):
        self.choices.append(command)
    
    def execute(self):
        
        print('{}'.format(self.choices))
        print("{}: '{}' are an element of this list = {}".format(self.choices[0], self.choices[1], self.choices))
        for choice in self.choices:

            print(f'choice is {choice.values()}')
            print(f'list of choice is {list(choice.values())}')
            if list(choice.values())[0]:
                print('Copying binaries --', self.src, ' to ', self.rootdir)
            else:
                print('No Operation') 

if __name__ == '__main__':
    ## Client code 
    wizard = Wizard('Python3.5.gzip', '/usr/bin')
    ## Users chooses to install Python only 
    wizard.preferences({'python': True})
    wizard.preferences({'java' : False})
    wizard.execute() 