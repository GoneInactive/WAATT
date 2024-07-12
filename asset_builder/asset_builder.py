import os
import csv
from tabulate import tabulate

class AssetBuilder:
    def __init__(self):
        return
    
    def __run__(self):
        print('Starting Asset Builder Tool')
        if input('Do you want to load a saved build? Enter y/n: ').upper() == 'Y':
            self.load_build()
            if input('Do you want to edit this build?').upper() == 'Y':
                self.edit_build()
        else:
            current_build = self.create_build()
            print('Do you want to save this build?')
            if input('Enter y/n: ').upper() == 'Y':
                self.save_build(current_build)

    def new_asset_build(self):
        return
    
    def load_save_build(self):
        return

    def create_build(self):
        print('Creating new asset build')
        assets = []
        total_percent = 0

        while True:
            while True:
                asset_name = input('Enter asset name: ')
                if asset_name:
                    break
                else:
                    print('Asset name cannot be empty.')

            while True:
                asset_percent = input('Enter package percent breakdown (%): ')
                try:
                    asset_percent = float(asset_percent)
                    if 0 <= asset_percent <= 100:
                        if total_percent + asset_percent <= 100:
                            break
                        else:
                            print(f'Total package percent cannot exceed 100%. Current total: {total_percent}%')
                    else:
                        print('Package percent must be between 0 and 100.')
                except ValueError:
                    print('Please enter a valid number for package percent.')

            assets.append((asset_name, asset_percent))
            total_percent += asset_percent

            print(f'Current total percent: {total_percent}%')

            if total_percent == 100:
                print('Total package percent has reached 100%. No more assets can be added.')
                break

        # Format and print the table
        print('\nFinal Asset Breakdown:')
        print(tabulate(assets, headers=['Asset Name', 'Package Percent'], tablefmt='grid'))

        # Save the asset build to a CSV file

        return assets

    def save_build(self,assets):
        # Ensure the /saves/ directory exists
        if not os.path.exists('saves'):
            os.makedirs('saves')

        # Define the file path
        # file_path = '/saves/asset_build.csv'
        file_path = 'asset_builder/saves/'+input('Enter file name: ') + '.csv'
        # Write the assets to a CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Asset Name', 'Package Percent'])
            for asset in assets:
                writer.writerow(asset)

        print(f'Asset build has been saved to {file_path}')

    
    def load_build(self):
        # Define the file path
        # file_path = 'saves/asset_build.csv'
        file_path = 'asset_builder/saves/'+input('Enter file name: ') + '.csv'

        # Check if the file exists
        if not os.path.exists(file_path):
            print(f'No saved asset build found at {file_path}')
            return

        # Read the assets from the CSV file
        assets = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                asset_name, asset_percent = row
                assets.append((asset_name, float(asset_percent)))

        # Print the loaded assets in a formatted table
        print('\nLoaded Asset Breakdown:')
        print(tabulate(assets, headers=['Asset Name', 'Package Percent'], tablefmt='grid'))

        return assets
    
    def edit_build(self):
        # Load the existing asset build
        assets = self.load_build()
        if not assets:
            return

        total_percent = sum(asset[1] for asset in assets)

        while True:
            print('\nCurrent Asset Breakdown:')
            print(tabulate(assets, headers=['Asset Name', 'Package Percent'], tablefmt='grid'))
            print(f'Current total percent: {total_percent}%')

            edit_option = input('Do you want to add, edit, or delete an asset? (add/edit/delete): ').lower()

            if edit_option == 'add':
                while True:
                    asset_name = input('Enter asset name: ')
                    if asset_name:
                        break
                    else:
                        print('Asset name cannot be empty.')

                while True:
                    asset_percent = input('Enter package percent breakdown (%): ')
                    try:
                        asset_percent = float(asset_percent)
                        if 0 <= asset_percent <= 100:
                            if total_percent + asset_percent <= 100:
                                break
                            else:
                                print(f'Total package percent cannot exceed 100%. Current total: {total_percent}%')
                        else:
                            print('Package percent must be between 0 and 100.')
                    except ValueError:
                        print('Please enter a valid number for package percent.')

                assets.append((asset_name, asset_percent))
                total_percent += asset_percent

            elif edit_option == 'edit':
                asset_name = input('Enter the asset name to edit: ')
                for i, asset in enumerate(assets):
                    if asset[0] == asset_name:
                        while True:
                            new_percent = input(f'Enter new package percent for {asset_name} (%): ')
                            try:
                                new_percent = float(new_percent)
                                if 0 <= new_percent <= 100:
                                    if total_percent - asset[1] + new_percent <= 100:
                                        total_percent = total_percent - asset[1] + new_percent
                                        assets[i] = (asset_name, new_percent)
                                        break
                                    else:
                                        print(f'Total package percent cannot exceed 100%. Current total: {total_percent}%')
                                else:
                                    print('Package percent must be between 0 and 100.')
                            except ValueError:
                                print('Please enter a valid number for package percent.')
                        break
                else:
                    print(f'Asset {asset_name} not found.')

            elif edit_option == 'delete':
                asset_name = input('Enter the asset name to delete: ')
                for i, asset in enumerate(assets):
                    if asset[0] == asset_name:
                        total_percent -= asset[1]
                        assets.pop(i)
                        break
                else:
                    print(f'Asset {asset_name} not found.')

            else:
                print('Invalid option.')

            if total_percent == 100:
                print('Total package percent has reached 100%. No more changes can be made.')
                break

            if input('Do you want to make another change? (Y/N): ').upper() == 'N':
                break

        # Save the updated asset build to the CSV file
        self.save_build(assets)

