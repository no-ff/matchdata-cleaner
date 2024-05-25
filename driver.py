# This file exists, so it is very easy to call the functions, with examples. 
from matchid_to_csv import convert
from get_match_ids import bfs_get_match_ids
YOUR_API_KEY = "RGAPI-efdc536a-6a0f-4b00-8e8d-853f3011d1d4"
# Must enter to make any call.


def convert_txt_to_list(file_name):
    with open(file_name, "r") as this:
        data = this.readlines()
    new = []
    for i in data:
        new.append(i[:-1])
    return new


"""
AMOUNT = 100000 # Specify how many match ids you want to get.
START =  "NA1_5005110386" #A MatchId to start the search on. Currently a Challenger match.
ALREADY = { "NA1_5005110386":1} # Lists of match_id we already have, prevents duplicates, and infinite loops.
match_ids = bfs_get_match_ids(AMOUNT, START, ALREADY, YOUR_API_KEY)
"""


CSV_FILE_NAME = "output1.csv" # Enter the csv file you want to append to.
INPUT = convert_txt_to_list("input1.txt")
convert(INPUT, YOUR_API_KEY, CSV_FILE_NAME)


def split_list_and_write_to_files(input_list, file1='input1.txt', file2='input2.txt'):
    # Calculate the midpoint of the list.
    mid_index = len(input_list) // 2

    # Split the list into two halves.
    first_half = input_list[:mid_index]
    second_half = input_list[mid_index:]

    # Write the first half to the first file.
    with open(file1, 'w') as f1:
        for item in first_half:
            f1.write(f"{item}")

    # Write the second half to the second file.
    with open(file2, 'w') as f2:
        for item in second_half:
            f2.write(f"{item}")

with open("matchids.txt", "r") as this:
    data = list(set(this.readlines()))   

#split_list_and_write_to_files(data)