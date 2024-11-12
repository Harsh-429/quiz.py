import tkinter as tk
from tkinter import messagebox
import random

# Questions pool with example questions; add more as needed.
questions_pool = [
    {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "12"], "answer": "8"},
    {"question": "Which keyword is used to define a function in Python?", "options": ["function", "define", "def", "func"], "answer": "def"},
    {"question": "How do you start a comment in Python?", "options": ["//", "#", "/*", "<!--"], "answer": "#"},
    {"question": "What is the output of print(5 % 2)?", "options": ["1", "2", "0", "5"], "answer": "1"},
    {"question": "Which data type is mutable?", "options": ["tuple", "int", "str", "list"], "answer": "list"},
    {"question": "What does 'len' function return?", "options": ["Sum", "Length", "Type", "None"], "answer": "Length"},
    {"question": "What is used to handle exceptions?", "options": ["try-except", "if-else", "for loop", "while loop"], "answer": "try-except"},
    {"question": "What is the output of print(3 * 'Hi')?", "options": ["3", "Hi", "HiHiHi", "Error"], "answer": "HiHiHi"},
    {"question": "Which keyword is used to start a loop?", "options": ["while", "def", "lambda", "return"], "answer": "while"},
    {"question": "How is a set defined in Python?", "options": ["[]", "{}", "()", "''"], "answer": "{}"},
    {"question": "What is the correct way to create a dictionary?", "options": ["dict()", "{}", "[]", "()"], "answer": "{}"}
]

# Select 10 questions from the pool
questions = random.sample(questions_pool, min(10, len(questions_pool)))

# Initialize quiz variables
current_question = 0
score = 0
mistakes = []  # Store mistakes as dictionaries with question, selected answer, and correct answer

# Function to load the next question
def load_question():
    global current_question
    if current_question < len(questions):
        question_data = questions[current_question]
        
        # Update question and progress labels
        progress_label.config(text=f"Question {current_question + 1} of {len(questions)}")
        feedback_label.config(text="")
        question_label.config(text=question_data["question"])
        
        # Load options into buttons
        for i, btn in enumerate(options_buttons):
            if i < len(question_data["options"]):
                btn.config(text=question_data["options"][i], state=tk.NORMAL, bg="#4a7a8c")
            else:
                btn.config(text="", state=tk.DISABLED)
    else:
        show_result()

# Function to check the answer and provide feedback
def check_answer(selected_option):
    global current_question, score
    question_data = questions[current_question]

    # Disable buttons after selecting an answer
    for btn in options_buttons:
        btn.config(state=tk.DISABLED)

    # Check answer and update feedback
    selected_answer = question_data["options"][selected_option]
    if selected_answer == question_data["answer"]:
        score += 1
        feedback_label.config(text="Correct!", fg="#3fa34d")
    else:
        feedback_label.config(text="Incorrect!", fg="#d9534f")
        # Store the incorrect answer details
        mistakes.append({
            "question": question_data["question"],
            "selected": selected_answer,
            "correct": question_data["answer"]
        })

    # Move to the next question after a short delay
    current_question += 1
    root.after(1000, load_question)

# Function to show the final score and mistakes
def show_result():
    result_text = f"Your score is: {score}/{len(questions)}\n\n"
    
    if mistakes:
        result_text += "Mistakes:\n"
        for mistake in mistakes:
            result_text += f"Q: {mistake['question']}\n"
            result_text += f"Your answer: {mistake['selected']} | Correct answer: {mistake['correct']}\n\n"
    else:
        result_text += "Perfect score! Well done!"
    
    messagebox.showinfo("Quiz Result", result_text)
    root.quit()

# Set up the GUI
root = tk.Tk()
root.title("Quiz Blaster")
root.geometry("600x500")
root.config(bg="#f8f9fa")

# Header frame
header_frame = tk.Frame(root, bg="#0275d8", pady=10)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="Quiz Time!", font=("Helvetica", 24, "bold"), fg="white", bg="#0275d8")
header_label.pack()

# Progress label
progress_label = tk.Label(root, text=f"Question {current_question + 1} of {len(questions)}", font=("Arial", 14), bg="#f8f9fa", fg="#555")
progress_label.pack(pady=10)

# Question frame
question_frame = tk.Frame(root, bg="#f8f9fa", padx=20, pady=10)
question_frame.pack(fill="both", expand=True)

question_label = tk.Label(question_frame, text="", font=("Arial", 16, "bold"), bg="#f8f9fa", wraplength=500, fg="#333")
question_label.pack(pady=20)

# Option buttons with rounded style
options_buttons = []
for i in range(4):
    btn = tk.Button(question_frame, text="", font=("Arial", 12), width=30, height=2, bg="#4a7a8c", fg="white",
                    relief="solid", bd=1, command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    options_buttons.append(btn)

# Feedback label
feedback_label = tk.Label(root, text="", font=("Arial", 12), bg="#f8f9fa")
feedback_label.pack(pady=20)

# Footer frame
footer_frame = tk.Frame(root, bg="#0275d8", pady=5)
footer_frame.pack(fill="x")

footer_label = tk.Label(footer_frame, text="Good Luck!", font=("Arial", 12), fg="white", bg="#0275d8")
footer_label.pack()

# Load the first question
load_question()

# Start the main event loop
root.mainloop()
