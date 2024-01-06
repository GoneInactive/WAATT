import os
import subprocess
import sys

def install_dependencies():
    if not os.path.exists('Data/log/entries.txt'):
        try:

            print('Starting Bootup...')

            with open('dependencies.txt', 'r') as f:
                data = f.readlines()

            # dependencies = [d.strip() for d in data]
            for d in data:
                subprocess.check_call([sys.executable, "-m", "pip", "install", d.strip()])
        except Exception as e:
            raise Exception(f'!ERROR! Unable to correctly install dependencies... Cannot continue with bootup: {e}')
    else:
        print('Dependenice Requirements Met.')

if __name__ == "__main__":
    install_dependencies()
    