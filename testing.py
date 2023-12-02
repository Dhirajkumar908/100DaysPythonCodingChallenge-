import csv

# Specify the path to the input CSV file
input_csv_path = 'E:/DHIRAJ/100_days_python_challenge/01122023.csv'

# Specify the path to the output CSV file
output_csv_path = 'E:/DHIRAJ/100_days_python_challenge/output.csv'

# Specify the string you want to remove
string_to_remove = "Service Area Code","Phone Numbers","Preferences","Opstype","Phone Type"

# Open the input and output CSV files
with open(input_csv_path, 'r', newline='', encoding='utf-8') as input_file, \
        open(output_csv_path, 'w', newline='', encoding='utf-8') as output_file:

    # Create CSV reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Iterate through the rows in the input CSV file
    for row in csv_reader:
        # Convert the tuple row to a string
        row_str = ','.join(row)
        
        # Check if the specified string is not in the row
        if string_to_remove not in row_str:
            # Write the row to the output CSV file
            csv_writer.writerow(row)

# Optional: Replace the original file with the modified one
# import os
# os.replace(output_csv_path, input_csv_path)
