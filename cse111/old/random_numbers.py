import random
import math

def main():
    #Variables
    numbers = [16.2, 75.1, 52.3]
    words_list = ["apple", "banana", "cherry"]
    
    #Output
    print("Original numbers:", numbers)
    append_random_numbers(numbers)
    print("Numbers after appending:", numbers)
    append_random_numbers(numbers, quantity=3)
    print("Numbers after appending:", numbers)
    
    #Continue with words
    end = input("Do you want to append random words? (yes/no): ")
    if end.strip().lower() == 'yes':
        append_random_words(words_list, quantity=2)
        print("Words after appending:", words_list)
    else:
        print("No words appended.")
        print("Get lost man")
        print("Okay you don't have to leave, but no words will be appended.")
        end = input("You sure you don't want to append words? (yes/no): ")
        if end.strip().lower() == 'yes':
            append_random_words(words_list, quantity=2)
            print("Words after appending:", words_list)
        else:
            print("No words appended.")

def append_random_numbers(numbers, quantity=1):
    '''Append random numbers to the list.'''
    for i in range(quantity):
        rand_num = round(random.uniform(1, 100), 1)
        numbers.append(rand_num)
        print("Appended random number:", rand_num) 
    
def append_random_words(words_list, quantity=1):
    '''Append random words to the list.'''
    for i in range(quantity):
        word = random.choice(["apple", "banana", "cherry", "date", "elderberry"])
        words_list.append(word)
        print("Appended random word:", word)

if __name__ == "__main__":
    main()
