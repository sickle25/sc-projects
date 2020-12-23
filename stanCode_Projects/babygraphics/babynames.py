"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys

PUNCTUATION = '.;!?#&-\'_+=/\\"@$^%()[]{}~ \n'

def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    change = 0  # When obtaining data, the data structure cannot be changed at the same time.

    if name not in name_data:
        name_data[name] = {year: rank}


    else:
        for y in name_data[name]:
            if year not in name_data[name]:
                change = 1
            else:
                if int(name_data[name][y]) > int(rank):
                    change = 1

    if change == 1:
        change = 0
        name_data[name][year] = rank



def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """

    with open (filename,'r') as f:
        for line in f:
            new_line = ''
            for word in line:
                if word not in PUNCTUATION:
                    new_line += word
            list = new_line.split(',')


            if len(list) == 1:
                year = list[0]

            else:
                rank = list[0]
                name1 = list[1]
                name2 = list[2]

                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)




        # name = name2
        # add_data_for_name(name_data, year, rank, name)
        # add_data_for_name(name_data, year, rank, name2)








def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for i in range(len(filenames)):
        add_file(name_data, filenames[i])


    return name_data

def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    # Convert the name to lowercase first, then search.
    matching_names = []
    for line in name_data:
        name = line

        n = name.lower()
        in_word = target.lower()
        check = n.find(in_word)
        if check != -1:
            matching_names.append(name)


    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args


    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
