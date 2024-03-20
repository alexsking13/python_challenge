import csv
import os

# Define the path to the input file
election_file = r"C:\Users\Alex\Documents\python_challenge\PyPoll\Resources\election_data.csv"

# Variables
total_votes = 0
candidate_votes = {}
winner = str()
winner_votes = 0

# Read CSV file
with open(election_file) as election_csv:
    election_reader = csv.reader(election_csv)
    csv_header = next(election_reader)  # Read the header and move to the next line

    # Loop through each row
    for row in election_reader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes for each candidate
candidate_percentages = {}
for candidate in candidate_votes:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    candidate_percentages[candidate] = percentage

# Determine the winner
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Prepare analysis text
analysis_text = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate in candidate_votes:
    analysis_text = analysis_text + f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"
analysis_text = analysis_text + (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print results to the terminal
print(analysis_text)

# Export results to a text file
folder_path=r"C:\Users\Alex\Documents\python_challenge\PyPoll\Analysis"
output_file = "election_results.txt"
file_path=os.path.join(folder_path,output_file)
with open(file_path, 'w') as f:
    f.write(analysis_text)