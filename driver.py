# This file exists, so it is very easy to call the functions, with examples.
from matchid_to_csv import convert
from get_match_ids import bfs_get_match_ids
from utils import convert_txt_to_list, split_file_and_write_to_files, remove_duplicates

# Enter your API key here.
YOUR_API_KEY = "RGAPI-ebe2abbb-ed67-4e96-bc93-29e11fef4d51"

#Available functions:
# convert_txt_to_list(file_name)
# split_file_and_write_to_files(input_file, file1, file2)
# remove_duplicates(input_file_path, output_file_path)
# convert(match_ids, api_key, file_name)
# bfs_get_match_ids(amount, start, already, api_key)

# Example usage:
MATCH_IDS = convert_txt_to_list("teddy.txt")
convert(MATCH_IDS, YOUR_API_KEY, "teddy.csv")




    
