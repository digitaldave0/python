import csv

# Create a dictionary to store the column values as keys and a list of column numbers as values
columns = {}

# Open the input file for reading
with open('/home/dave/Projects/stuff/python/tests/sample.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        # Loop through the columns in the row and check for duplicates
        for key, value in row.items():
            # If the value already exists in the dictionary, add the column number to the list
            if value in columns:
                columns[value].append(reader.fieldnames.index(key) + 1)
            else:
                # Otherwise, add the value and column number to the dictionary
                columns[value] = [reader.fieldnames.index(key) + 1]

# Open the output file for writing
with open('output.txt', 'w') as outfile:
    # Loop through the dictionary and write any duplicate values to the output file
    for value, columns_list in columns.items():
        if len(columns_list) > 1:
            outfile.write(f"{value} appears in columns {', '.join(str(c) for c in columns_list)}\n")
