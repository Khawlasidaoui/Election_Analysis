#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.


# import datetime as dt
# now=dt.datetime.now()
# print("the time right now is",now)

# DEPENDENCIES

import csv
import os

#INPUT

#Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources","election_results.csv")
#Open election results and the read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    #skip header row --> prints as a list
    headers=next(file_reader)
    print(headers)



     

    











# OUTPUT

#Create a filename variabe to a direct or indirect path to the file
file_to_save=os.path.join("analysis","election_analysis.txt")
#use open() with "w" to write to file
# outfile=open(file_to_save,"w")
# # write data to output file:
# outfile.write("Hello World")
# #close file
# outfile.close()
#use with statement to open and writ to output file:
with open(file_to_save,"w") as txt_file:
    #Write to file
    txt_file.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")

#Notes:
# file_to_save is the path and acutal document name in the folder
# txt_file is the variable in python that we use to write to file_to_save.


    
  
