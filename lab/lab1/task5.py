

def run_quiz(questions):
    score = 0
    total = len(questions)
    for question, answers in questions.items():
        print(question)
        user_answer = input().strip().lower()
        if user_answer in answers:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"You got {score} out of {total} correct.")
    if score / total >= 0.7:
        print("You win!")
    else:
        print("You lose.")

questions = {
    "What is the capital of France?": {"paris"},
    "Who is the current president of the United States?": {"joe biden"},
    "What are the colors in the French flag?": {"blue", "white", "red"},
    "What is the currency of Japan?": {"yen"}
}

run_quiz(questions)
