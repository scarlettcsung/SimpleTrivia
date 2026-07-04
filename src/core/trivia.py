import random

def pick_random_question(category_object:list):
    question = {}
    if len(category_object) <= 1:
        idx = random.randrange(len(category_object))
        question = category_object.pop(idx)
    else:
        return None
    return question
import random

def give_question(question_object:dict):
    return question_object["question"]

def give_answer(question_object:dict):
    return question_object["answer"]