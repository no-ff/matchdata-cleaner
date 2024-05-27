# This file exists, so it is very easy to call the functions, with examples.
from matchid_to_csv import convert
from get_match_ids import bfs_get_match_ids
YOUR_API_KEY = "RGAPI-5b23e179-3710-4cc9-a5b8-dc9325b9e49c"
# Must enter to make any call.


def convert_txt_to_list(file_name):
    with open(file_name, "r") as this:
        data = this.readlines()
    new = []
    for i in data:
        new.append(i[:-1])
    return new


AMOUNT = 1000000  # Specify how many match ids you want to get.
# A MatchId to start the search on. Currently a Challenger match.
START = "NA1_4999862437"# Lists of match_id we already have, prevents duplicates, and infinite loops.
ALREADY = {"NA1_4999862437": 1}
match_ids = bfs_get_match_ids(AMOUNT, START, ALREADY, YOUR_API_KEY)

# Enter the csv file you want to append to.
#CSV_FILE_NAME = "potential/output1.csv"
#INPUT = convert_txt_to_list("potential/input1.txt")
#convert(INPUT, YOUR_API_KEY, CSV_FILE_NAME)


def split_file_and_write_to_files(input_file, file1, file2):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            data = file.readlines()

        # Calculate the midpoint of the list.
        mid_index = len(data) // 2

        # Split the list into two halves.
        first_half = data[:mid_index]
        second_half = data[mid_index:]

        # Write the first half to the first file.
        with open(file1, 'w') as f1:
            f1.writelines(first_half)

        # Write the second half to the second file.
        with open(file2, 'w') as f2:
            f2.writelines(second_half)
        
        print(f"File split successfully. First half written to {file1}, second half written to {file2}.")

    except Exception as e:
        print(f"An error occurred: {e}")



def remove_duplicates(input_file_path, output_file_path):
    try:
        # Read the input file
        with open(input_file_path, 'r') as file:
            data = file.readlines()

        # Remove duplicates by converting the list to a set and back to a list
        unique_data = list(set(data))

        # Sort the data if you want to maintain a specific order (optional)
        unique_data.sort()

        # Write the unique data to the output file
        with open(output_file_path, 'w') as file:
            file.writelines(unique_data)
        
        print(f"Duplicates removed. Unique data written to {output_file_path}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
