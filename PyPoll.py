from asyncore import write
import csv
import os

# Assign the input & output data file
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = [] #list of candidates
candidate_votes = {} # number of votes of each candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the input data file and perform analysis
with open(file_to_load) as election_data:

    # Skip the header row
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    # loop though all rows
    for row in file_reader:
        # increase number of votes
        total_votes = total_votes + 1

        # get the list of candidates
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # track the candidate's vote count
        candidate_votes[candidate_name] += 1

# Open the output file to write data to the file.
with open(file_to_save, 'w') as txt_file:
    # write the total votes
    election_results = (
        f"Election Results\n"
    f"----------------------------------\n"
    f"Total votes: {total_votes:,}\n"
    f"----------------------------------\n"
    )
    txt_file.write(election_results)

    # calculate and write number % percentages of votes for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)

        # determine the winner
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage   
            
    # write the winner
    winning_candidate_summary = (    
            f"---------------------------\n"    
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count:,}\n"
            f"Winning percentage: {winning_percentage:.1f}%\n"
            f"------------------------------------")
    txt_file.write(winning_candidate_summary)

