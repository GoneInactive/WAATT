import json

class UserManager:
    def __init__(self):
        pass

    def create_user(name, number, value):
        dir = "/Data/Accounts/" + str(number) + ".json"
        number = int(number)
        value = float(value)

        print("Checking for account nunber repeat...")
        try:
            with open(dir, "r") as f:
                f.readlines()
            print("")
            print("!ERROR! users/UserManager.py --> UserManager.create_user(): An account with number id {number} already exists.")
            print("")
        except FileNotFoundError:
            print(dir)
            print("Passes. Creating New Account...")

            data = {
                    "Account_name": name,
                    "Account_number": number,
                    "Initial_value": value,
                    "Current_value": value
                    }

            with open(dir, 'w') as fp:
                json.dump(data, fp)

            with open("Data/accountnumbers.txt", "a") as myfile:
                myfile.write(str(number))

            print("Done.")
        except Exception as e:
            print(f"!ERROR! users/UserManager.py --> UserManager.create_user():{e}")
