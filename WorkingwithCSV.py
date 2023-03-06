import csv
from prettytable import PrettyTable

def search_location(file_path, location):
    results = []
    with open(file_path, mode='r') as myfile:
        data = csv.DictReader(myfile, delimiter=";")
        for row in data:
            if row['Location'] == location:
                results.append({'Username': row['Username'], 'Location'
: row['Location']})
    if not results:
        return "No results found for location: " + location
    else:
        table = PrettyTable()
        table.field_names = ['Username', 'Location']
        for row in results:
            table.add_row([row['Username'], row['Location']])
        return str(table)

def write_to_log(results, log_file_path):
    with open(log_file_path, mode='a', newline='') as log_file:
        fieldnames = ['Username', 'Location']
        writer = csv.DictWriter(log_file, fieldnames=fieldnames)
        for row in results:
            writer.writerow(row)

def main():
    file_path = '/home/dave/Projects/stuff/python/tests/sample.csv'
    location = input("Enter a location to search for: ")
    results = search_location(file_path, location)
    print(results)
    log_file_path = 'log.csv'
    if type(results) == str:
        write_to_log([], log_file_path)
    else:
        write_to_log(results, log_file_path)
        print("Results written to log file: " + log_file_path)

if __name__ == '__main__':
    main()