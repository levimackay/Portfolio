import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    student_list = read_compound_list("pupils.csv")
    birthday = lambda row: row[BIRTHDATE_INDEX]
    student_list.sort(key=birthday)
    print("Oldest to youngest:")
    print_list(student_list)
    student_list.sort(key=lambda row: row[GIVEN_NAME_INDEX])
    print("\nBy Given Name:")
    print_list(student_list)
    print("\nBy birth month and day:")
    student_list.sort(key=lambda row: (row[BIRTHDATE_INDEX][5:7], row[BIRTHDATE_INDEX][8:10]))
    print_list(student_list)

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(student_list):
    """Print the contents of a compound list.

    Parameter
        compound_list: the compound list to print.
    """
    read_compound_list("pupils.csv")
    for row in student_list:
        print(f"[{row[GIVEN_NAME_INDEX]} {row[SURNAME_INDEX]}, {row[BIRTHDATE_INDEX]}]")
    
if __name__ == "__main__":
    main()