#Add dependencies
import os
import csv
#assign a variable to the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Create a file name variable for output file
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Initiate counter variable to 0 comes before openign the file because 
# needs to be reset to 0 everytime we open the file
total_votes=0

#initiate candidate list
candidate_options = [] 

#Declare an empty dictionary
candidate_votes={}

#Winning Candidate and Winning count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0.0

# open the election results file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print header row
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        #count 1 for each row to count total votes
        total_votes += 1

        #print the candidate name for each row
        candidate_name = row[2]

        
        if candidate_name not in candidate_options:
            #add variable candidate name to end of list
            candidate_options.append(candidate_name)

            #begin tracking that candidates vote count
            candidate_votes[candidate_name]=0

        # add a vote to the candidates count inside for loop so go through each row
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results) 

    #Determine the percentage of votes for each candidate by looping through 
    #Iterate through candidate list


    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate for each name in candidate votes dictionary
        votes = candidate_votes[candidate_name]
        #Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100

        #print out each dandidate's name, vote coutna nd percnet to the terminal
    #   print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)


        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    #print(winning_candidate_summary)

    











