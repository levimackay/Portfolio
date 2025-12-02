import time

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def main():
    intro = [
        "========================================",
        "Hey, I'm Levi Mackay 👋",
        "I'm 21 and studying Computer Science.",
        "",
        "Some quick facts about me:",
        "- I'm from Mountain Home, Idaho.",
        "- I served a 2-year mission in the Balkans.",
        "- I snowboard a lot.",
        "- I like coding, lifting, and playing guitar.",
        "- I'm a Mariners fan.",
        "========================================"
    ]

    for line in intro:
        slow_print(line)
        time.sleep(0.3)

    person = input("What is your name? ")
    slow_print(f"Nice to meet you, {person}!")
    question = input("Do you have any questions for me? (Press Enter to continue)")
    if question != "":
        slow_print("I don't have time to write that code right now. It was good to meet you though!")
        time.sleep(1)
    else:
        slow_print("I don't have time to write that code right now. It was good to meet you though!")
        time.sleep(1)
        
main()
