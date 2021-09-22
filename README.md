# Election_Analysis

## Python and VSCode was used to write a script for helping Seth and Tom submit the election audit results to the election commission. However; the election commission has requested some additional data to complete the audit:

### The total voter turnout for the election is shown below in Figure 1. 
### ![Fig 1 - VS code of total_votes](https://github.com/ASCHEET/Election_Analysis/blob/main/Resources/total_votes.png?raw=true)
### The code looks at the provided .csv file and with the total_votes set to zero prior to the 'for' loop, the 'for' loop iterates between all rows and counts (adds 1 of each row) for all 'rows' = votes cast in the election.
### Regarding Figure 2 below, there is code showing the ability for python to output results to a text file.  This output is shown later in Figure 6. 
### ![Fig 2 - VS Code of Python Terminal](https://github.com/ASCHEET/Election_Analysis/blob/main/Resources/VS_to_terminal_total_votes.png?raw=true) 
### The total votes are displayed in the python terminal [Figure 3] using the command "print(election_results, end="")" and from the terminal output one can see that 369,711 votes were cast for this election.
### Figure 2 above, shows the per county votes that were cast in the election and an example of the terminal output is shown in Figure 3.

### Figure 3 also shows python export of the data from the python terminal view below. 
### ![Fig 3 - txt_file_output](https://github.com/ASCHEET/Election_Analysis/blob/main/Resources/terminal_total_votes1.png?raw=true)

### The code utilized to calculate percentage of votes cast per county is displayed below.  It requires separating each candidate_votes by candiate_name and totaling those separately.  It is important to know this calculation only calculates percentages based on the votes that were cast.  It is not indicative of the results based on registered voters vs. voter turnout.  
### ![Fig 4 - candidate percentages ](https://github.com/ASCHEET/Election_Analysis/blob/main/Resources/candidate_percentages.png?raw=true) 
### The picture above calculates the winning candidate on the percentages of votes each candidate_name received, then divides by the total_votes cast.

### ![Fig 5 - VS Code of county results](https://github.com/ASCHEET/Election_Analysis/blob/main/Resources/winning_candidate.png?raw=true) 
### The county with highest turnout 'winning_county_info' in the code and displayed in Fig 5 above.  The county with the largest county turnout was Denver County with over 82% of the votes cast being from Denver county.  This code could be modified to highlight some discrepancies regarding voter irregularities.  For example, it is unknown why the majority of the voter turnout is from Denver county and so little is from Arapahoe and Jefferson Counties.  These results could indicate incomplete voter collection or potential fraud.  At a minimum, questions could be asked and to the discrepancy.  The code print(winning_county_info) sends the script to the python terminal while txt_file.write(winning_county_info) sends the results to the text file.
### This code also shows the election results are printed to separate text file call election_analysis_challenge.txt.  
### ![Fig 6 - Text File Output](https://github.com/ASCHEET/Election_Analysis/blob/main/Resources/txt_results.png?raw=true)
