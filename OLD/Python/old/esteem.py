import math
import random

scores = []
positive = []
negative = []


def positive_scores(positive):
    '''Calculate the scores for the positive quesitons with D = 0, d = 1, a = 2 and A = 3'''
    for i in range(len(positive)):
        if positive[i] == 'D':
            scores.append(0)
        elif positive[i] == 'd':
            scores.append(1)
        elif positive[i] == 'a':
            scores.append(2)
        elif positive[i] == 'A':
            scores.append(3)
    return scores


def negative_scores(negative):
    '''Calculate the scores for the negative questions with D = 3, d = 2, a = 1 and A = 0'''
    for i in range(len(negative)):
        if negative[i] == 'D':
            scores.append(3)
        elif negative[i] == 'd':
            scores.append(2)
        elif negative[i] == 'a':
            scores.append(1)
        elif negative[i] == 'A':
            scores.append(0)
    return scores


def calculate_esteem(positive, negative, scores):
    positive_scores(positive)
    negative_scores(negative)
    total_score = sum(scores)
    if total_score < 15:
        return "Low"
    elif 30 <= total_score:
        return "High"



def main():
    questions = [
        'I feel that I am a person of worth, at least on an equal plan2e with others.',
        'I feel that I have a number of good qualities.',
        'All in all, I am inclined to feel that I am a failure.',
        'I am able to do things as well as most other people.',
        'I feel I do not have much to be proud of.',
        'I take a positive attitude toward myself.',
        'I wish I could have more respect for myself.',
        'I certainly feel useless at times.',
        'At times I think I am no good at all.',
    ]
    print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    
    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]} (D/d/a/A): ")
        response = input("Enter D, d, a, or A: ").strip()
        if response not in ['D', 'd', 'a', 'A']:
            print("Invalid input. Please enter D, d, a, or A.")
            continue 
        if i in [1, 2, 4, 6, 7]:
            positive.append(response)
        else:
            negative.append(response)
        
    
    positive_scores(positive)
    negative_scores(negative)
    
    print("Your self-esteem score is:", sum(scores))
    print("Your self-esteem level is:", calculate_esteem(positive, negative, scores))
    
main()
