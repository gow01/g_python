#!/usr/bin/env python3

# Initiate code with the necessary imports for different functional use
import json
import numpy as np

# Function definition for handling json streams of data
def json_handler(file):

    # agrs is json files
    # read json file
    with open(file) as json_file:

        # parse json data
        # provide full file path
        data = json.load(json_file)

    # Return json as dictionary to be used
    return data


# Function definition for using input name of staff member to search through dict from json file
def input(staff):

    print(staff)
    selected_staff_req = []
    dd = []
    cc = []
    bb = []
    places_to_visit = []
    print('------------------------------------------------------')
    # Parse args to function
    # Loop through json_handler dict to find key value pair for input
    # Parse the json file locations to function
    users_json = 'C:\\Users\\gerar\\source\\repos\\master\\g_python\\python_tdd\\users.json'
    venues_json = 'C:\\Users\\gerar\\source\\repos\\master\\g_python\\python_tdd\\venues.json'

    # Extract dictionaries from json data
    users_data = json_handler(users_json)
    venues_data = json_handler(venues_json)

    # Loop through dictionary of users data from json files
    for item in users_data:
        # Loop through staff members inputted
        for staff_members in staff:

            # Extract first value of dictionary
            values = item.values()
            value_iter = iter(values)
            first_value = next(value_iter)

            # Compare first value with inputted staff members
            if first_value == staff_members:
                selected_staff_req.append(item)
    print(selected_staff_req)
    print('------------------------------------------------------')
    
    # Looping through venues to extract places to visit
    for item in venues_data:

        # Extracting second values of wont eats to make comparison
        venues_values = item.values()
        venues_values_iter = iter(venues_values)
        first_venues_value = next(venues_values_iter)
        second_venues_value = next(venues_values_iter)
        dd.append(second_venues_value)
        #print(second_venues_value)
        #print('---------------------------------------------------------')
        # Loop through selected staff requirements
    for each_staff_req in selected_staff_req:

        # Extract second value from selected staff req
        values = each_staff_req.values()
        value_iter = iter(values)
        first_value = next(value_iter)
        second_value = next(value_iter)
        cc.append(second_value)
        #print(second_value)
    print(dd)
    print('--------------------------------------------------')
    print(cc) 
    print('--------------------------------------------------')

    # Next step would be to compare the matrices and parse the difference on to determine place to  visit 

    # After this I will again compare the matrices to determine which places to not visit
            
    # This can then be appended using the necessary text to form a list of dictionary
    
    # Then use the list of dictionaries to dump into a json file to output at the end of the script


def main(): # main function
    print("Welcome to Staff Outing Decider")
    #input(json_handler())

if __name__ == '__main__':
    main()