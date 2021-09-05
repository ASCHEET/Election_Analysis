# The data we need to receive
import csv

with open('election_results.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
for row in csv_reader: 
      print(csv_reader)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on teh popular vote.