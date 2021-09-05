# The data we need to receive
import csv
import os

file_to_load = os.path.join('election_results.csv')
file_to_save = os.path.join("analysis", "election_results.txt")

with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the csv file
    # for row in file_reader:
        # for i in range(len(row)):
        # print(row[0])

# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write to the data file
# with open(file_to_save, "w") as txt_file:

    # txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
# Write some data to the .txt file


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on teh popular vote.