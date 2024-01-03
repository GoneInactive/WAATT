from users.UserManager import UserManager

class MethodHandler:
    def __init__(self):
        """Initialize the MethodHandler."""
        pass

    def help_txt(self):
        """Implementation for method1."""
        with open('ui/Data/help.txt','r') as f:
            data = f.readlines()
        for d in data:
            print(d)

    def version(self):
        """Implementation for method2."""
        print('Version Hella Beta')


class CommandLineInterface:
    def __init__(self, method_handler=None):
        """
        Initialize the CommandLineInterface.

        Parameters:
            method_handler (MethodHandler): An instance of MethodHandler.
        """
        self.method_handler = MethodHandler()

        self.methods_mapping = {
            'help': self.method_handler.help_txt,
            'version': self.method_handler.version,
            # Add more methods as needed
        }

    def __call__(self, *args, **kwargs):
        # Code to execute when an instance is called
        print("Calling CommandLineInterface with arguments:", args)
        print("Keyword arguments:", kwargs)

    def run(self):
        """
        Run the main loop of the program.

        This method continuously prompts the user for input until the user types 'exit'.
        User input is processed by calling the `process_input` method.

        To exit the program, the user can type 'exit'.
        """
        running = True
        while running:
            user_input = input("\nEnter a command (type 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("\nExiting the program. Goodbye!")
                running = False
            else:
                self.process_input(user_input)

    def process_input(self, user_input):
        """
        Process user input and execute the corresponding method.

        Parameters:
            user_input (str): The user-provided input representing a command.
        """
        try:
            method_to_execute = self.methods_mapping.get(user_input.lower())
            if callable(method_to_execute):
                method_to_execute()
            else:
                print("\nInvalid command. Try again.")

        except Exception as e:
            print('!ERROR! ui/CommandLineInterface.py --> CommandLineInterface.process_input(): ',e)


# Create an instance of the classes and run the program
if __name__ == "__main__":
    CommandLineInterface().run()
