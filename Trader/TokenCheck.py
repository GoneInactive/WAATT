import os

class TokenCheck():
    def __init__(self):
        self.token_dir = self.__get_token_dir()
        self.pickle_path = os.path.join(self.token_dir, "robinhood.pickle")
        self.username_path = os.path.join(self.token_dir, "robinhood_user.txt")

    def run(self, username):
        try:
            username = username.lower()
        except AttributeError:
            raise Exception('Bad username') from AttributeError
        if not username == self.read_file(self.username_path):
            try:
                self.write_path(self.token_dir)
                self.write_file(self.username_path, username)
                self.delete_file(self.pickle_path)
                print('Username change detected. Removing token.')
            except OSError as ex:
                print('Unable to remove token', ex)

    @staticmethod
    def delete_file(file_path):
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass

    @staticmethod
    def __get_token_dir():
        home_dir = os.path.expanduser("~")
        token_dir = os.path.join(home_dir, ".tokens")
        return token_dir

    @staticmethod
    def write_path(directory):
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass

    @staticmethod
    def write_file(file_path, contents):
        with open(file_path, 'w') as my_file:
            my_file.write(contents)

    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, 'r') as my_file:
                return ''.join([line.strip('\n') for line in my_file])
        except FileNotFoundError:
            return None