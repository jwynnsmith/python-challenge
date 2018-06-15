import os
import csv

#Set filepath and import csv file
#filepath = os.path.join('C:\\','Homework','PyPoll','raw_data','election_data_2.csv')
#input_file = input("Enter the name of the CSV file(s) you will like to process one at a time? ")
#filepath = os.path.join(input_file)
csvpath = os.path.join("raw_data", "election_data_1.csv")
with open(csvpath, newline = '') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    header = next(csvdata)
    
    #Create lists
    voterid = []
    county = []
    candidates = []
    names_of_candidates = []
    
    txt_elect = open("Election_Results_1.txt", "w")
    txt_elect.write("Election Results 1\n")
    txt_elect.write("-----------------------------------------------\n")
    

    #Run a for loop for every x of data
    for x in csvdata:
        voterid.append(x[0])
        county.append(x[1])
        candidates.append(x[2])
    
    #Create variables. 
    voters_list = len(voterid)
    candidates_list = set(candidates) #Set function is used to identify each unique candidate
    txt_elect.write(f"The Total number of votes cast: {voters_list}\n")
    txt_elect.write("------------------------------------------------\n")

    print("Election Results")
    print("-----------------------------------------------")
    print(f"The Total number of votes cast: {voters_list}")
    print("------------------------------------------------")

  
    for x in candidates_list:
        names_of_candidates.append(x)

    #Create a dictionary for the candidates
    dict_of_candidates = {}
    candidates_count = 0
    for x in names_of_candidates:
        candidate_name = str(names_of_candidates[candidates_count])
        votes = int(candidates.count(candidate_name))
        vote_share = round(votes/voters_list * 100, 2)
        dict_of_candidates.update({candidate_name: votes})
        print(f"{candidate_name}: {vote_share}%  ({votes})")
        txt_elect.write(f"{candidate_name}: {vote_share}%  ({votes})\n")
        candidates_count = candidates_count + 1

    

    winner = max(dict_of_candidates, key=lambda key: dict_of_candidates[key])
    
    print("--------------------")
    print(f"Winner: {winner}")
    print("--------------------")


#txt_elect.write(f"{candidate_name}: {vote_share}%  ({votes})\n")
txt_elect.write("--------------------\n")
txt_elect.write(f"Winner: {winner}\n")
txt_elect.write("--------------------\n")
txt_elect.close()