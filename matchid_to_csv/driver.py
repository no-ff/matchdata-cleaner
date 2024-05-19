#this file exists, so it is very easy to call the functions, with examples. 
from matchid_to_csv import convert

"""
convert(match_ids, api_key, csv)

Arguments:
    match_ids: List of match ids
    api_key: your riot api key that you retrieve in the development portal
    csv: route/ filename to the csv file you will append the data to

What it does:
    goes through the match_ids, and appends new lines to the csv file of the following format,
    Team1Top,Team1Jg,Team1Mid,Team1ADC,Team1sup,Team2Top,Team2Jg,Team2Mid,Team2ADC,Team2sup,goldDiff,winningTeam  
    i.e) "Yasuo,Ekko,Kassadin,Smolder,Pyke,Jax,Amumu,Diana,Jinx,-11483,200"
    
    If goldDiff > 0, then team1 has that goldDiff gold advantage.
    If goldDiff < 0, then team2 has that |goldDiff| gold advantage.
"""

#Example Usage
#the following call was made to create all data of sample_oupput with sample_data as input
import sample_data
input = sample_data.input
convert(input, "RGAPI-ea2182cf-cda1-41ad-8ac5-8b599474ae92", "matchid_to_csv/sample_output.csv")
