ETL-project-G11 Final Report

Presidential Candidate Campaign Spending and Polling Data

What data sources you chose, and why?
1.	Fivethirtyeight.com:- Readily accessible dataset with all the presidential candidates’ polling number from major polling providers by state with the ability to download into CVS
2.	OpenFEC API dataset (https://api.open.fec.gov/developers/#/) as it had the detailed information about candidate expenditure by state and disbursement type with free API keys that allowed us access to download bulk data for each candidate
3.	Census.gov   & Data World: We used Data world and US. Census Data sources to utilize state and population information for our project. The data was updated in 2019 which is the most recent population statistics for the US population. We used pandas to extract and clean these csv files.

Detailing the process of the extraction, transformation, and loading steps and explain why you performed the types of transformations you did: 
Polling Data
The polling data was downloaded from fivethirtyeight.com website as a CSV file.  This was then opened in the Jupyter lab as a Pandas Dataframe. Next, we performed the data cleaning in Pandas by keeping only the columns needed for our project as shown in the Jupyter lab. Since we were only interested in Trump and Biden data, a conditional argument was created.  Next, we checked to see if there were null values in our polling data. There were 4,005 rows out of 10,365 rows with null data. Since we are interested in state polling data in relation to our financial data by state, we dropped all rows that contain null values in the state column. We now have 6,761 rows without null data in relation to the state column.  We were ok if the “methodology” and “fte_grade” columns contained null data. Since we used SQL Postgres database-- a relational database--we created a committee ID column in the polling table in order to relate candidate spending and polling data in the schema. Next, a connection was made to the local database in Postgres. Four tables were created: States', 'Candidates', 'Candidate_Spending', 'Polls'.  The data was then transferred into SQL successfully.

OpenFEC API (Candidate Spending and Candidates Data)
Extraction:
Extracted campaign committee spend data for candidates Trump and Biden passing the committee_id, per page count, and page numbers as parameters. A for loop was used to make the calls 261 times for Trump data and 330 for Biden data due to a maximum limit of 100 records per page per call. Upon completion of the API calls, data was loaded into two lists, one for each candidate.
Data Transformation for committee (Candidates) data
From each candidate list, using a for loop query, we retained key attributes describing the campaign committee into a dictionary for each candidate. A new merge function to merge both dictionaries together was defined and applied to create one dictionary which was later converted to a pandas data frame “committee”.

Data Transformation for Candidate Spending Data
Used a multi-for loop to create individual lists of dictionaries for each attribute for the Candidates_Spending table and appended each list of dictionary into an empty dictionary for each candidate. This set the stage for creating a pandas dataframe for each candidate. Both pandas dataframe were consolidated into one dataframe. Given that we were interested in only data for US States that were eligible to vote in a presidential election, we used to drop function to remove the non-applicable states and then reset index with the resulting “spending” data frame.
Load
Using sqlalchemy engine connection, spending and the committee data frames were loaded into Postgres SQL tables called “Candidates” and “Candidate_Spending”. The schemas for these tables had been pre-created in Postgres SQL prior to the load.

States Data
The states population data was downloaded from Census.gov in a csv file and the states attribute data was downloaded from Dataworld. Dropped all columns from State and Abbreviation dataset that had unnecessary columns such as region, county and division names.Sorted State and Abbreviation. Saved data into a Pandas DataFrame and organized by State.Dropped all State and Population dataset that had unnecessary columns such as region, county and division names.Saved data into a Pandas DataFrame and merged into one csv file and name the file state.pop.csv. Renamed columns to make them consistent.

Why (Postgress SQL) Relational Database?
The data type we chose for this project are all structured data and are related. In addition, joining the tables will allow us to provide meaningful insights and analyses beyond what is reflected in each individual table as demonstrated by some of the use cases outlined below.


Hypothetical use case(s) for your Database
1.	Is there a correlation between campaign spending and the state population? i.e. are candidates more likely to spend more in states with higher populations?
2.	Is there a correlation between total campaign spending by state and polling numbers by the state? How does spend impact polling numbers?
3.	Is there a correlation between the type of spend (e.g. Advertising) and poll polling numbers? For example, if a candidate spends more on advertising/media, etc. what impact if any, is there on the poll responses?
4.	Do candidates spend more in battleground states? If so, do they spend more in battleground states the closer it gets to the election date?

                                             