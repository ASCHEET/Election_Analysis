# Election_Analysis

## Python and VSCode was used to write a script for helping Seth and Tom submit the election audit results to the election commission. However; the election commission has requested some additional data to complete the audit:

## The voter turnout for each county is shown using the following code: 
### ![Fig 1 - VS code of total_votes] ()
### The code looks at the provided .csv file and with the total_votes set to zero prior to the 'for' loop, the 'for' loop interates between all rows and counts (adds 1 of each row) for all 'rows' = votes cast in the election.
### The votes are displayed in the python terminal using the command print(election_results, end="") from Figure 2, and an example of the terminal output is 
### ![Fig 2 - VS Code of Python Terminal and text (.txt_ file output commands. ![Fig 3 - Python Termingal of Total Votes] () ![Fig 4 - txt_file_output] ()
The percentage of votes from each county out of the total count
### The code utilized to calcuate percentage of votes cast per county is displayed below.  It requires separating each candidate_votes by candiate_name and totaling those separately.  It is important to know this calculation only calculates percentages based on the votes that were cast.  It is not indicative of the results based on registered voters vs. voter turnout.  
### ![Fig 5 - candidate percentages ] ()
The county with the highest turnout
### County with highest turnout 'winning_county_info' in the code and displayed in Fig 6 below.  The county with the largest county turnout was Denver County with over 82% of the vote.  This code could be modified to highlight some descrepincies regarding voter irregularities.  For example, it is unknown why the magority of the voter turnout is from Denver county and so little is from Arapahoe and Jefferson Counties.  These results could indicate incomplete voter collection or potential fraud.  At a minimum, questions could be asked and to the discrepincy.
### ![Fig 6 - VS Code of county results] () 
