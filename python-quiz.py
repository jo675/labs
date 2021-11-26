questions = [
    'what is 1 + 1?',
    'what is 2 + 2?',
    'what is 3 + 3?',
    'what is 4 + 4?',
]
user_answers = []

correct_answers = [
    2,
    4,
    6,
    8,
]
def menu():
    """welcome menu"""
    print('welcome to math quiz')

def ask_questions():
    """ask question from user"""
    for question in questions:
        print(question)
        try:
            user_answers.append(int(input()))
        except ValueError:
            user_answers.pop            
            print('wrong option, please enter a number')
            print(question)
            user_answers.append(int(input()))
            
                          
def get_score(user_answers, correct_answers):
    """compare the answers from the user with correct answers"""
    score = []
    for i in range(4):    
        if user_answers[i] == correct_answers[i]:
            score.append(1)
    return sum(score)

def show_result():
    """show user the result of quiz and if passed or failed"""
    total_score = get_score(user_answers, correct_answers)
    print(f'Your score is {total_score}')

    if total_score >= 3:
        print('you pass the quiz')
    elif total_score < 3:
        print('you fail the quiz')

menu()
ask_questions()
show_result()
