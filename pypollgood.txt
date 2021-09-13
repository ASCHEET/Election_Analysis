# The data we need to receive
import csv
import os

file_to_load = os.path.join('election_results.csv')
file_to_save = os.path.join("analysis", "election_results.txt")

# 1. Initialize the total vote counter to zero
total_votes = 0
# Candidate Options and candidate votes

candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    # print(headers)
    

# 1. The total number of votes cast
    # Print each row in the csv file
    for row in file_reader:
        # for i in range(len(row)):
        # print(row)
        total_votes += 1
# 3. Print the total votes.
        # print(total_votes)

# Create a filename variable to a direct or indirect path to the file.
# 2. A complete list of candidates who received votes
        
        candidate_name = row[2]
        county_name = row[1]
        print(county_name)
# If the candidate doesn't match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\n"
        f"Election Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
# Print the candidate vote dictionary            
#print(candidate_votes)
# Using the open() function with the "w" mode we will write to the data file

# Write some data to the .txt file

# 3. The percentage of votes each candidate won
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

    # 4. The total number of votes each candidate won
# Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_persent = 
        # vote percentage.
            winning_count = votes
            winning_percentage = vote_percentage
    # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
# 5. The winner of the election based on teh popular vote.
    winning_candidate_summary = (
        f"-------------------\n"
        f"            Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)    
    txt_file.write(winning_candidate_summary)