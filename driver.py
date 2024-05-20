#this file exists, so it is very easy to call the functions, with examples. 
from matchid_to_csv import convert
from get_match_ids import bfs_get_match_ids
YOUR_API_KEY = "" #must enter to make any call


AMOUNT = 1 #specify how many match ids you want to get
START =  "NA1_4995853430" #A MatchId to start the search on
ALREADY = { "NA1_4995853430":1} #lists of match_id we already have, prevents duplicates, and infinite loops
match_ids = bfs_get_match_ids(AMOUNT, START, ALREADY, YOUR_API_KEY)


CSV_FILE_NAME = "sample_output.csv" #enter the csv file you want to append to
convert(match_ids, YOUR_API_KEY, CSV_FILE_NAME)
