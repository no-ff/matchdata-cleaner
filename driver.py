#this file exists, so it is very easy to call the functions, with examples. 
from get_match_ids import bfs_get_match_ids

YOUR_API_KEY = "RGAPI-4ffbc243-e506-4653-9f9c-1fc10db5c39e" #must enter to make any call
CSV_FILE_NAME = "sample_output.csv" #enter the csv file you want to append to
AMOUNT = 1000 #specify how many match ids you want to get
START = "NA1_4998514481" #A MatchId to start the search on
ALREADY = {"NA1_4998514481":1} #lists of match_id we already have, prevents duplicates, and infinite loops
match_ids = bfs_get_match_ids(AMOUNT, START, ALREADY, YOUR_API_KEY, CSV_FILE_NAME)


