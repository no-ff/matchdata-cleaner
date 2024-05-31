def convert_txt_to_list(file_name):
    with open(file_name, "r") as this:
        data = this.readlines()
    new = []
    for i in data:
        new.append(i[:-1])
    return new


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
