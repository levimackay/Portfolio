# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1695, 1752],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1737, 1803],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1802, 1858],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1899, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1829],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    for person_key, person_data in people_dict.items():
        name = person_data[NAME_INDEX]
        birth_year = person_data[BIRTH_YEAR_INDEX]
        death_year = person_data[DEATH_YEAR_INDEX]

        if death_year == 0:
            age_at_death = "N/A"
        else:
            age_at_death = death_year - birth_year
        print(f"{name} died at age {age_at_death}. ({birth_year} - {death_year})")
    pass


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    male_count = 0
    female_count = 0
    for person_key, person_data in people_dict.items():
        gender = person_data[GENDER_INDEX]
        if gender == 'M':
            male_count += 1
        elif gender == 'F':
            female_count += 1
    print(f"Number of males: {male_count}");
    print(f"Number of females: {female_count}");
    
    pass


def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    for marriage_key, marriage_data in marriages_dict.items():
        husband_key = marriage_data[HUSBAND_KEY_INDEX]
        wife_key = marriage_data[WIFE_KEY_INDEX]
        wedding_year = marriage_data[WEDDING_YEAR_INDEX]
        
        husband_data = people_dict[husband_key]
        husband_name = husband_data[NAME_INDEX]
        husband_birth_year = husband_data[BIRTH_YEAR_INDEX]
        husband_age_at_wedding = wedding_year - husband_birth_year

        wife_data = people_dict[wife_key]
        wife_name = wife_data[NAME_INDEX]
        wife_birth_year = wife_data[BIRTH_YEAR_INDEX]
        wife_age_at_wedding = wedding_year - wife_birth_year

        print(f"{husband_name} (age {husband_age_at_wedding}) "
              f"married {wife_name} (age {wife_age_at_wedding}) "
              f"in {wedding_year}.")
    
    pass
'''
def count_marriages(marriages_dict):
    """Count and print the number of marriages in for each person and then display for each person.

    Parameter
        marriages_dict: a dictionary that contains data about marriages
            Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
    Return: nothing
    """
    if not marriages_dict:
        print("No marriages found.")
        return
    marriage_count = []
    for marriage_key, marriage_data in marriages_dict.items():
        husband_key = marriage_data[HUSBAND_KEY_INDEX]
        wife_key = marriage_data[WIFE_KEY_INDEX]

        if husband_key in marriage_count:
            marriage_count[husband_key] += 1
        else:
            marriage_count[husband_key] = 1

        if wife_key in marriage_count:
            marriage_count[wife_key] += 1
        else:
            marriage_count[wife_key] = 1
for person_key, count in marriage_count.items():
    person_name = people_dict[person_key][NAME_INDEX]
    print(f"{person_name} has {count} marriage(s).")
    pass
'''
if __name__ == "__main__":
    main()
