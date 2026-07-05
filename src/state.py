current_trivia = {}
current_category = []

def set_trivia(data):
    """A helper function to update the global variable."""
    global current_trivia
    current_trivia = data

def set_category(category_name):
    global current_category
    current_category = current_trivia[category_name]