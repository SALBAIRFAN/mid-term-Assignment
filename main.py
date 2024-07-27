# student1 Salba Irfan
# Student2 Anas Saleem

import json


def input_data():
    city_data = {}

    city_name = input("Enter city name: ")
    
    population = input("Enter population: ")

    literacy_rate = input("Enter literacy rate: ")

    city_data['city_name'] = city_name
    city_data['population'] = population
    city_data['literacy_rate'] = literacy_rate

    return city_data


# function for saving data in JSON file
def save_data_to_json(data, filename='census_data.json'):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data)

    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)

def main():
    while True:
        data = input_data()
        save_data_to_json(data)
        more_data = input("Do you want to add more data? (yes/no): ").strip().lower()
        if more_data != 'yes':
            break

if __name__ == "__main__":
    main()