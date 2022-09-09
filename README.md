# Election_Analysis

## Overview of Project
This project is to perform analysis on election data to find out the following information for the election commission:

  * Total Votes in the election

  * Total vote count and percentage of votes for each county

  * The county with the highest turnout
    
  * Total vote count and percentage of the total votes for each candidate
    
  * The winner of the election, winning vote count, and winning percentage of votes
    
    
    
## Election Audit Results
  * Total votes: 369,711

  * County Votes:
    * Jefferson: 10.5% (38,855)
    * Denver: 82.8% (306,055)
    * Arapahoe: 6.7% (24,801)

  * Largest county turnout: Denver

  * Candidate votes:
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana DeGette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606)

  * Winner:
    * Winner: Diana DeGette
    * Winning Vote Count: 272,892
    * Winning Percentage: 73.8%

  
![Election Audit Results](https://user-images.githubusercontent.com/110554264/189426725-9b87baa9-20da-4750-94a3-b624d320591c.png)

## Election Audit Summary
As the script reads data from an election dataset in .csv format and write the election audit results to the .txt file, it can be used for any election to analyze election audit results. However, the script should be modified in the following cases:

  * The election dataset (.csv file) contains a different set of columns than the one we use in this script. In this case, the script will be modified to read election data correctly.

  * Additional data requested by the election commission other than those listed in Election Audit Results section above. In this case, the script will be modified to analyze additional data and save those requested information to the output file (.txt).

       


