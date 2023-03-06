import pandas as pd
from prettytable import PrettyTable

'''
pandas.read_csv() function to read the CSV file into a pandas DataFrame. 
We then use boolean indexing to filter the DataFrame to only include rows where the Location column matches 
the specified location. 
Finally, we use the to_dict() method to convert the resulting DataFrame to a list of dictionaries.
'''

def search_location(file_path, location):
    df = pd.read_csv(file_path, delimiter=',')
    results = df[df['Location'] == location][['Username', 'Location']].to_dict('records')
    return results

def format_results(results):
    table = PrettyTable()
    table.field_names = ['Username', 'Location']
    for row in results:
        table.add_row([row['Username'], row['Location']])
    return table

def write_to_log(results, log_file_path):
    df = pd.DataFrame(results)
    df.to_csv(log_file_path, mode='w', header=not log_file_path.exists(), index=False)

def main():
    file_path = '/home/dave/Projects/stuff/python/tests/sample.csv'
    location = input("Enter a location to search for: ")
    results = search_location(file_path, location)
    table = format_results(results)
    print(table)
    log_file_path = 'log.csv'
    if results:
        #write_to_log(results, log_file_path)
        print("Results written to log file: " + log_file_path)

if __name__ == '__main__':
    main()