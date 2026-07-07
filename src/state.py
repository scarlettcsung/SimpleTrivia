# src/state.py

# Define these at the top level of the file
current_trivia = {}
current_category_name = None
current_category = []
used_questions = set()

def set_trivia(data):
    global current_trivia
    current_trivia = data

def get_available_questions(category_name):
    all_questions = current_trivia.get(category_name, [])
    return [q for q in all_questions if q["question"] not in used_questions]

def mark_question_as_used(question_text):
    global used_questions
    used_questions.add(question_text)

def set_category(category_name):
    global current_category_name
    current_category_name = category_name
