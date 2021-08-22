# Election Analysis

## Project Overview
The Colorado election committee has requested additional information on top of the recent analysis completed 
for them in regards to the election audit.  The board committee would now also like to determine the following:
1.  The voter turnout for each county
2.  The percentage of votes from each county out of the total count
3.  The county with the highest turn out

The challenge is to use Python on the provided Election_results.csv file to calculate the desired statistics and print out the results to the terminal as well as in a text file that can be provided to the election committee.

#### Background
Colorado Board of Elections employees, Seth and Tom, requested an analysis of election results in 
conjunction with an audit that is being done of a recent local congressional election.  The audit originally requested
the following information:

1.  The Total number of Votes cast
2.  A Complete list of candidates who received votes
3.  The total number of votes each candidate received
4.  What is the percentage of votes each candidate won
5.  Who is the winner of the election by the popular vote

After reviewing this information, the election committee has requested additional information with regards to the individual county showings.  The challenge is to enhance the starter code used to develop the initial audit information to also include the additional requests.    

#### Resources provided
- Data Source:  election_results.csv  To see data file click ![Here]([election_results.csv](https://github.com/AswithaB/Election_Analysis/files/7026566/election_results.csv)
- Software:  Python 3.8.8, Visual Studio code

## Election-Audit Results
* THE NUMBER OF TOTAL VOTES CAST IN THIS CONGRESSIONAL ELECTION
>In order to calculate the total votes cast in the election, we used a `for` loop coupled with a `counter variable` that increases each time the `for` loop goes through the rows of data. 
The results of this loop code shows the total votes cast as follows:

![total votes](https://user-images.githubusercontent.com/85645485/130341708-8455991b-4cea-4c63-95e0-408c5a18b24f.PNG)

* BREAKDOWN OF VOTES BY COUNTY AND PERCENTAGE BY COUNTY
>In order to calculate the breakdown of votes by county, a dictionary and list are created to keep county names as the key and accumulated votes by county as the value:

![county code 1](https://user-images.githubusercontent.com/85645485/130341702-85f55b5a-2681-4975-b068-56a5f5a2d742.PNG)
 >Next while still in the `for` loop looking at all the records, when a new county name is encountered it is `append`ed to the list
 
 ![county code 2](https://user-images.githubusercontent.com/85645485/130341703-9c7e3904-fa65-46f7-b126-20b8538bf6ae.PNG)
 
 >Finally a new variable to track votes by county is created and increased each time the county name shows up in the data file.
 The percentage of total votes for each county is now easy to calculate by dividing the total of the county by the overall total. 
 
 ![county percentage](https://user-images.githubusercontent.com/85645485/130341704-68fc296d-19c4-4ec1-a89a-97e52b7d3a3f.PNG)
 
 >The final results by county are as follows:
 
 ![county votes](https://user-images.githubusercontent.com/85645485/130341705-1825b450-406a-42f9-856a-8102773ff567.PNG)
 
 * THE COUNTY WITH THE LARGEST VOTES
  >To identify the winning county, an `if statement` is used with a comparison `variable` within the `for` loop to check and see if the accumulated amount of votes in the `dictionary` is bigger than the prior winning county count and if so, replace the winning county count until the whole dataset has been processed.  This comparison variable is initiated to 0 at the beginning of the code. 
  
  ![winning county](https://user-images.githubusercontent.com/85645485/130341711-355241df-ac6a-48ab-8931-8e389baf9679.PNG)
  
  >The result of this program gives us the county with the largest turnout: 
  
  ![largest county](https://user-images.githubusercontent.com/85645485/130341707-ce50c529-0651-40f3-9d2c-b169d56a6d89.PNG)
  
  * THE CANDIDATE VOTES AND PERCENTAGE
  > Similar logic is used to determine the votes for each candidate and the percentage of the total votes each has received as used in the county analysis.  The results of the candidate vote count are as follows:
  
  ![candidate votes](https://user-images.githubusercontent.com/85645485/130341701-4dd5cc41-76a5-43d5-8e39-9547666d9b75.PNG)
  
  * THE WINNING CANDIDATE
>Given the prior calculations, it is a simple matter to determine the winner of the election.  Similar logic to finding the county with the most votes is used to determine the candidate with the most votes as shown in the code below:
  
  ![winner code](https://user-images.githubusercontent.com/85645485/130341709-1dc4d667-8bce-4e67-9038-27efb5d25d5d.PNG)
  
 >Finally our winner and statistics are as follows:
 
 ![winner](https://user-images.githubusercontent.com/85645485/130341710-15608329-73d4-45df-a1b3-6ce622a8b211.PNG)
 
 ## ELECTION AUDIT SUMMARY
 
The script provided for this audit is able to calculate the total votes, votes by county and candidate and the percentage of total votes these account for.  The script can be used on any file of undetermined length with similar data elements.  With some modification, the script could also produce statistics of interest such as:
* The votes by candidate by county - the election commission could then see which candidate won in each county and not just the overall winner
* The script could also calculate the candidate winning the most counties which may be different than the overall popular vote

The code for this analysis can be found ![here:](https://github.com/xactuary/PyPoll-Python-Challenge/blob/master/PyPoll_Challenge.py)

A text file of the results of the analysis can be found ![here:](https://github.com/xactuary/PyPoll-Python-Challenge/blob/master/Analysis/election_analysis.txt)

