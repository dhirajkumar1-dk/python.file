#Question--- Quiz Application
# concept--- Lists , Loops , Random , Dictionaries.

import time

def run_quiz():
    questions = [
        {
            "questio]9: "Which programming language is known as the 'language of the web'?",
            "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
            "answer": "B"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .pyt", "B. .pt", "C. .py", "D. .pw"],
            "answer": "C"
        },
        {
            "question": "Which of the following data types is immutable in Python?",
            "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
            "answer": "C"
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "A. Central Processing Unit", 
                "B. Central Performance Unit", 
                "C. Computer Processing Unit", 
                "D. Control Processing Unit"
            ],
            "answer": "A"
        }
    ]

    score = 0
    total_questions = len(questions)

    print("=" * 45)
    print("   WELCOME TO THE PYTHON QUIZ APPLICATION!   ")
    print("=" * 45)
    print("Answer by typing A, B, C, or D for each question.\n")
    time.sleep(1)

    for idx, item in enumerate(questions, 1):
        print(f"Question {idx}: {item['question']}")
        for option in item['options']:
            print(f"  {option}")
        
        # Input validation
        while True:
            user_answer = input("\nYour answer: ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input! Please enter A, B, C, or D.")

        # Check answer
        if user_answer == item['answer']:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Incorrect! The correct answer was {item['answer']}.\n")
        
        print("-" * 45)

    # Final Results
    percentage = (score / total_questions) * 100
    print("\n" + "=" * 45)
    print("                QUIZ RESULTS                 ")
    print("=" * 45)
    print(f"Final Score : {score} / {total_questions}")
    print(f"Percentage  : {percentage:.1f}%")
    
    if percentage == 100:
        print("Performance : Perfect score! Excellent job! ")
    elif percentage >= 70:
        print("Performance : Great effort! ")
    else:
        print("Performance : Keep practicing! ")
    print("=" * 45)

if __name__ == "__main__":
    run_quiz()