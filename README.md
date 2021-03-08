# Election_Analysis

##Overview of Election Audit
To complete the election audit of a congressional election, python is used to read data from a .csv file and perfom the following tasks:

* Get the total numbers of votes cast.
* Get a list of candidates who received votes.
* Compute the total number of votes for each candidate.
* Calculate the percentage of votes each candidate won.
* Determine the winner of the election based on popular vote. 

## Election-Audit Results
The output of the analysis below summarizes the results:

![Analysis results terminal](https://user-images.githubusercontent.com/79415699/110260240-4e845d80-7f79-11eb-826e-1f6966aa5099.PNG)

* 369,711 votes were cast in the election.

* The distribution based on counties is the following:
- Jefferson received 38,855 votes (10.5% of total votes cast)
- Denver received 306,055 votes (82.8% of total votes cast)
- Arapahoe received 24,801 votes (6.7% of total votes cast)

* Based on the % above, Denver was the county with the largest number of votes. 

* As for the candidates: 
- Charles Casper received 85,213 votes putting him at 23.0% of total number of votes. 
- Diana DeGette received 272,892 votes, putting her at 73.8%
- Raymon Anthony Doane received 11,606 votes, placing him at 3.1%. 

* Based on the % above, the winnder of the election was Diana DeGette. 

## Election-Audit Summary
This script was written to iterate through a list of ballots for candidates in the electino. With some modification, this script can be used for any other election in several other districts or generally any application that requires going through thousands of rows of data to get total counts of categories, and break them down based on percentages or another category like location. Some examples would be analyzing student grades data based on school or state or year.
