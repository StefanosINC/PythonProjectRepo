#########*******************************########################
# **** As a user i would like to choose a directory and see all the files in there that are in CSV*****
# **** As a user I would like to choose that file and turn it into a JSON File. into a directory of my choosing ******
# **** As a user I would like download that fil
import os
import csv 
import json


def CSV_TO_JSON(Csv_File): 
    try:
            request_json_file = input('New JSON File you want to create')
            if request_json_file.endswith('.json'):
                AskForValidDirectory = input('Please enter a valid directory')      # open the CSV file and create a JSON file
                if os.path.isdir(AskForValidDirectory):
                    print('Directory exists and is valid')
                else:
                    raise FileNotFoundError('Directory not found')
            else: 
                raise NameError('File did not end with ** .json ** Please label this file correctly.')
            Json_File = os.path.join(AskForValidDirectory, request_json_file)
            with open(Csv_File, 'r') as csv_file, open(Json_File, 'w') as json_file:
        # read the CSV data and convert it to a list of dictionaries
                csv_reader = csv.DictReader(csv_file)
                data = [row for row in csv_reader]
        # write the data to a JSON file
                json.dump(data, json_file)
    except (FileNotFoundError, NameError) as e:
        print(f'Error: {e}')
    except FileExistsError as fee:
        print(f'Error: {fee} - File cannot be opened') 
    
    
#C:\Users\stefa\OneDrive\Desktop\CSVToJSon\CsvToJson

def Main():
    try:
        basepath = input('Enter a directory of your choice')
        if os.path.isdir(basepath): ## If its a directory
            data = os.scandir(basepath)
            ## set a boolean value . If this contains a csv. Leave it to true and continue if false then no CSV files found.
            tempList = []
            for entry in data:
                tempList.append(entry)
            print(tempList)
            for data in tempList:
                if entry.is_file() and entry.name.endswith('.csv') in tempList:
                    csvFile = entry
                    print(csvFile)
                    CSV_TO_JSON(csvFile)
            else:
                raise ValueError(f"No CSV FILE Found In the Directory: {basepath}")
        else:
            raise FileNotFoundError('Directory Path is invalid')
    except(ValueError, FileNotFoundError) as e:
            print(f"Error Message: {e}")

Main()

