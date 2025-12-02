import random
import math

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think",
                     "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    return random.choice(words)

def get_preposition():
    words = [
        "about", "above", "across", "after", "along", "around", "at", "before",
        "behind", "below", "beyond", "by", "despite", "except", "for", "from",
        "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past",
        "to", "under", "with", "without"
    ]
    return random.choice(words)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {adjective} {noun}"

def get_adjective():
    words = ["tall", "funny", "quiet", "noisy", "red", "fast", "small", "busy", "lazy", "happy"]
    return random.choice(words)

def get_adverb():
    words = ["quickly", "happily", "sadly", "loudly", "calmly", "gracefully", "eagerly", "sweetly"]
    return random.choice(words)

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    adverb = get_adverb()
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {adjective} {noun} {prepositional_phrase1} {adverb} {verb} {prepositional_phrase2}."
    return sentence

def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

main()
